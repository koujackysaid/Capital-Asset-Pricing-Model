# Capital-Asset-Pricing-Model
### Understanding CAPM through linear regression approach, then it is just different format

In linear regression:
y = b + b1(x) + e
- y is dependent value
- b is the y intercept
- b1 is the slope. (from the perspective of graph, from the perspective of formula, it is b1, from practical meaning, it is when the IV change 1 unit, then the DV will change b1 unit)
- x is the independent value, also the predictor
- e is the error terms

In CAPM terms:
return of asseti = alpha + beta(market return) + error term
- alpha is the y intercept
- beta is the slope
- market return is the benchmark, can choose disecrete index

Generally, beta info in Yahoo Finance doesnt consider the risk-free rate, if consider, it would be:
return of asseti - rf = aplha + beta(market return-rf) + error term

### Building the regression model
- stats module has no constant as default
- users need to add one on their own
- OLS stands for ordinary least squares, which is an approach to get a min SSE, max SSR, so the regression line has the biggest explanatory power of the dependent variable
- use the seaborn module to plot the regression model

### Statistical Concept Revision and Interpretation of the results
- refer to the notes of the jupyter notebook file
