# df creator using predictits csv downloads that are available
import pandas as pd 

def data(market):
    #24h,7d,30d, 90d,
    time = '90d'
    url = 'https://www.predictit.org/Resource/DownloadMarketChartData?marketid='+str(market)+'&timespan='+str(time)
    df = pd.read_csv(url)
    return df
    
def market_name(market):
    # this may not be the best way to do it, but it worked pretty well for me 
    df = pd.read_json('https://www.predictit.org/api/marketdata/markets/'+str(market))
    # sets the market to a string and returns it. 
    text = str(df['name'][0])
    return text
