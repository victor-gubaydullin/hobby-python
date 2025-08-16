import aiohttp

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

async def fetch_usd_value(crypto_name, amount_raw):
    params = {
        "ids": crypto_name.lower(),
        "vs_currencies": "usd"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(COINGECKO_URL, params=params) as response:
            data = await response.json()
            price = data.get(crypto_name.lower(), {}).get("usd", 0)
            return price * amount_raw