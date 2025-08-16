from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from locales.translation import t

def donate_keyboard(language_code: str) -> InlineKeyboardMarkup:
    donate_options_buttons = [
        InlineKeyboardButton(text=t(language_code, "donate.cryptobot.button_label"), callback_data="cryptobot"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.button_label"), callback_data="crypto_wallets"),
    ]
    top_donators_button = [
        InlineKeyboardButton(text=t(language_code, "donate.top_donators.button_label"), callback_data="top_donators"),
    ]
    control_buttons = [
        InlineKeyboardButton(text=t(language_code, "donate.back_to_main_menu"), callback_data="main_menu"),
    ]

    all_buttons = [donate_options_buttons] + [top_donators_button] + [control_buttons]
    return InlineKeyboardMarkup(inline_keyboard=all_buttons)

def donate_crypto_wallets_keyboard(language_code) -> InlineKeyboardMarkup:
    crypto_wallets_buttons = [
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.BTC.button_label"), callback_data="BTC"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.ETH.button_label"), callback_data="ETH"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.USDT.button_label"), callback_data="USDT"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.USDC.button_label"), callback_data="USDC"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.TON.button_label"), callback_data="TON"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.BNB.button_label"), callback_data="BNB"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.TRX.button_label"), callback_data="TRX"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.SOL.button_label"), callback_data="SOL"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.XRP.button_label"), callback_data="XRP"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.LTC.button_label"), callback_data="LTC"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.DOGE.button_label"), callback_data="DOGE"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.ADA.button_label"), callback_data="ADA"),
        # InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets.MATIC.button_label"), callback_data="MATIC"),
    ]
    control_buttons = [
            InlineKeyboardButton(text=t(language_code, "donate.back_to_main_menu"), callback_data="main_menu"),
            #InlineKeyboardButton(text=t(language_code, "donate.previous_crypto_list"), callback_data="previous_crypto_list"),
            #InlineKeyboardButton(text=t(language_code, "donate.next_crypto_list"), callback_data="next_crypto_list"),
            InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.button_label"), callback_data="crypto_blockchain"),
    ]
    all_buttons = [crypto_wallets_buttons[i:i+2] for i in range(0, len(crypto_wallets_buttons), 2)] + [control_buttons]

    return InlineKeyboardMarkup(inline_keyboard=all_buttons)


def donate_crypto_blockchain_keyboard(language_code) -> InlineKeyboardMarkup:
    blockchain_buttons = [
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.Ethereum_ERC20.button_label"), callback_data="Ethereum_ERC20"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.BSC_BEP20.button_label"), callback_data="BSC_BEP20"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.Polygon_ERC20.button_label"), callback_data="Polygon_ERC20"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.Arbitrum_ERC20.button_label"), callback_data="Arbitrum_ERC20"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.Optimism_ERC20.button_label"), callback_data="Optimism_ERC20"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.Base_ERC20.button_label"), callback_data="Base_ERC20"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.Avalanche_CChain_ERC20.button_label"), callback_data="Avalanche_CChain_ERC20"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.TRON_TRC20.button_label"), callback_data="TRON_TRC20"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.Solana_SPL.button_label"), callback_data="Solana_SPL"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.XRP_Ledger.button_label"), callback_data="XRP_Ledger"),
    ]
    control_buttons = [
            InlineKeyboardButton(text=t(language_code, "donate.back_to_main_menu"), callback_data="main_menu"),
            InlineKeyboardButton(text=t(language_code, "donate.crypto_blockchain.back_to_wallets"), callback_data="crypto_wallets"),
    ]
    all_buttons = [blockchain_buttons[i:i+2] for i in range(0, len(blockchain_buttons), 2)] + [control_buttons]

    return InlineKeyboardMarkup(inline_keyboard=all_buttons)