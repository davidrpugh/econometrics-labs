* Based on AJR do file maketable4.do.
* Creates selected regression results for AJR Table 4.

clear
capture log close
cd M:\QM\Lab5
log using Lab5_AJR, replace text

* Preparation.
* Load data and keep only "base sample" countries.
use maketable8, clear
keep if baseco==1

* Task 1: Examine data; estimate using OLS

hist logpgp95
gen pgp95=exp(logpgp95)
hist pgp95

list shortnam logpgp95 pgp95

twoway scatter logpgp95 avexpr, mlabel(shortnam)

* AJR Table 2, column 2, p. 1379
reg logpgp95 avexpr

* AJR Table 2, column 5, p. 1379
* NB: coeff on latitude slightly different from published
reg logpgp95 lat_abst avexpr

* Task 2: Is logem4 a good instrument for avexpr?

twoway (scatter avexpr logem4, mlab(shortnam)) (lfit avexpr logem4)

reg avexpr logem4
* Use test to get an F statistic
test logem4

reg avexpr logem4 lat_abst
* Use test to get an F statistic
test logem4

* Task 3: Estimating using IV

* Note that with ivreg2 the first-stage F stat is reported with the output.
ivreg2 logpgp95 (avexpr=logem4)
ivregress 2sls logpgp95 (avexpr=logem4)

* Include latitude
ivreg2 logpgp95 lat_abst (avexpr=logem4)

* Task 4: Is avexpr endogenous?

ivreg2 logpgp95 (avexpr=logem4), endog(avexpr)

ivreg2 logpgp95 lat_abst (avexpr=logem4), endog(avexpr)

* Task 5: An overidentified model

* Is euro1900 a good instrument for avexpr?
twoway (scatter avexpr euro1900, mlab(shortnam)) (lfit avexpr euro1900)
reg avexpr euro1900
test euro1900

* Estimate using the two instruments separately.
* Use the same estimation sample.
ivreg2 logpgp95 (avexpr=euro1900)
ivreg2 logpgp95 (avexpr=logem4) if e(sample)

* Estimate using both instruments.
* Also examine the first-stage regression.
ivreg2 logpgp95 (avexpr=logem4 euro1900), first

capture log close
