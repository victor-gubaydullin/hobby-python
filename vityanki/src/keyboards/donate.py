from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from locales.translation import t

def donate_keyboard(language_code: str) -> InlineKeyboardMarkup:
    donate_options_buttons = [
        InlineKeyboardButton(text=t(language_code, "donate.cryptobot"), callback_data="cryptobot"),
        InlineKeyboardButton(text=t(language_code, "donate.crypto_wallets"), callback_data="crypto_wallets"),
    ]
    top_donators_button = [
        InlineKeyboardButton(text=t(language_code, "donate.top_donators"), callback_data="top_donators"),
    ]
    control_buttons = [
        InlineKeyboardButton(text=t(language_code, "donate.back_to_main_menu"), callback_data="main_menu"),
    ]

    all_buttons = [donate_options_buttons] + [top_donators_button] + [control_buttons]
    return InlineKeyboardMarkup(inline_keyboard=all_buttons)


'''
Option with each cryptocurrency walles as a separate button.
This can be useful for direct transfers to specific wallets, but for now we will use a single button
that will return a list of all available wallets.
def donate_keyboard(language_code) -> InlineKeyboardMarkup:
    cryptobot_button = [
        InlineKeyboardButton(text=t(language_code, "donate.cryptobot"), callback_data="cryptobot"),
    ]
    crypto_wallets_button = [
        InlineKeyboardButton(text=t(language_code, "donate.BTC"), callback_data="BTC"),
        InlineKeyboardButton(text=t(language_code, "donate.ETH"), callback_data="ETH"),
        InlineKeyboardButton(text=t(language_code, "donate.USDC"), callback_data="USDC"),
        InlineKeyboardButton(text=t(language_code, "donate.USDT"), callback_data="USDT"),
        InlineKeyboardButton(text=t(language_code, "donate.EURC"), callback_data="EURC"),
        InlineKeyboardButton(text=t(language_code, "donate.EURI"), callback_data="EURI"),
        InlineKeyboardButton(text=t(language_code, "donate.XRP"), callback_data="XRP"),
        InlineKeyboardButton(text=t(language_code, "donate.TRX"), callback_data="TRX"),
        InlineKeyboardButton(text=t(language_code, "donate.BNB"), callback_data="BNB"),
        InlineKeyboardButton(text=t(language_code, "donate.SOL"), callback_data="SOL"),
        InlineKeyboardButton(text=t(language_code, "donate.TON"), callback_data="TON"),
        InlineKeyboardButton(text=t(language_code, "donate.DOGE"), callback_data="DOGE"),
        InlineKeyboardButton(text=t(language_code, "donate.LTC"), callback_data="LTC"),
        InlineKeyboardButton(text=t(language_code, "donate.DAI"), callback_data="DAI"),
        InlineKeyboardButton(text=t(language_code, "donate.ADA"), callback_data="ADA"),
        InlineKeyboardButton(text=t(language_code, "donate.DOT"), callback_data="DOT"),
    ]
    control_buttons = [
            InlineKeyboardButton(text=t(language_code, "donate.back_to_main_menu"), callback_data="main_menu"),
            InlineKeyboardButton(text=t(language_code, "donate.previous_crypto_list"), callback_data="previous_crypto_list"),
            InlineKeyboardButton(text=t(language_code, "donate.next_crypto_list"), callback_data="next_crypto_list"),
    ]
    all_buttons = [cryptobot_button] + [crypto_wallets_button[i:i+2] for i in range(0, len(crypto_wallets_button), 2)] + [control_buttons]

    return InlineKeyboardMarkup(inline_keyboard=[all_buttons])
'''