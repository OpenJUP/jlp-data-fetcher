import asyncio
import time
from solana.rpc.async_api import AsyncClient
from jlp.accounts import Pool, Custody
from solders.pubkey import Pubkey
from solana.rpc.commitment import Processed

# Constants
USD_DECIMALS = 6
JLP_TOKEN = '27G8MtK7VtTcCHkpASjSDdkWWYfoqT6ggEuKidVJidD4'
RPC_ENDPOINT = "https://api.mainnet-beta.solana.com"

async def fetch_jlp_pool_info():
    """Fetch and print pool and custody data without database interaction."""
    sol_client = AsyncClient(RPC_ENDPOINT)

    try:
        # Fetch supply of JLP token
        supply_response = await sol_client.get_token_supply(Pubkey.from_string(JLP_TOKEN))
        supply = float(supply_response.value.ui_amount)

        # Fetch pool info
        pool_pubkey = Pubkey.from_string('5BUwFW4nRbftYTDMbgxykoFWqWHPzahFSNAaaaJtVKsq')
        pool = await Pool.fetch(sol_client, pool_pubkey)

        ts = time.time_ns()
        pool_aum = float(pool.aum_usd / 10 ** USD_DECIMALS)
        pool_limit_usd = float(pool.limit.max_aum_usd / 10 ** USD_DECIMALS)
        pool_apr_bps = float(pool.pool_apr.fee_apr_bps)
        pool_realized_fee = float(pool.pool_apr.realized_fee_usd / 10 ** USD_DECIMALS)
        theo_price = pool_aum / supply

        # Print Pool Info
        print("\n=== Pool Info ===")
        print(f"Timestamp: {ts}")
        print(f"Pool AUM (USD): {pool_aum}")
        print(f"Supply: {supply}")
        print(f"Pool Limit (USD): {pool_limit_usd}")
        print(f"Pool APR (bps): {pool_apr_bps}")
        print(f"Pool Realized Fee (USD): {pool_realized_fee}")
        print(f"Theoretical Price: {theo_price}")

        # Fetch custody data
        custodies = [
            ('SOL', Pubkey.from_string('7xS2gz2bTp3fwCC7knJvUWTEU9Tycczu6VhJYKgi1wdz')),
            ('BTC', Pubkey.from_string('5Pv3gM9JrFFH883SWAhvJC9RPYmo8UNxuFtv5bMMALkm')),
            ('ETH', Pubkey.from_string('AQCGyheWPLeo6Qp9WpYS9m3Qj479t7R636N9ey1rEjEn')),
            ('USDC', Pubkey.from_string('G18jKKXQwBbrHeiK3C9MRXhkHsLHf7XgCSisykV46EZa')),
            ('USDT', Pubkey.from_string('4vkNeXiYEUizLdrpdPS1eC2mccyM4NUPRtERrk6ZETkk'))
        ]
        custody_pubkeys = [pubkey for _, pubkey in custodies]
        custodies_resp = await Custody.fetch_multiple(sol_client, custody_pubkeys, commitment=Processed)

        # Print Custody Data
        print("\n=== Custody Data ===")
        for custody, (symbol, _) in zip(custodies_resp, custodies):
            decimals = custody.decimals
            print(f"\nToken: {symbol}")
            print(f"Target Ratio (bps): {int(custody.target_ratio_bps)}")
            print(f"Max Global Long Sizes: {int(custody.pricing.max_global_long_sizes / 10 ** 6)}")
            print(f"Max Global Short Sizes: {int(custody.pricing.max_global_short_sizes / 10 ** 6)}")
            print(f"Fees Reserves: {float(custody.assets.fees_reserves / 10 ** decimals)}")
            print(f"Owned: {float(custody.assets.owned / 10 ** decimals)}")
            print(f"Locked: {float(custody.assets.locked / 10 ** decimals)}")
            print(f"Guaranteed USD: {float(custody.assets.guaranteed_usd / 10 ** 6)}")
            print(f"Global Short Sizes: {float(custody.assets.global_short_sizes / 10 ** 6)}")
            print(f"Global Short Average Prices: {float(custody.assets.global_short_average_prices / 10 ** 6)}")
            print("-" * 30)

    except Exception as ex:
        print(f"Error fetching data: {ex}")
    finally:
        await sol_client.close()

# Run the function
if __name__ == "__main__":
    asyncio.run(fetch_jlp_pool_info())
