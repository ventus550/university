library(ellipse)
library(ggplot2)
library(mvtnorm)
library(gridExtra)

data = read.table("BankGenuine.txt", header = FALSE, sep = "")
names(data) = c("LENGTH", "LEFT", "RIGHT", "BOTTOM", "TOP", "DIAGONAL")
data <- apply(data, 2, as.numeric)

head(data)

par(mfrow = c(6, 2), mar=c(4.1, 4.1, 4.1, 2.1))
options(repr.plot.width=18, repr.plot.height=18)

for (i in 1:6) {
	Sample = data[,i]
	hist(Sample, density=50, breaks=16, prob=TRUE, main="Histogram")
	curve(dnorm(x, mean=mean(Sample), sd=sqrt(var(Sample))), col="darkred", lwd=3, add=TRUE)

	qqnorm(Sample, col = rgb(red = 0, green = 0, blue = 0, alpha = 0.1))
	qqline(Sample, col="darkred", lwd=3)
}

µ = colMeans(data); µ

𝞢 = cov(data); 𝞢

boundary.statistic = function(n, p, level) p*(n-1)/(n-p)*qf(level, p, n-p) / n
is_within_ellipse = function(v, mu, sigma, level = 0.95, n = length(data)) {
	return( t(v - mu) %*% solve(sigma) %*% (v - mu) <= boundary.statistic(n, length(mu), level) )
}

new.means = c(214.97, 130, 129.67, 8.3, 10.16, 141.5)
is_within_ellipse(new.means, µ, 𝞢)[1]

bonferroni.confidence.region = function (data, conf.level=0.95) {
	bonferroni.conf.level = conf.level / ncol(data)
	ttest.confidence.interval = function (sample, conf.level)
		t.test(sample, conf.level=bonferroni.conf.level)$conf.int
	
	confidence.intervals = apply(data, 2, ttest.confidence.interval)
	return (confidence.intervals)
}

bonferroni.confidence.region.test = function(data, means, conf.level=0.95) {
	confidence.intervals = bonferroni.confidence.region(data, conf.level=conf.level)
	return( all(apply(t(confidence.intervals) - means, 1, prod) < 0) )
}

bonferroni.confidence.region.test(data, new.means)[1]

regions = bonferroni.confidence.region(data)

# https://rdrr.io/cran/ellipse/man/ellipse.html
confidence.ellipse = function(mu, sigma, which=c(1, 2), level=0.95, rescale = TRUE, n = nrow(data)) {
	plotz = ggplot() + geom_path() + theme_bw()
	
	if (!rescale)
		plotz = plotz + coord_equal()
		
	ellipse_data1 = ellipse(x = sigma, centre = mu[which], which = which, t = boundary.statistic(n, 2, level))
	colnames(ellipse_data1) = c("x", "y")
	plotz = plotz + geom_path(data = ellipse_data1, aes(x, y), color = "black", alpha=sqrt(1-level))

	return(plotz)
}

line.projection = function(µ, 𝞢, m, d=data, which=1) {
	rect.region = t.test(data[,which], conf.level=0.95)$conf.int
	# Plot the line segment representing the interval
	a = rect.region[1]
	b = rect.region[2]
	plot(c(a, b), c(0, 0), type = "l", xlab = "", ylab = "", main = colnames(data)[which])

	# Mark the interval with brackets
	segments(a, 0, b, 0, lwd = 2, col = "black")

	# Mark the point on the line
	points(m[which], 0, pch = 17, col = "darkred", cex=6)
	# axis(1, at = data[,which], las=3)
}

plot.line.projections = function(µ, 𝞢, m, d=data) {
	par(mfrow = c(2, 3), mar=c(4.1, 4.1, 4.1, 4.1), yaxt = "n", pty = "s", bty = "n")
	options(repr.plot.width=18, repr.plot.height=10)
	for (i in 1:6)
		line.projection(µ, 𝞢, m, d=d, which=i)
}

plot.line.projections(µ, 𝞢, new.means)

plane.projection = function(µ, 𝞢, m, d=data, which=c(2, 3)) {
	m = data.frame(t(m[which]))
	colnames(m) = c("x", "y")

	rect.region = bonferroni.confidence.region(d[,which])

	confidence.ellipse(µ, 𝞢, which=which) +
	theme(axis.title.x=element_blank(), axis.title.y=element_blank()) +
	geom_point(d = m, aes(x, y), size=3, alpha=0.8, pch=17, color="darkred") +
	geom_rect(aes(
		xmin=rect.region[1,1],
		xmax=rect.region[2,1],
		ymin=rect.region[1,2],
		ymax=rect.region[2,2]
	), alpha=0, color="grey")
}

text.plot = function(txt) {
	ggplot() + 
	annotate("text", x = 4, y = 25, size=8, label = txt) + 
	theme_void()
}

plot.plane.projections = function(point) {
	options(repr.plot.width=18, repr.plot.height=18)
	plots = vector('list', 36)
	for (i in 1:6) for (j in 1:6) {
		if (i == j) {
			plot = text.plot(colnames(data)[i])
		} else {
			plot = plane.projection(µ, 𝞢, m=point, which=c(j, i))
		}
		plots[[6*(i-1) + j]] = plot
	}
	do.call(grid.arrange, plots)
}

plot.plane.projections(new.means)

new.means2 = c(214.99, 129.95, 129.73, 8.51, 9.96, 141.55)

is_within_ellipse(new.means2, µ, 𝞢)[1]

bonferroni.confidence.region.test(data, new.means2)[1]

plot.plane.projections(new.means2)

new.means3 = c(214.9473, 129.9243, 129.6709, 8.3254, 10.0389, 141.4954)

is_within_ellipse(new.means3, µ, 𝞢)[1]

bonferroni.confidence.region.test(data, new.means3)[1]

plot.plane.projections(new.means3)

multitest = function(p, µ, alpha, method = "bonferroni") {
	false.head = sum(µ != 0)
	# p.values = pnorm(rnorm(p, mean=µ, sd=1))
	# reject.left = p.adjust(p.values, method = method) < alpha
	# reject.rght = 1-p.adjust(p.values, method = method) < alpha
	
	p.values = 2 - 2 * pnorm(abs(rnorm(p, mean=µ, sd=1)))
	# reject.left = p*p.values*2 < alpha
	# reject.rght = 1-p*p.values*2 < alpha

	# q.values = qnorm(p.adjust(p.values, method = method))
	# rejections = abs(q.values) >= qnorm(1-alpha/2/p)
	rejections = p.adjust(p.values, method = method) < alpha
	
	# X = rnorm(p, mean=µ, sd=1)
	# reject.left = X < qnorm(alpha/2/p)
	# reject.rght = X > qnorm(1 - alpha/2/p)
	# rejections = reject.left | reject.rght
	# X = abs(rnorm(p, mean=µ, sd=1))
	# rejections = X >= qnorm(1 - alpha/2/p)

	return(c(
		rejected = any(rejections),
		fdr = sum(rejections[(false.head+1):length(rejections)]) / max(1, sum(rejections)),
		power = sum(rejections[1:(false.head+1)]) / false.head
	))
}

simulate.multiple.testing = function(µ, alpha=0.05, reps=1000){
	p = length(µ)
	bf = replicate(reps, multitest(p, µ, alpha, method="bonferroni"))
	bh = replicate(reps, multitest(p, µ, alpha, method="BH"))
	return(data.frame(
		bf = rowMeans(bf),
		bh = rowMeans(bh)
	))
}

p = 5000
µa = c(rep(sqrt(2 * log(p)), 10), rep(0, p - 10))
simulate.multiple.testing(µa, reps=10000)

µb = c(rep(sqrt(2 * log(p)), 500), rep(0, p - 500))
simulate.multiple.testing(µb, reps=10000)


