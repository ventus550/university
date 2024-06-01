library(glmnet)
library(SLOPE)
library(bigstep)
library(ggplot2)
library(tidyr)
library(gridExtra)


# data = scale(get(load("Lab3.Rdata")) - 10)
data = get(load("Lab3.Rdata"))
data = apply(data - 10, 2, function(col) col / sd(col))

data[1:5,]

par(mfrow = c(6, 2), mar=c(4.1, 4.1, 4.1, 2.1))
options(repr.plot.width=18, repr.plot.height=18)

for (i in 1:6) {
	Sample = data[,i]
	hist(Sample, density=50, breaks=16, prob=TRUE, main="Histogram")
	curve(dnorm(x, mean=mean(Sample), sd=sqrt(var(Sample))), col="darkred", lwd=3, add=TRUE)

	qqnorm(Sample, col = rgb(red = 0, green = 0, blue = 0, alpha = 0.1))
	qqline(Sample, col="darkred", lwd=3)
}

first = data[1:5,]; first
µmle = as.matrix(as.numeric(colMeans(first)))
µ = as.matrix(as.numeric(colMeans(data[6:210,])))
# µ = as.matrix(as.numeric(colMeans(data)))

xnorm = sum(µmle**2)
µjs.zero = (1 - (1/25)*(ncol(data) - 2) / xnorm) * µmle

# should we use true mean here?
xnorm = sum((µmle - µ)**2)
µjs.mean = µ + (1 - (1/25)*(ncol(data) - 2) / xnorm) * (µmle - µ)

plot(µ, µmle, col = "darkred", asp = 1, frame = FALSE, pch=10)
points(µ, µjs.zero, col = "darkblue", pch=20)
points(µ, µjs.mean, col = "darkgreen", pch=22)
abline(0, 1, col = "gray")
legend(
	"bottomright",
	legend = c("Maximum likelihood estimator", "Schrink to zero", "Shrink to common mean"),
	col = c("darkred", "darkblue", "darkgreen"),
	pch = c(10, 20, 22),
	cex = 0.8,
)

sum((µ - µmle)**2)

sum((µ - µjs.zero)**2)

sum((µ - µjs.mean)**2)

n = 1000; p = 950
X = matrix(data = rnorm(n * p, 0, sqrt(1e-3)), nrow = n)

model.prediction.error = function(p) {
	β = rep(0, p)
	β[1:min(5, p)] <- 3
	X = X[,1:p]

	e = rnorm(n, 0, 1)
	y = X %*% β + e

	B = solve(t(X) %*% X) %*% t(X) %*% y

	Y =  X %*% B 
	RSS = sum((Y - y)**2)
	M = X %*% solve(t(X) %*% X) %*% t(X)
	var = RSS / (n - p)

	return(c(
		PE  = sum((X %*% (β - B))**2) + 1*n,
		PE1 = RSS + 2*var*p,
		PE2 = RSS + 2*1*p,
		PE3 = sum(((Y - y) / (1 - diag(M)))**2)
	))
}

rowMeans(replicate(100, model.prediction.error(2)))
rowMeans(replicate(100, model.prediction.error(5)))
rowMeans(replicate(100, model.prediction.error(10)))
rowMeans(replicate(100, model.prediction.error(100)))
rowMeans(replicate(100, model.prediction.error(500)))
rowMeans(replicate(100, model.prediction.error(950)))

residual.boxplots = function(p) {
	estimators = t(data.frame(replicate(30, model.prediction.error(p))))
	residuals = (estimators - estimators[,1])[, -1]
	data = gather(data.frame(residuals), key = "PE", value = "Value")
	return(
		ggplot(data, aes(x=PE, y=Value, color=PE)) +
		geom_boxplot() +
		theme_minimal() +
		ggtitle(paste(p, " variables")) +
		ylab("Error") +
		theme(plot.title = element_text(size = 16, face = "bold", hjust = 0.5))
	)
}

grid.arrange(
	residual.boxplots(2),
	residual.boxplots(5),
	residual.boxplots(10),
	residual.boxplots(100),
	residual.boxplots(500),
	residual.boxplots(950),
ncol = 3)

n = 1000; p = 950
X = matrix(data = rnorm(n * p, 0, sqrt(1e-3)), nrow = n)
β = rep(0, p); β[1:20] <- 6
e = rnorm(n, 0, 1)
y = X %*% β + e

metrics = function(B) c(
	E1  = sum((B - β)**2),
	E2  = sum((X %*% (B - β))**2),
	FDP = sum(B[21:p] != 0) / sum(B != 0),
	TPP = sum(B[1:20] != 0) / 20
) 

# https://cran.r-project.org/web/packages/bigstep/vignettes/bigstep.html
big = prepare_data(y, X)
results = stepwise(big, crit = mbic2)
discoveries = as.numeric(results$model)

discoveries

B = rep(0, p)
B[discoveries] = as.numeric(get_model(results)$coefficients)[-1]

metrics(B)

# use intercept?
ridge = cv.glmnet(X, y, alpha=0, intercept = F)
ridge.metrics = metrics(coef(ridge)[-1,])

ridge.metrics

lasso = cv.glmnet(X, y, alpha=1)
lasso.min.metrics = metrics(coef(lasso, s = "lambda.min")[-1,])
lasso.1se.metrics = metrics(coef(lasso, s = "lambda.1se")[-1,])

lasso.min.metrics

lasso.1se.metrics

lasso.new = glmnet(X, y, alpha=1, lambda = qnorm(1 - 0.1/2/p)/n)

coef(lasso.new)

lasso.new.metrics

lasso.ols = glmnet(X, y, alpha=1, lambda=0)
lasso.ols.metrics = metrics(coef(lasso)[-1,])
lasso.ols.metrics

glmnet(X, Y, alpha = 1, lambda = 0)

# https://cran.r-project.org/web/packages/SLOPE/vignettes/introduction.html
slope = SLOPE(X, y, lambda = qnorm(1 - seq(1, 950, 1)*0.1/2/p)/n)

metrics(coef(slope)[,20][-1])

slope = SLOPE(X, y, lambda=rep(0, 950))
metrics(coef(slope)[,2][-1])


