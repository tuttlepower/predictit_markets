# predictit_markets.py

import pandas as pd
import requests

def market_data(market, time=90, maxContracts=6):
    """
    Fetch market data from PredictIt's API and return as a DataFrame.

    Parameters:
    - market (int): The market ID to fetch data for.
    - time: The timespan for which data is fetched. Options: '24h', 7, 30, 90 (in days).
    - maxContracts (int): The maximum number of contracts to fetch.

    Returns:
    - pd.DataFrame: DataFrame containing the market data or None if an error occurred.
    """
    url = f'https://www.predictit.org/api/Public/GetMarketChartData/{market}'
    params = {
        'timespan': time,
        'maxContracts': maxContracts,
        'isTimespanInHours': 'false'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        data = response.json()
        df = pd.DataFrame(data)
        return df

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except ValueError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None

def market_name(market):
    # this may not be the best way to do it, but it worked pretty well for me 
    df = pd.read_json('https://www.predictit.org/api/marketdata/markets/'+str(market))
    # sets the market to a string and returns it. 
    text = str(df['name'][0])
    return text
