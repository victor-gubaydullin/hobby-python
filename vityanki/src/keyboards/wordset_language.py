from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def wordset_language_keyboard():
    '''TODO: Should think about whether to use a predefined set of languages or allow users to add their own.
    A predifined set of languages is easier to implement, but a user-defined set of languages is more flexible.
    A predifined set of languages makes it easier to add voice acting via Amazon Polly or other services.'''
    language_buttons = [
            InlineKeyboardButton(text="🇬🇧 EN", callback_data="wordset_language_en"),
            InlineKeyboardButton(text="🇩🇪 DE", callback_data="wordset_language_de"),
            InlineKeyboardButton(text="🇷🇺 RU", callback_data="wordset_language_ru"),
            InlineKeyboardButton(text="🇫🇷 FR", callback_data="wordset_language_fr"),
            InlineKeyboardButton(text="🇪🇸 ES", callback_data="wordset_language_es"),
            InlineKeyboardButton(text="🇨🇳 CN", callback_data="wordset_language_cn"),
            InlineKeyboardButton(text="🇯🇵 JP", callback_data="wordset_language_jp"),
            InlineKeyboardButton(text="🇮🇳 HI", callback_data="wordset_language_hi"),
            InlineKeyboardButton(text="🇰🇷 KO", callback_data="wordset_language_ko"),
            InlineKeyboardButton(text="🇵🇹 PT", callback_data="wordset_language_pt"),
            InlineKeyboardButton(text="🇮🇹 IT", callback_data="wordset_language_it"),
            InlineKeyboardButton(text="🇳🇱 NL", callback_data="wordset_language_nl"),
            InlineKeyboardButton(text="🇸🇪 SV", callback_data="wordset_language_sv"),
            InlineKeyboardButton(text="🇳🇴 NO", callback_data="wordset_language_no"),
            InlineKeyboardButton(text="🇩🇰 DA", callback_data="wordset_language_da"),
            InlineKeyboardButton(text="🇫🇮 FI", callback_data="wordset_language_fi"),
            InlineKeyboardButton(text="🇷🇴 RO", callback_data="wordset_language_ro"),
            InlineKeyboardButton(text="🇵🇱 PL", callback_data="wordset_language_pl"),
            InlineKeyboardButton(text="🇨🇿 CS", callback_data="wordset_language_cs"),
            InlineKeyboardButton(text="🇭🇺 HU", callback_data="wordset_language_hu"),
            InlineKeyboardButton(text="🇧🇬 BG", callback_data="wordset_language_bg"),
            InlineKeyboardButton(text="🇷🇸 SR", callback_data="wordset_language_sr"),
            InlineKeyboardButton(text="🇺🇦 UA", callback_data="wordset_language_ua"),
            InlineKeyboardButton(text="🇭🇷 HR", callback_data="wordset_language_hr"),
            InlineKeyboardButton(text="🇸🇰 SK", callback_data="wordset_language_sk"),
            InlineKeyboardButton(text="🇸🇮 SL", callback_data="wordset_language_sl"),
            InlineKeyboardButton(text="🇲🇰 MK", callback_data="wordset_language_mk"),
            InlineKeyboardButton(text="🇲🇹 MT", callback_data="wordset_language_mt"),
            InlineKeyboardButton(text="🇱🇻 LV", callback_data="wordset_language_lv"),
            InlineKeyboardButton(text="🇱🇹 LT", callback_data="wordset_language_lt"),
            InlineKeyboardButton(text="🇪🇪 ET", callback_data="wordset_language_et"),
            InlineKeyboardButton(text="🌐 AR", callback_data="wordset_language_ar"),
            InlineKeyboardButton(text="🇹🇷 TR", callback_data="wordset_language_tr"),
            InlineKeyboardButton(text="🇮🇩 ID", callback_data="wordset_language_id"),
            InlineKeyboardButton(text="🇵🇭 TL", callback_data="wordset_language_tl"),
            InlineKeyboardButton(text="🇻🇳 VI", callback_data="wordset_language_vi"),
            InlineKeyboardButton(text="🇹🇭 TH", callback_data="wordset_language_th"),
            InlineKeyboardButton(text="🇲🇾 MS", callback_data="wordset_language_ms"),
    ]
    # Arrange buttons in rows of 4
    # This will create a grid layout with 4 buttons per row
    return InlineKeyboardMarkup(
        inline_keyboard=[language_buttons[i:i + 4] for i in range(0, len(language_buttons), 4)]
    )
