capture cd M:\Econometrics\Lab7

capture log close
log using Lab7_Assignment1, replace text

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
* Assignment 1: Replicate Stata's built-in estat hettest

reg growth lngdp60 igdp
capture drop ehat
predict double ehat, res
gen double ehatsq=ehat^2

* The original version of White's general test can suffer from a loss of
* power because it is looking in too many different directions for
* heteroskedasticity.  This will show up in a large number of degrees
* of freedom.  We can increase the power and reduce the degrees of
* freedom by decreasing the dimension of the vector psi in our
* vector of contrasts test.

* Simplest version - use only the levels of the regressors, and
* forget about the squares and cross-products.

*** INSERT YOUR CODE HERE ***
di e(N)*e(r2)

* Confirm it matches Stata's official estat hettest with the
* rhs and iid option.
* NB: omitting the iid option means hettest reports the default
* Breusch-Pagan/Godfrey version, which assumes normality.  The
* assumption of normality is often too strong in economic applications,
* so the iid option (the White version) is preferable.

reg growth lngdp60 igdp
estat hettest, rhs iid

* An alternative is, instead of using the levels of the regressors,
* use a linear combination of the levels of the regressors.  The
* obvious linear combination is the predicted values (yhat) from the
* regression.  Do the following:
* 1. Estimate the original equation.
* 2. Generate the predicted values.
* 3.  Run the White-style artificial regression and report the
*     NR2 test statistic.

*** INSERT YOUR CODE HERE ***
di e(N)*e(r2)

* Confirm it matches Stata's official estat hettest with the iid option.

reg growth lngdp60 igdp
estat hettest, iid

* A third alternative is to use a summary combination of levels
* and squares of the regressors, namely the predicted values
* (yhat) and the squares of the predicted values (yhat^2).

*** INSERT YOUR CODE HERE ***
di e(N)*e(r2)

* You can confirm this vs. the output of the Stata add-in ivhettest.
* ivhettest performs tests for heteroskedasticity for OLS and IV
* estimations, and includes a wide range of options.  See help ivhettest
* for a discussion.  You should use the fitsq option.

* To install ivhettest (you need do this only once):
ssc install ivhettest

* Confirm your test statistic matches that from ihvettest.

reg growth lngdp60 igdp
ivhettest, fitsq

capture log close
