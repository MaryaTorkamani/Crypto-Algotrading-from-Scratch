#Strategy implementation and backtesting

Strategy implementation in backtesting, in contrary to the actual live initialization, needs rapid strategy 
deployment, testing, visualization and comparing instead of "fast initation".

To fulfill this requirements, we have two choices of libraries in python:

##1. Backtesting.py/
	better overall performance and simplicity in strategy implementation, and great visualization and/ 
	comparing, all in one package/
	https://kernc.github.io/backtesting.py/doc/backtesting/#manuals/

##2. vectorBT/
	faster than Backtesting.py in both implementation and backtest process, but lacks easy setup and/ 
	visualization/
	https://vectorbt.dev/#what-is-vectorbt/

_____________________________________________________________________

For the first evaluation, Backtesting.py library was used to emulate the backtesting results of the sma conseq candles on 1d timeframe

To see the list of trades: trade_list.csv
To see an interactive plot of the backtest: SmaConsec.html
