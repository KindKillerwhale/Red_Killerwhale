import unittest
import asyncio
from core.exchange_utils import ExchangeManager

class TestExchangeUtils(unittest.TestCase):
    def setUp(self):
        self.exchange_manager = ExchangeManager()

    def test_fetch_ticker(self):
        result = asyncio.run(self.exchange_manager.watch_ticker('binance', 'BTC/USDT'))
        self.assertIsNotNone(result)

    def test_fetch_all_tickers(self):
        result = asyncio.run(self.exchange_manager.fetch_all_tickers())
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
