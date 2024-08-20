import asyncio
import logging
from core.exchange_utils import ExchangeManager
from core.periodic_graph_analysis import PeriodicGraphAnalyzer
from core.risk_management import RiskManager
from bot_implementation.telegram_bot import TelegramBot
from config.config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingBot:
    def __init__(self, telegram_token, chat_id):
        self.telegram_bot = TelegramBot(telegram_token, chat_id)
        self.exchange_manager = ExchangeManager()
        self.graph_analyzer = PeriodicGraphAnalyzer()
        self.risk_manager = RiskManager()

    async def run(self):
        logging.info("Trading bot started")
        await self.telegram_bot.send_message("Trading bot started")
        
        try:
            market_data = await self.exchange_manager.fetch_all_tickers()
            await self.telegram_bot.send_message("Fetched market data from exchanges")

            graph = self.graph_analyzer.build_graph(market_data)
            profitable_opportunities = self.graph_analyzer.find_profitable_opportunities(graph)
            
            if profitable_opportunities:
                for opportunity in profitable_opportunities:
                    cycle, profit = opportunity
                    message = f"Profitable opportunity found: Cycle - {cycle}, Profit - {profit}"
                    await self.telegram_bot.send_message(message)
            else:
                await self.telegram_bot.send_message("No profitable opportunities found")
        except Exception as e:
            logging.error(f"Error in trading bot run: {e}")
        finally:
            await self.exchange_manager.close_exchanges()
            logging.info("Trading bot stopped")

if __name__ == "__main__":
    token = Config.TELEGRAM['token']
    chat_id = Config.TELEGRAM['chat_id']
    bot = TradingBot(token, chat_id)
    asyncio.run(bot.run())
