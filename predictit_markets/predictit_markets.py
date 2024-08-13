# predictit_markets.py

import pandas as pd
import requests


def market_data(market, time=90, max_contracts=6):
    """
    Fetch market data from PredictIt's API and return as a DataFrame.

    Parameters:
    - market (int): The market ID to fetch data for.
    - time: The timespan for which data is fetched. Options: '24h', 7, 30, 90 (in days).
    - maxContracts (int): The maximum number of contracts to fetch.

    Returns:
    - pd.DataFrame: DataFrame containing the market data or None if an error occurred.
    """
    url = f"https://www.predictit.org/api/Public/GetMarketChartData/{market}"
    params = {
        "timespan": time,
        "maxContracts": max_contracts,
        "isTimespanInHours": "false",
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
    # this may not be the best way to do it, but it worked pretty well for me.

    df = pd.read_json("https://www.predictit.org/api/marketdata/markets/" + str(market))
    # sets the market to a string and returns it.

    text = str(df["name"][0])
    return text


def all_markets():
    """
    Fetch all available markets from the PredictIt API and return the data as a DataFrame.

    This function sends a GET request to the PredictIt API endpoint to retrieve all market data.
    The returned data includes market IDs and names, which are then structured into a pandas
    DataFrame with two columns: 'Market ID' and 'Market Name'.

    Returns:
    --------
    pd.DataFrame
        A DataFrame containing market IDs and their corresponding names.

    Raises:
    -------
    Exception
        If the API request fails, an exception is raised with the HTTP status code.

    Examples:
    ---------
    df = all_markets()
    print(df.head())
       Market ID                         Market Name
    0       123                   Which party wins?
    1       456  Who will be the next president?
    """
    url = "https://www.predictit.org/api/marketdata/all"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        markets = data["markets"]
        market_names = [(market["id"], market["name"]) for market in markets]
        df = pd.DataFrame(market_names, columns=["Market ID", "Market Name"])
        return df
    else:
        raise Exception(
            f"Failed to retrieve data. HTTP Status Code: {response.status_code}"
        )
