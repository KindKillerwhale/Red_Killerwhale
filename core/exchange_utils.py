import ccxt.pro as ccxtpro
import asyncio
import logging
import json
from config.config import Config

logging.basicConfig(level=logging.INFO, filename='trading_bot.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

class ExchangeManager:
    def __init__(self):
        self.exchanges = {name: getattr(ccxtpro, name)() for name in Config.EXCHANGE_NAMES}
        self.currency_pairs = self.load_currency_pairs()

    def load_currency_pairs(self):
        with open('./exchange_pairs/currency_pairs.json', 'r') as file:
            return json.load(file)

    async def filter_supported_exchanges(self):
        valid_exchanges = {}
        for name, exchange in self.exchanges.items():
            try:
                if exchange.has['watchTicker'] and not exchange.apiKey:
                    await exchange.load_markets()
                    valid_exchanges[name] = exchange
            except AttributeError as e:
                logging.error(f"AttributeError loading markets for {name}: {e}")
            except Exception as e:
                logging.error(f"Error loading markets for {name}: {e}")
        return valid_exchanges

    async def validate_symbol(self, exchange, symbol):
        return symbol in exchange.symbols

    async def watch_ticker(self, exchange_name, symbol):
        exchange = self.valid_exchanges[exchange_name]
        if not await self.validate_symbol(exchange, symbol):
            logging.error(f"Exchange {exchange_name} does not support symbol {symbol}")
            return

        while True:
            try:
                ticker = await exchange.watch_ticker(symbol)
                logging.info(f"{exchange_name} {symbol}: {ticker}")
            except Exception as e:
                logging.error(f"Error watching ticker for {exchange_name}: {e}")


    async def fetch_all_tickers(self):
        self.valid_exchanges = await self.filter_supported_exchanges()
        if not self.valid_exchanges:
            logging.error("No valid exchanges found. Exiting...")
            return

        tasks = []
        for symbol, exchanges in self.currency_pairs.items():
            for exchange_name in exchanges:
                if exchange_name in self.valid_exchanges:
                    tasks.append(self.watch_ticker(exchange_name, symbol))
        if not tasks:
            logging.error("No tasks to watch tickers. Exiting...")
            return
        await asyncio.gather(*tasks)

    async def close_exchanges(self):
        for exchange in self.valid_exchanges.values():
            try:
                await exchange.close()
            except Exception as e:
                logging.error(f"Error closing exchange: {e}")