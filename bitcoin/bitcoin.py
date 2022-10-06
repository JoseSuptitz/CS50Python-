import requests, sys, json

if len(sys.argv) == 2:
    try:
        converted = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')
else:
    sys.exit('Missing command-line argument')

try:
    bitcoin = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    sys.exit()

test = bitcoin.json()

bitcoin_usd = test["bpi"]["USD"]["rate_float"] * converted

print(f'${bitcoin_usd:,.4f}')