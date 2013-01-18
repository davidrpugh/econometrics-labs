capture cd M:\Econometrics\Lab7

use http://fmwww.bc.edu/ec-p/data/Hayashi/griliches76.dta, clear

* Create the year dummies.
* xi will use the prefix "_I" by default; "d" is more intuitive.
capture drop d*
xi i.year, prefix(d)

**** Quick guide to ivreg2 ****
* Basic syntax:
*
* ivreg2 y x1 x2 x3 (v1 v2 = z1 z2 z3 z4), <options>
*    y  = dependent variable
*    xs = exogenous regressors
*    vs = endogenous regressors
*    zs = excluded instruments
*
* Covariance options:
*    nothing = classical S, homoskedasticity assumed
*    robust = robust S_HC, heteroskedasticity-consistent
*
* Estimator options:
*    nothing = OLS or IV
*    gmm2s = 2-step feasible efficient GMM


****** SPECIFICATION 1 ******
* Schooling and IQ endogenous
* IV as efficient GMM
* W = inverse of S_classical
* S_classical also used in AVar
* Replicates Hayashi Table 3.3 Line 3
* What does overid test mean?  How many degrees of freedom and why?

ivreg2 lw expr tenure rns smsa dyear*		///
	(s iq = med kww age mrt)


****** SPECIFICATION 2 ******
* Schooling and IQ endogenous
* IV as inefficient GMM
* W = inverse of S_classical
* S_HC used in AVar
* What does overid test mean?  How many degrees of freedom and why?
* Compare with the previous estimation.  What is the same/different?
ivreg2 lw expr tenure rns smsa dyear*		///
	(s iq = med kww age mrt), robust


****** SPECIFICATION 3 ******
* Schooling and IQ endogenous
* Replicates Hayashi Table 3.3 Line 5
* 2-step Feasible Efficient GMM
* W = inverse of S_HC
* S_HC also used in AVar
* What does overid test mean?  How many degrees of freedom and why?
* Compare with the previous estimations.  What is the same/different?
ivreg2 lw expr tenure rns smsa dyear*		///
	(s iq = med kww age mrt), robust gmm2s


****** SPECIFICATION 4 ******
* Schooling and IQ endogenous
* Replicates Hayashi Table 3.3 Line 1
* OLS as efficient GMM
* W = inverse of S_classical
* S_classical also used in AVar
* Use ivreg2 small option to use same finite-sample formula as
* regress and to report t-stats instead of z-stats.
regress lw s iq expr tenure rns smsa dyear*
ivreg2 lw s expr tenure rns smsa dyear*		///
	(s iq = med kww age mrt), small

	
****** SPECIFICATION 5 ******
* Schooling and IQ exogenous
* OLS as inefficient GMM
* W = inverse of S_classical
* S_HC used in AVar
* What does overid test mean?  How many degrees of freedom and why?
* Compare with the previous estimation.  What is the same/different?
regress lw s iq expr tenure rns smsa dyear*, robust
ivreg2 lw s iq expr tenure rns smsa dyear*		///
	( = med kww age mrt), small robust


****** SPECIFICATION 6 ******
* Schooling and IQ exogenous
* 2-step Feasible Efficient GMM, also known as HOLS
* W = inverse of S_HC
* S_HC also used in AVar
* What does overid test mean?  How many degrees of freedom and why?
* Compare with the previous estimations.  What is the same/different?
ivreg2 lw s iq expr tenure rns smsa dyear*		///
	( = med kww age mrt), small robust gmm2s

