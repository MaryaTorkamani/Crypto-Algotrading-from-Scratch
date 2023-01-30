# Crypto Risk Factors
Feature selection is very important for analysis and modeling. Our approach to this is to review the literature on risk factors and other work is being done in the cryptocurrency space.
According on [Liu Y, Tsyvinski A, Wu X (2022)](https://doi.org/10.1111/jofi.13119), we select 25 factors that constracted only on
price and market information. There are broadly four groups of factors: **size, momentum, volume, and volatility**.

| Category | Factor | Definition|
| --- | --- | ---|
| `Size` | MCAP | Log last day market capitalization in the portfolio formation week
| `Size` | PRC | Log last day price in the portfolio formation week|
| `Size` | MAXDPRC | The maximum price of the portfolio formation week|
| `Size` | AGE | The number of weeks that have been listed on Coinmarketcap.com|
| `Momentum` | r 1,0 | One-week momentum|
| `Momentum` | r 2,0 | Two-week momentum|
| `Momentum` | r 3,0 | Three-week momentum|
| `Momentum` | r 4,0 | Four-week momentum|
| `Momentum` | r 8,0 | Eight-week momentum|
| `Momentum` | r 16,0 | One-week momentum|
| `Momentum` | r 50,0 | Fifty-week momentum|
| `Momentum` | r 100,0 | Hundred-week momentum|
| `Volume` | VOL| Log average daily volume in the portfolio formation week|
| `Volume` | PRCVOL| Log average daily volume times price in the portfolio formation week|
| `Volume` | VOLSCALED| Log average daily volume times price scaled by market capitalization in the portfolio formation week|
| `Volatility` | BETA| The regression coefficient βi in Ri − Rf = αi + βi CMKT + εi.|
| `Volatility` | BETA2| Beta squared|
| `Volatility` | IDIOVOL| The idiosyncratic volatility is measured as the standard deviation of the residual after estimating Ri − Rf = αi + βi CMKT + εi. The CMKT model is estimated using daily returns of the previous 365 days before the formation week.|
| `Volatility` | RETVOL| The standard deviation of daily returns in the portfolio formation week|
| `Volatility` | RETSKEW| he skewness of daily returns in the portfolio formation week|
| `Volatility` | RETKURT| The kurtosis of daily returns in the portfolio formation week|
| `Volatility` | MAXRET| Maximum daily return of the portfolio formation week|
| `Volatility` | DELAY| Maximum daily return of the portfolio formation week|
| `Volatility` | MAXRET| The improvement of R2 in Ri−Rf =αi+βi CMKT+βi CMKT−1+βi CMKT−2+εi, CMKT CMKT−1 CMKT−2 where CMKT−1 and CMKT−2 are the lagged one and two day coin market index returns, compared to using only current coin market excess returns. The model is estimated using daily returns of the previous 365 days before the formation week.|
| `Volatility` | STDPRCVOL| Log standard deviation of dollar volume in the portfolio formation week|
| `Volatility` | DAMIHUD| The average absolute daily return divided by dollar volume in the portfolio formation week|
