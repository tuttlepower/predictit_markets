# test_integration_predictit_markets.py

import unittest
from predictit_markets import predictit_markets

class TestPredictItMarketsIntegration(unittest.TestCase):

    def test_real_api_call(self):
        # This test will hit the real API
        df = predictit_markets.market_data(8089)
        self.assertTrue(len(df) > 0)

if __name__ == '__main__':
    unittest.main()
