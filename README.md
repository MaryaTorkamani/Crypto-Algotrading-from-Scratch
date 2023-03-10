# Crypto-Data-Analysis
The Goal: Complementary data analysis in cryptocurrency historical data in order to get insight for our next Algotrading project.

First of all we need a roadmap for this project to know where to begin our journey and what steps are ahead of us.
Below you can find a simplified roadmap for starting out our data analysis.
![Algotrading roadmap](https://user-images.githubusercontent.com/100773115/215308335-3d344d94-a3bd-4917-b748-45e1f7323e03.jpg)

The first necessary thing to do is to get data. Data must be reliable and consistent, so the best source will always be the brokers you want to work with(in this case Binance). Nowadays, brokers have very comprehensive APIs, capable of providing reliable data, with generous frequency, but everything depends on what type of analysis and trades you want to make. At first we were supposed to acquire our historical data through yahoo finance (yfinance library), but due to yfinance limitation regarding some tokens we are just using Binance API.
Now it is time to select our coins to analyze. We got to select them not only based on their market cap, but also consider different aspect of them, e.g Utility and correlation with BTC.
Next step after capturing and preparing data is a step called by some people, Strategy Factory. Below you can see overview of this step.
![SmartSelect_20230206_170758_miMind](https://user-images.githubusercontent.com/100773115/216987573-0c0d0036-3362-4830-b30c-1fc4d99f08dc.jpg)
