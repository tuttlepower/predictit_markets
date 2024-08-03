# predictit_markets

`pip install predictit-markets`

Simple Python package that helps to retrieve predictit market data. 

# market_data
Given a number, returns a [Pandas](https://pandas.pydata.org/docs/) dataframe of the market data. It attempts to grab the last 90 days, but can be changed to '24h',7, or 30 as well. Constructor defaults to 90, but can take the other dates as an argument. Important to note that the '24h' is a string whereas the other arguements are integers.
Can also take an integer for the max number of contracts, so if you only want to see the top 2, ie Democrat and Repblican, versus the entire field. 

`df = market_data(6598)`

`print(df.head())`

![Output image](https://raw.githubusercontent.com/tuttlepower/predictit_markets/master/predictit_markets/images/output_example.PNG")

# market_name

`print(market_name(6598))`

Returns the name of the market as a string. 

`Which party will win Washington in the 2020 presidential election?`

That's all there is to it. Predictit's API is in XML format, which I thought was a pain, and they have download buttons for every market. I found [this](https://gist.github.com/kiernann/bf5ba187a5070ecb6cfe34db76860c45) and it helped me understand the urls that are used to download the market CSV's so I recreated it for Python. I didn't see anything else like this posted, and I figured it may help someone else down the line. ~~Was considering putting this as a package, but it doesn't seem like it would be worth it.~~

[Is now a python package](https://pypi.org/project/predictit-markets/#description)

- Thinking of adding the ability to get the data raw, but I think df's are fine for now. 
- Thinking of adding charts, but may just throw a notebook up with examples.