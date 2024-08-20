# Red_Killerwhale

Red_Killerwhale is a cryptocurrency trading bot that leverages market data to find arbitrage opportunities and make profitable trades. It integrates with multiple exchanges and provides real-time updates via a Telegram bot.

## Features

- **Arbitrage Strategies:** Identify profitable trading opportunities across multiple exchanges.
- **Exchange Integration:** Fetch market data from various exchanges using `ccxt.pro`.
- **Risk Management:** Implement stop-loss and take-profit strategies.
- **Telegram Integration:** Receive real-time updates on trading activities.

## Setup

### Prerequisites

- Python 3.8+
- `ccxt.pro`
- `networkx`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KindKillerwhale/Red_Killerwhale.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Red_Killerwhale
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Configure your Telegram bot token and chat ID:

    Edit the `bot_implementation/trading_bot.py` file and update the following variables:

    ```python
    token = 'YOUR_TELEGRAM_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    ```

2. Run the trading bot:

    ```bash
    python3 -m bot_implementation.trading_bot
    ```

### Testing

Run the tests using `unittest`:

```bash
python3 -m unittest discover tests
