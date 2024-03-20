library("ellipse")
library("ggplot2")

confidence.ellipse = function(mu, sigma, levels=seq(0, 1, 0.1), rescale = TRUE) {
	diago = eigen(sigma)
	vectors = diago$vectors %*% diag(sqrt(diago$values)) + mu
	arrow.size = arrow(length=unit(0.3, 'cm'))

	plotz = ggplot() + geom_path() + theme_bw() +
		geom_segment(aes(x=mu[1], y=mu[2], xend=vectors[1,1], yend=vectors[2,1]), arrow = arrow.size, color = "darkred") +
		geom_segment(aes(x=mu[1], y=mu[2], xend=vectors[1,2], yend=vectors[2,2]), arrow = arrow.size, color = "darkblue")
	
	if (!rescale)
		plotz = plotz + coord_equal()
		
	for (level in levels) {
		ellipse_data1 = ellipse(x = sigma, centre = mu, level = level)
		plotz = plotz + geom_path(data = ellipse_data1, aes(x, y), color = "black", alpha=sqrt(1-level))
	}

	return(plotz)
}


# Problem 2

## 6.
A = matrix(c(3, -1, -1, 3), nrow=2)
e = eigen(A)

## 6.1
cat("P * P^T =\n")
print(round(e$vectors %*% t(e$vectors), 16))

## 6.2
cat("\ndet(A) =", det(A), "\n")
cat("Π(λi) =", prod(e$values), "\n\n")

## 6.3
cat("det(Λ) =", det(diag(e$values)))

## 6.5
cat("\nTest the inverse\n")
print(round(A %*% e$vectors %*% diag(1/e$values) %*% t(e$vectors), 16))

# Problem 3
µ = c(3343, 49.8)
cov = 0.75 * 528 * 2.5
𝞢 = matrix(c(528**2, cov, cov, 2.5**2), nrow=2)
e = eigen(𝞢); e

confidence.ellipse(µ, 𝞢)

# Problem 4
cat("mean = ", 49.8 + 0.75*2.5/528*(4025 - 3343), " var = ", (2.5**2) * (1 - 0.75**2))

# Project
is_within_ellipse = function(v, mu, sigma, level = 0.68) {
	return( t(v - mu) %*% solve(sigma) %*% (v - mu) <= qchisq(level, df=2) )
}

make.plots = function(sample) {
	par(mfrow = c(1, 2))
	options(repr.plot.width=18, repr.plot.height=6)

	hist(sample, density=20, breaks=200, prob=TRUE, main="Histogram")
	curve(dnorm(x, mean=mean(sample), sd=sqrt(var(sample))), col="darkred", lwd=3, add=TRUE)

	qqnorm(sample, col = rgb(red = 0, green = 0, blue = 0, alpha = 0.1))
	qqline(sample, col="darkred", lwd=3)
}

## Part One
data = read.table("WeightLength.txt", header = TRUE, sep = "\t")
mean_weight = mean(data$Weight)
mean_length = mean(data$Length)
var_weight = var(data$Weight)
var_length = var(data$Length)
covariance = cov(data$Weight, data$Length)

cat(
	"mean_weight: ", mean_weight,
	"\nmean_length: ", mean_length,
	"\ncovariance: ", covariance
)

make.plots(data$Weight)
make.plots(data$Length)

µ = c(mean_weight, mean_length)
𝞢 = matrix(cov(data), nrow=2)
confidence.ellipse(µ, 𝞢, list(0.75, 0.95)) 

scores = function(data, µ, 𝞢, levels = list(0.75, 0.95)) {
	df = data.frame(data)
	for (level in levels) {
		df[[paste(level)]] = apply(data, 1, function(v) {is_within_ellipse(v, µ, 𝞢, level = level)})
	}
	df$Score <- rowSums(df[, (ncol(df) - length(levels) + 1):ncol(df)])
	return(df)
}

data.frame(table(Score = scores(data, µ, 𝞢)$Score))

confidence.ellipse(as.numeric(µ), 𝞢, list(0.75, 0.95)) + geom_point(data = scores(data, µ, 𝞢), aes(x = Weight, y = Length, color = Score))

e = eigen(𝞢)
P = e$vectors
Λ = diag(e$values)

cat(
	"decomposition:",
	"\nP: ", P,
	"\nΛ: ", Λ
)

px = as.matrix(data) %*% t(P)
colnames(px) = c("Weight", "Length")
dpx = as.data.frame(px)

ggplot(data, aes(x=Weight, y=Length)) + geom_point()

ggplot(dpx, aes(x=Weight, y=Length)) + geom_point()

## Part Two
data = read.table("ParentsWeightLength.txt", header = TRUE, sep = "\t")
means = colMeans(data)
covrs = cov(data)

### means
µWL = means[3:4]
µFM = means[1:2]

### covariances
𝞢WL = covrs[3:4, 3:4]
𝞢FM = covrs[1:2, 1:2]
𝞢WLFM = covrs[1:2, 3:4]
𝞢FMWL = covrs[3:4, 1:2]

𝞢FM.inv = solve(𝞢FM)

make.plots(data$FatherHeight)
make.plots(data$MotherHeight)
make.plots(data$Weight)
make.plots(data$Length)

µ = function (fm) µWL + 𝞢FMWL %*% 𝞢FM.inv %*% (fm - µFM)
𝞢 = 𝞢WL - (𝞢FMWL %*% 𝞢FM.inv %*% 𝞢WLFM) 

confidence.ellipse(c(0,0), matrix(as.numeric(𝞢), nrow=2), levels=list(0.75, 0.95))

conditional.scores = function(data, µ, 𝞢, levels = list(0.75, 0.95)) {
	conditional.ellipse = function (datarow) {
		lw = datarow[c("Weight", "Length")]
		fm = datarow[c("FatherHeight", "MotherHeight")]
		return(is_within_ellipse(lw, µ(fm), 𝞢, level = level))
	}
	df = data.frame(data)
	for (level in levels) {
		df[[paste(level)]] = apply(data, 1, conditional.ellipse)
	}
	df$Score <- rowSums(df[, (ncol(df) - length(levels) + 1):ncol(df)])
	return(df)
}

data.frame(table(Score = conditional.scores(data, µ, 𝞢)$Score))

(confidence.ellipse(as.numeric(µWL), matrix(as.numeric(𝞢WL), nrow=2), list(0.75, 0.95))
+ geom_point(data = conditional.scores(data, µ, 𝞢), aes(x = Weight, y = Length, color = Score)))

µ = µWL + 𝞢FMWL %*% solve(𝞢FM) %*% (c(185, 178) - µFM)
𝞢 = 𝞢WL - (𝞢FMWL %*% solve(𝞢FM) %*% 𝞢WLFM) 

confidence.ellipse(as.numeric(µ), matrix(as.numeric(𝞢), nrow=2), list(0.75, 0.95))

e = eigen(𝞢)
P = e$vectors
Λ = diag(e$values)

cat(
	"decomposition:",
	"\nP: ", P,
	"\nΛ: ", Λ
)

px = as.matrix(data[c("Weight", "Length")]) %*% t(P)
colnames(px) = c("Weight", "Length")
dpx = as.data.frame(px)

ggplot(data, aes(x=Weight, y=Length)) + geom_point()
ggplot(dpx, aes(x=Weight, y=Length)) + geom_point()