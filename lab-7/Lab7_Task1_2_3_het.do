capture cd M:\Econometrics\Lab7

use mrw1992, clear

* Keep non-oil-exporters
keep if nonoil

* Keep only the variables we need
keep c_name gdp60 gdp85 pop igdp school

gen lngdp60 = ln(gdp60)
gen lngdp85 = ln(gdp85)

gen growth = (lngdp85 - lngdp60) / 25
label variable growth "average growth rate"

**************************************************************************
* Task 1: The simplified MRW estimation for 105 non-oil-exporters
* Use only initial income per capita and I/Y as regressors

reg growth lngdp60 igdp
* Use FWL/added-variable plots to examine contributions of the Xs.
* avplots (note the "s") will do all these in one picture
avplots

* Use a simple visual inspection of the residuals to decide if it is
* plausible there is heteroskedasticity related to individual Xs.
capture drop ehat
predict ehat, res
scatter ehat lngdp60, nodraw name(GDP, replace)
scatter ehat igdp,    nodraw name(IY, replace)
graph combine GDP IY, name(ols_resid, replace)

* Next, perform the intraocular version of White's test:
* When you estimate using classical vs. robust SEs, are the SEs
* different?  Bigger?  Smaller?  What does this suggest?
reg growth lngdp60 igdp
reg growth lngdp60 igdp, rob

**************************************************************************
* Task 2: White's general test for heteroskedasticity

* Estimate the equation and create the squared residuals
* We use double precision because we want the test stat to be precise.

reg growth lngdp60 igdp
capture drop ehat
predict double ehat, res
gen double ehatsq=ehat^2

* Assemble the levels, squares, and cross-products of the regressors.
* This means:
* 1. Levels: lngdp60 and igdp
* 2. Squares: lngdp60^2 and igdp^2
* 3. Cross-products: lngdp*igdp

* The variables for (1) already exist.
* Create the variables for (2) and (3).
* There won't be any redundancies (this time).

*** Your code here ***

* Perform the artificial regression.
* The dep var is ehatsq.
* The regressors are (1), (2) and (3) above.

*** Your code here ***

* Finally, display the NR2 test statistic
di e(N)*e(r2)

* Confirm you've done it correctly.  It should match the test stat
* reported by Stata's postestimation imtest with the white option.
* How many degrees of freedom does the test have?  Why?

reg growth lngdp60 igdp
estat imtest, white

* How do you interpet the result?

**************************************************************************
* Task 3: White's test with redundancies

* Use a specification that is quadratic in lngdp60:
* lngdp60 appears as a level and as a square.
* Create this new variable:
gen lngdp60sq=lngdp60^2

* There are no other regressors, so as in Task 2 we have 2 regressors
* plus a constant.

* Estimate and create the squared residuals.
reg growth lngdp60 lngdp60sq
capture drop ehat
predict double ehat, res
gen double ehatsq=ehat^2

* Assemble the levels, squares, and cross-products of the regressors.
* Look closely - where is the redundancy?  That is, where are you
* creating a variable that already exists?

*** Your code here ***

* Perform the artificial regression.
* The dep var is ehatsq.
* The regressors are the levels, squares and cross-products
* MINUS ANY REDUNDANCIES.

*** Your code here ***

* Finally, display the NR2 test statistic
di e(N)*e(r2)

* Confirm you've done it correctly.  It should match the test stat
* reported by Stata's postestimation imtest with the white option.

reg growth lngdp60 lngdp60sq
estat imtest, white

* How many degrees of freedom does the test have this time?
* How does this compare to Task 2, when you had the same number
* of regressors?
