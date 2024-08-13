# tests/test_predictit_markets.py

import unittest
from unittest.mock import patch, Mock
import requests
import pandas as pd
from predictit_markets.predictit_markets import all_markets, market_data


class TestPredictItMarkets(unittest.TestCase):

    @patch("predictit_markets.predictit_markets.requests.get")
    def test_market_data_success(self, mock_get):
        # Simulate a successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "marketId": 8089,
                "contractId": 31414,
                "contractName": "Shapiro",
                "date": "2024-07-26T00:00:00",
                "dateString": "2024-07-26",
                "openSharePrice": 0.26,
                "highSharePrice": 0.34,
                "lowSharePrice": 0.25,
                "closeSharePrice": 0.31,
                "tradeVolume": 160257,
                "lineColor": "#0D8ECF",
            }
            # Add more sample data here if needed
        ]
        mock_get.return_value = mock_response

        # Test the market_data function
        df = market_data(8089)

        # Assert the DataFrame is not None and contains the expected data
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["contractName"], "Shapiro")

    @patch("predictit_markets.predictit_markets.requests.get")
    def test_market_data_http_error(self, mock_get):
        # Simulate an HTTP error response
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404 Client Error: Not Found"
        )
        mock_get.return_value = mock_response

        # Test the market_data function
        df = market_data(9999)  # Assuming 9999 is a non-existent market ID

        # Assert the DataFrame is None due to the error
        self.assertIsNone(df)

    @patch("predictit_markets.predictit_markets.requests.get")
    def test_market_data_request_exception(self, mock_get):
        # Simulate a request exception
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        # Test the market_data function
        df = market_data(8089)

        # Assert the DataFrame is None due to the exception
        self.assertIsNone(df)

    @patch("predictit_markets.predictit_markets.requests.get")
    def test_market_data_json_error(self, mock_get):
        # Simulate a JSON decoding error
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("No JSON object could be decoded")
        mock_get.return_value = mock_response

        # Test the market_data function
        df = market_data(8089)

        # Assert the DataFrame is None due to JSON error
        self.assertIsNone(df)

    @patch("predictit_markets.requests.get")
    def test_all_markets_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "markets": [
                {"id": 123, "name": "Market 1"},
                {"id": 456, "name": "Market 2"},
            ]
        }

        df = all_markets()

        expected_df = pd.DataFrame(
            [
                {"Market ID": 123, "Market Name": "Market 1"},
                {"Market ID": 456, "Market Name": "Market 2"},
            ]
        )

        pd.testing.assert_frame_equal(df, expected_df)


if __name__ == "__main__":
    unittest.main()
