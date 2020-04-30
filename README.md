# predictit_markets
Simple Python code that helps to retreive predictit market data. 

#data
Given a number, returns a [Pandas](https://pandas.pydata.org/docs/) dataframe of the market data. It attempts to grab the last 90 days, but can be changed to 24h,7d, or 30d as well.

`df = data(6598)
print(df.head())`


  `ContractName                   Date OpenSharePrice HighSharePrice LowSharePrice CloseSharePrice  TradeVolume
0   Republican  3/31/2020 12:00:00 AM          $0.02          $0.02         $0.02           $0.02            1
1   Democratic  3/31/2020 12:00:00 AM          $0.99          $0.99         $0.99           $0.99            1
2   Republican   4/1/2020 12:00:00 AM          $0.02          $0.04         $0.02           $0.04            2
3   Democratic   4/1/2020 12:00:00 AM          $0.99          $0.99         $0.95           $0.95            2
4   Republican   4/2/2020 12:00:00 AM          $0.04          $0.04         $0.04           $0.04`


#market_name