import json

with open('./exchange_pairs.json', 'r') as file:
    data = json.load(file)

currency_pairs = {}

for exchange, pairs in data.items():
    for pair in pairs:
        base_quote = f"{pair['base']}/{pair['quote']}"
        if base_quote not in currency_pairs:
            currency_pairs[base_quote] = []
        currency_pairs[base_quote].append(exchange)

with open('./currency_pairs.json', 'w') as outfile:
    json.dump(currency_pairs, outfile, indent=4)

currency_pairs

