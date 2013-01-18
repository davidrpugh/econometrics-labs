* Change working folder to Lab 5 folder for saving graphs
capture cd M:\QM\Lab5

capture program drop mysim
program define mysim, rclass
	drop _all
	set obs 100

* Generate independent variable x and error u
	gen x = rnormal()
	gen u = rnormal()

* Generate the dependent variable y according to the
* following true model: y = b0 + b1*x + u
* b0 (the constant)   = 1
* b1 (the coeff on x) = 1
	gen y = 1 + 1*x + u

* Estimate the model using OLS
	reg y x

* Return the estimated b1 and the estimated SE(b1).
	return scalar b1=_coef[x]
	return scalar se1=_se[x]
end

***********************************************************************
******************** Simulate *****************************************
***********************************************************************
* Simulate.  Obtain coefficient estimate and standard error.
* A new trick - "set more off" means Stata won't stop and ask "More?"
* "more" will be off until the do file stops running.
set more off
* Provide the "seed" for the Monte Carlos.  This guarantees that
* you get the same series of random variables each time.
set seed 1
simulate b1 = r(b1) se1 = r(se1), reps(5000): mysim
***********************************************************************
***********************************************************************

* The model estimated is y = b0 + b1*x + u.
* The null hypothesis is H0: b1=1.
* The test statistic is t=(b1-1)/SE(b1).
* Use the CLT and the Normal distribution for testing.
* The 5% critical values for a 2-tailed test using the
* normal distribution are -1.96 and 1.96

*********** BIAS ************
* Is the estimated b1 biased or unbiased?
sum b1, detail
twoway (kdensity b1), xlabel(0.5 1 1.5) xline(1)		///
	title(Distribution of b) name(bias, replace)

******** TEST SIZE, PART 1 **********
* Test statistic.
capture drop t
gen t=(b1-1)/se1
* How often do you reject the null hypothesis when it's true?
* How often do you reject because the estimated b1 is very large?
* How often do you reject because the estimated b1 is very small?
* Hint: use the count command.

******** TEST SIZE, PART 2 **********
* P-values for a 2-sided test.
* normal(.) is the CDF for the normal distribution,
* normal(a) is the area under the PDF to the LEFT of a,
* 1-normal(a) is the area under the PDF to the RIGHT of a.
* For a 2-sided test, we are interested in the distribution
* of abs(a), which is the HALF-NORMAL distribution.
* The half-normal is just 2 * the positive half of the normal.
* (We rescale by 2 so that the area under the half-normal =1.)
* The CDF of the half-normal is 2*normal(a) - 1 where a >= 0.
* The p-value is the probability of a value at least as extreme
* as the one we observe, so we want the area in the tail to the
* RIGHT of abs(a). The area to the LEFT of a is 2*normal(a)-1,
* so we want 1 - (2*normal(abs(a))-1) = 2*(1-normal(abs(a))).
capture drop p
gen p = 2*(1-normal(abs(t)))
* Interpret the following graph.
hist p, bin(40) percent yline(2.5) title("Size (40 bins, 2.5%)")	///
	name(size, replace)
