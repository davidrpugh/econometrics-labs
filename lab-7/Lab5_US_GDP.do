capture cd "M:\QM\Lab5"

capture log close
log using US_GDP, text replace

insheet using US_GDP_49_09.csv, names case clear

* Preliminaries

gen t = _n
tsset t
gen ly=ln(GDP)
label var ly "Log(GDP)"
gen tsq=t^2

********** Task 1 ************
* Stata time-series operators

list YEAR  t  GDP  L.GDP  L2.GDP  L3.GDP
list YEAR  t  GDP  L.GDP  F.GDP
list YEAR  t  GDP  L.GDP  L2.GDP  L3.GDP
list YEAR  t  GDP  F.GDP  F2.GDP  F3.GDP
list YEAR  t  GDP  F.L.GDP
list YEAR  t  GDP  D.GDP

gen diff1 = GDP - L.GDP
list YEAR  t  GDP  D.GDP diff1

gen diff2 = GDP - L2.GDP
gen doublediff = diff1 - L.diff1
list YEAR  t  GDP  D.GDP  D2.GDP  diff2  doublediff

********** Task 2 ************
* Inspecting the data

* slide 147

line GDP YEAR, yline(0)
line ly YEAR, yline(0)

* slide 148

line D.GDP YEAR
line D.ly YEAR

********** Task 3 ************
* Modelling log GDP

* slide 149

reg D.ly t

* slide 150

reg ly t tsq
predict lyhat, xb
line ly lyhat YEAR
twoway (qfit ly t) (line ly t)

reg ly t tsq
predict uhat if e(sample), resid
label var uhat "Detrended log GDP"
line uhat YEAR, yline(0)

********** Task 4 ************
* Determining the nonstationary properties of the data:
* Unit-root tests

* slide 166

* delta_0 = delta_1 = 0
reg D.uhat L.uhat, nocons
dfuller uhat, nocons

* delta_0 = delta_1 = 0
reg D.ly L.ly, nocons
dfuller ly, nocons

* delta_0 <> 0 (constant), delta_1 = 0 (trend)
reg D.ly L.ly
dfuller ly

* slide 167

* delta_0, delta_1 <> 0
reg D.ly L.ly t
dfuller ly, trend


********** Task 5 ************
* More unit-root tests

* p. 101

reg D.uhat L.uhat LD.uhat, nocons
dfuller uhat, nocons lags(1)

********** Task 6 ************
* Correlogram analysis

* p. 111

corrgram uhat
ac uhat
pac uhat

wntestq uhat, lags(1)
wntestq uhat, lags(2)

* Slide 177
reg uhat L.uhat L2.uhat, nocons
* Figure 11, slide 178
predict double fitted if e(sample), xb
predict double etahat if e(sample), resid
line uhat fitted YEAR
line etahat YEAR, yline(0)

var uhat, lags(1/2) nocons dfk small
varstable

* Slide 184
irf create ar2, set(myirf, replace)
irf graph irf
irf graph cirf

******** End of Lab *********

capture log close
