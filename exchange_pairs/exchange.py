import ccxt
import json

exchanges = [
    'alpaca', 'ascendex', 'bequant', 'binance', 'binancecoinm', 'binanceus', 
    'binanceusdm', 'bingx', 'bitcoincom', 'bitfinex', 'bitfinex2', 'bitget', 
    'bithumb', 'bitmart', 'bitmex', 'bitopro', 'bitpanda', 'bitrue', 'bitstamp', 
    'bitvavo', 'blockchaincom', 'bybit', 'cex', 'coinbase', 'coinbaseexchange', 
    'coinbaseinternational', 'coincheck', 'coinex', 'coinone', 'cryptocom', 
    'currencycom', 'deribit', 'exmo', 'gate', 'gateio', 'gemini', 'hitbtc', 
    'hollaex', 'htx', 'huobi', 'huobijp', 'hyperliquid', 'idex', 
    'independentreserve', 'kraken', 'krakenfutures', 'kucoin', 'kucoinfutures', 
    'lbank', 'luno', 'mexc', 'ndax', 'okcoin', 'okx', 'onetrading', 'oxfun', 
    'p2b', 'phemex', 'poloniex', 'poloniexfutures', 'probit', 'upbit', 'vertex', 
    'wazirx', 'whitebit', 'woo', 'woofipro'
]

def fetch_pairs(exchange_id):
    try:
        exchange = getattr(ccxt, exchange_id)()
        markets = exchange.load_markets()
        pairs = [{"base": market.split('/')[0], "quote": market.split('/')[1]} for market in markets]
        return {exchange_id: pairs}
    except Exception as e:
        print(f"Failed to fetch data for {exchange_id}: {e}")
        return {exchange_id: []}

def main():
    all_pairs = {}
    for exchange_id in exchanges:
        pairs = fetch_pairs(exchange_id)
        all_pairs.update(pairs)

    # Save to JSON file
    with open('exchange_pairs.json', 'w') as json_file:
        json.dump(all_pairs, json_file, indent=4)

    print("Exchange pairs data saved to exchange_pairs.json")

if __name__ == "__main__":
    main()

