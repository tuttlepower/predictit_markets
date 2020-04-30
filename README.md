# predictit_markets
Simple Python code that helps to retreive predictit market data. 

#data
Given a number, returns a [Pandas](https://pandas.pydata.org/docs/) dataframe of the market data. It attempts to grab the last 90 days, but can be changed to 24h,7d, or 30d as well.

`df = data(6598)
print(df.head())`

![alt text](https://github.com/tuttlepower/predictit_markets/blob/master/images/output_example.PNG "Output Example")

#market_name
`print(market_name(6598))`

