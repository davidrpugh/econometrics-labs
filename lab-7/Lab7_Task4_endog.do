capture cd M:\Econometrics\Lab7

capture program drop mysimendog
program define mysimendog, rclass
	drop _all
	set obs 100

* x = regressor, possibly endogenous = correlated with e
* e = error
* z = instrument, correlated with x but not with e

* xe_cov = corr(x,e)
* xe_cov = 0 => x is exogenous
* xe_cov /ne 0 => x is ENDOGENOUS

* xz_cov = corr(x,z)
* xz_cov = 0 => instrument is useless
* xz_cov /ne 0 => instrument is "relevant"
* Bigger xz_cov, "stronger" instrument
* By assumption:
* corr(z,0) = 0

* Create x, z and e using the drawnorm command.
* The covariance matrix is V.
	drawnorm x z e, cov(V)

* Create the dependent variable.
* In the true model, b1 (the constant) =0 and b (the coeff on x) =1.
	gen y = x + e

* Run the regression using OLS
	reg y x
	return scalar b_ols=_coef[x]

* Run the regression using IV
* Use the simple, old and now undocumented "ivreg" command - very fast.
	ivreg y (x = z)
	return scalar b_iv=_coef[x]

end

***********************************************************************
******************** Simulate *****************************************
***********************************************************************

* Create the covariance matrix V(x,z,e):

* V =
*   |    1       xz_cov    xe_cov  |
*   |  xz_cov      1         0     |
*   |  xe_cov      0         1     |

* Column/row 1: x
* Column/row 2: z
* Column/row 3: e
* The ones are the variances of x, z and e.
* The zeros are the covariances of z with u.
* A zero covariance with e makes z an exogenous instrument.
* A nonzero covariance with x makes z a "relevant" instrument.
* Note that be using var(x)=var(z)=var(e)=1, the covariances
* can also be interpreted as correlations.

* We do this using the Stata matrix mini-language (not Mata!).
* This matrix will be used by simulate and mysimendog.

* To run a simulation, remove the comment delimiters /* and */
* (and put them back around the other one).

/*
* Specification 1:
global simnumber=1
global simname "Cov(x,e)=0.3; Cov(x,z)=0.5; n=100"
global xe_cov=0.3
global xz_cov=0.5
global n=100
*/

/*
* Specification 2:
global simnumber=2
global simname "Cov(x,e)=0.1; Cov(x,z)=0.3; n=100"
global xe_cov=0.1
global xz_cov=0.3
global n=100
*/

mat V = (1, $xz_cov , $xe_cov \ $xz_cov, 1, 0 \ $xe_cov, 0, 1)
mat list V

* Simulate.  Obtain coefficient estimates and standard errors.
set more off
* Control the random number seed so that the results are replicatable.
set seed 1
simulate								///
			b_ols=r(b_ols)				///
			b_iv=r(b_iv)				///
			, reps(10000): mysimendog
***********************************************************************
***********************************************************************

**************** Address the "No Moments" Problem *********************
* The IV estimator b_iv has moments up to the degree of
* overidentification, L-K.  Here, the equation is exactly
* identified, L=K, so the IV estimator has no moments at all.
* Thus an attempt to estimate the population mean of b_iv - the first
* moment - with the population mean will fail, because we the sample
* mean can't converge to the population mean if the population mean
* doesn't exist!  The same applies to the second moment: the variance
* of b_iv also doesn't exist in the L=K case.
* If the mean of b_iv doesn't exist, we can't talk about bias or
* the MSE criterion.
* We address this problem by imposing the assumption for b_iv that
* we know the true beta lies in the interval [0,2].  This will give
* our new IV estimator a mean and a variance.  We do the same for OLS.
replace b_iv=0  if b_iv<0
replace b_iv=2  if b_iv>2
replace b_ols=0 if b_ols<0
replace b_ols=2 if b_ols>2
***********************************************************************


* Are the estimates for b biased or unbiased?
twoway												///
		(kdensity b_ols if b_ols>0 & b_ols<2)		///
		(kdensity b_iv if b_iv>0 & b_iv<2)			///
		, xlabel(0 0.5 1 1.5 2) xline(1)			///
		title(Distribution of b)					///
		subtitle("$simname")						///
		name(bias$simnumber, replace)

* Which estimator performs better in terms of bias?
* Which estimator performs better in terms of variance?
* (Just look at the standard deviations.)
sum b_ols b_iv


* Which estimator performs better in terms of MSE (mean squared error)?
gen mse_ols=(b_ols-1)^2
gen mse_iv =(b_iv -1)^2
sum mse_ols mse_iv

* Do this after both simulations have been run:
* graph combine bias1 bias2
* graph export bias1_2.emf, replace

