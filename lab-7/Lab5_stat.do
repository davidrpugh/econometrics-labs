* Change working folder to Lab 5 folder for saving graphs
capture cd M:\QM\Lab5

capture program drop mysimstat
program define mysimstat, rclass
	drop _all
	set obs 500
	gen t = _n
	tsset t
* Generate x, e and y
* b0 (the constant) =0 and b1 (the coeff on x) =0.
* In this case, in the true model x does NOT affect y.
* So y is simply y = 0 + 0*x + u = u.

	if $stationary==1 {
* Stationary case
		gen x = rnormal()
		gen u = rnormal()
		gen y = u
		}
	else {
* Nonstationary data
		gen x = 0 if t==1			/*  Set initial value of x to 0  */
		gen e1 = rnormal()			/*  White noise error  */
		replace x=L.x + e1 if t>1	/*  x is a random walk  */
		gen u = 0 if t==1			/*  Set initial value of u to 0  */
		gen e2 = rnormal()			/*  White noise error  */
		replace u=L.u + e2 if t>1	/*  u is a random walk  */
		gen y = u					/*  b1=0 so y is just =u  */
		}

* We want to see what happens as t->infinity, so we
* run the regression for t=50, t=100, t=500, and save
* and return each set of results.

	reg y x if t<=50
	return scalar b50 =_coef[x]
	return scalar se50=_se[x]

	reg y x if t<=100
	return scalar b100 =_coef[x]
	return scalar se100=_se[x]

	reg y x if t<=500
	return scalar b500 =_coef[x]
	return scalar se500=_se[x]

end

***********************************************************************
******************** Simulate *****************************************
***********************************************************************
* Set global macro $stationary to be 0 or 1.  This global macro will be
* supplied to simulate and also used in graphing below.
* =1 means data are stationary, =0 means data are nonstationary (and not cointegrated).
global stationary=1

* A new trick - "set more off" means Stata won't stop and ask "More?"
* "more" will be off until the do file stops running.
set more off
simulate b50=r(b50) se50=r(se50) b100=r(b100) se100=r(se100)	///
	b500=r(b500) se500=r(se500), reps(5000): mysimstat
***********************************************************************
***********************************************************************

* Convergence to beta=0?
sum b*, detail
twoway (kdensity b50) (kdensity b100) (kdensity b500), ///
	xline(0) title("Convergence?") name(convergence, replace)

* t-ratios
capture drop t*
gen t50=b50/se50
gen t100=b100/se100
gen t500=b500/se500
sum t*, detail
* The null hypothesis is Ho: beta1=0.
* How often would you reject the null if you use the t-stat
* and the usual Normal critical values of -1.96 and +1.96?
* (Answer: 5% of 5,000 repetitions = 250 times.)
count if t50 < -1.96  | t50  > 1.96
count if t100 < -1.96 | t100 > 1.96
count if t500 < -1.96 | t500 > 1.96

* Examine the distribution of the t-stats.
* This is an example of how to add a standard normal by hand.
twoway 	(kdensity t50 if t50>-25 & t50<25)				///
		(kdensity t100 if t100>-25 & t100<25)			///
		(kdensity t500 if t500>-25 & t500<25)			///
		(function Normal=normalden(x), range(-4 4)) ,	///
		title(t-ratios) name(tratios, replace)

* Size
* P-values for 2-sided tests.
capture drop p*
gen p50  = 2*(1-normal(abs(t50)))
gen p100 = 2*(1-normal(abs(t100)))
gen p500 = 2*(1-normal(abs(t500)))
* An undocumented command that will enable us to cleanly graph the size
* of the test for the 3 cases.  The "h" and "x" variables are what the
* graph histogram command uses internally.  We create these for our own use below.
twoway__histogram_gen p50,  gen(h50   x50,  replace) bin(40) percent
twoway__histogram_gen p100, gen(h100  x100, replace) bin(40) percent
twoway__histogram_gen p500, gen(h500  x500, replace) bin(40) percent
* This is how to label variables.
label var h50  "N=50"
label var h100 "N=100"
label var h500 "N=500"
* Size properties of t-tests.
twoway (line h50 x50) (line h100 x100) (line h500 x500),	///
	yscale(range(0)) ylabel(#5) yline(2.5) ytitle(Percent)	///
	title("Size (40 bins, 2.5%)") name(size, replace)


* Use the global macro to decide what names and titles to use.
* Export the graphs for later use as Windows metafiles.
if $stationary==1 {
	graph combine convergence tratios size,		///
		title(Stationary data) name(stationary, replace)
	graph export stationary.wmf, replace	
	}
else {
	graph combine convergence tratios size,		///
		title(Nonstationary data) name(nonstationary, replace)
	graph export nonstationary.wmf, replace	
	}
