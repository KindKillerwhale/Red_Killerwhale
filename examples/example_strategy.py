import asyncio
import logging
from core.exchange_utils import ExchangeManager
from bot_implementation.telegram_bot import TelegramBot

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def example_strategy():
    bot = TelegramBot('YOUR_TELEGRAM_BOT_TOKEN', 'YOUR_CHAT_ID')
    await bot.send_message("Starting example strategy")
    logging.info("Starting example strategy")

    exchange_manager = ExchangeManager(['binance', 'kraken'])
    await exchange_manager.fetch_all_tickers()
    await bot.send_message("Fetching real-time market data from exchanges")
    logging.info("Fetching real-time market data from exchanges")

    await exchange_manager.close_exchanges()

# Run the example strategy
asyncio.run(example_strategy())
