# Robo-Advising

Our strategy is market meet. We first filtered out invalid tickers, such as delisted stocks, stocks that are not in the US/Canada, and stocks that have too little volume. Then we took the historical prices of valid stocks and the two market indices (S&P 500 and the TSX 60) over the period from October 1, 2023 to November 22, 2024, in order to avoid volatility and stock market crash during Covid. Then we averaged the exchange rate over this time period and multiplied the market indicies and US stocks by that value to ensure all values are in CAD for future calculations. 

To select stocks, we calculated the beta and correlation values of each stock return, with respect to the returns of both stock indices. We then ranked the stocks based on how close the beta values are to 1 and how high their correlations with market indices are. The 24 stocks that ranked the highest were selected, thought not all of them will be bought

To determine portfolio weighting, we used a library cvxpy. Using this we created a variable w which is a list of weights. Then we specified that we need to minimize the difference between the index portfolio value and our stocks portfolio value. We put this under a loop so it checks the best weights for different number of stocks, ranging from 12 tot 24. At the end, we use the weights that lead to the closest value to the market. 

