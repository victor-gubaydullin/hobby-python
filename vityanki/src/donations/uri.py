from urllib.parse import urlencode

def btc_uri(address: str, amount_btc: float, label: str | None = None, message: str | None = None) -> str:
    q = {"amount": f"{amount_btc:.8f}"}
    if label:   q["label"]   = label
    if message: q["message"] = message
    return f"bitcoin:{address}?{urlencode(q)}"

def eth_uri(address: str, amount_eth: float) -> str:
    wei = int(round(amount_eth * 10**18))
    return f"ethereum:{address}?value={wei}"

def erc20_uri(contract: str, recipient: str, amount_tokens: float, decimals: int) -> str:
    amt = int(round(amount_tokens * (10 ** decimals)))
    return f"ethereum:{contract}/transfer?address={recipient}&uint256={amt}"

def tron_uri(address: str, amount_tokens: float | None = None) -> str:
    return f"tron:{address}" + (f"?amount={amount_tokens}" if amount_tokens is not None else "")

def ton_uri(address: str, amount_ton: float | None = None, text: str | None = None) -> str:
    base = f"ton://transfer/{address}"
    q = {}
    if amount_ton is not None: q["amount"] = str(int(round(amount_ton * 10**9)))
    if text:                   q["text"]   = text
    return base if not q else f"{base}?{urlencode(q)}"

def sol_uri(address: str, amount_sol: float | None = None, spl_token: str | None = None) -> str:
    q = {}
    if amount_sol is not None: q["amount"] = f"{amount_sol:.9f}"
    if spl_token:              q["spl-token"] = spl_token
    qs = f"?{urlencode(q)}" if q else ""
    return f"solana:{address}{qs}"
