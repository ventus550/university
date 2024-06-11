library(glmnet)
library(SLOPE)
library(bigstep)
library(ggplot2)
library(tidyr)
library(gridExtra)
library(knockoff)



generate.data = function(n = 500, p = 450, k = 5) list(
	X = matrix(data = rnorm(n * p, 0, sd=sqrt(1/n)), nrow = n),
	β = 10 * (1:p %in% seq(1, k))
)

estimate.knockoffs = function(model, k, n = 500, p = 450, iters=100) {
	data = generate.data(n = n, p = p, k = k)
	X = data$X
	β = data$β

	iter = function() {
		y = X %*% β + 2*rnorm(n, 0, 1)

		knockoffs = function(X) create.gaussian(X, rep(0, ncol(X)), diag(ncol(X)))
		coefs = knockoff.filter(X, y, knockoffs, statistic = model, fdr = 0.2)$selected
		ncoefs = length(coefs)
		
		return(c(
			power = sum(coefs <= k) / k,
			fdp = sum(coefs > k) / (ncoefs + (ncoefs == 0))
		))
	}
	suppressWarnings(rowMeans(replicate(iters, iter())))
}

stat_ridge <- function(X, X_k, y) {
  stat.glmnet_coefdiff(X, X_k, y,
    alpha = 0,
    intercept = FALSE,
    standarize = FALSE
  )
}

estimate.knockoffs(stat_ridge, k=5, iters=100)
estimate.knockoffs(stat_ridge, k=20, iters=100)
estimate.knockoffs(stat_ridge, k=50, iters=100)

stat_lasso1 <- function(X, X_k, y) {
  stat.glmnet_coefdiff(X, X_k, y,
    alpha = 1,
    intercept = FALSE,
    standarize = FALSE
  )
}

estimate.knockoffs(stat_lasso1, k=5, iters=100)
estimate.knockoffs(stat_lasso1, k=20, iters=100)
estimate.knockoffs(stat_lasso1, k=50, iters=100)

estimate.net = function(k, n = 500, p = 450, iters=100, alpha=1) {
	data = generate.data(n = n, p = p, k = k)
	X = data$X
	β = data$β

	iter = function() {
		y = X %*% β + 2*rnorm(n, 0, 1)
		B = coef(cv.glmnet(X, y, alpha=alpha, intercept=F, standarize=F))[-1,]
		coefs = which(B != 0)
		ncoefs = length(coefs)

		return(c(
			E1  = sum((B - β)**2),
			E2  = sum((X %*% (B - β))**2),
			power = sum(coefs <= k) / k,
			fdp = sum(coefs > k) / (ncoefs + (ncoefs == 0))
		))
	}
	suppressWarnings(rowMeans(replicate(iters, iter())))
}

# ridge
estimate.net(alpha=0, k=5, iters=100)
estimate.net(alpha=0, k=20, iters=100)
estimate.net(alpha=0, k=50, iters=100)

# lasso
estimate.net(alpha=1, k=5, iters=100)
estimate.net(alpha=1, k=20, iters=100)
estimate.net(alpha=1, k=50, iters=100)

estimate.ols = function(k, n = 500, p = 450, iters=100) {
	data = generate.data(n = n, p = p, k = k)
	X = data$X
	β = data$β

	iter = function() {
		y = X %*% β + 2*rnorm(n, 0, 1)
		B = coef(glmnet(X, y, alpha=0, lambda=0, intercept=F, standarize=F))[-1,]

		return(c(
			E1  = sum((B - β)**2),
			E2  = sum((X %*% (B - β))**2)
		))
	}
	suppressWarnings(rowMeans(replicate(iters, iter())))
}

estimate.ols(k=5, iters=100)
estimate.ols(k=20, iters=100)
estimate.ols(k=50, iters=100)


