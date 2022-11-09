from typing import List, Any, Iterable
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# Buttons
CBB_ALL = 'all'
CBB_PESTELYA = 'pestelya'
CBB_NEVSKY = 'nevsky'

CBB_CHECK_IN_TIME = 'check_in_time'
CBB_EARLY_LATE_CHECK = 'early_check'
CBB_IN_YARD_PARKING = 'in_yard_parking'
CBB_NEAREST_PARKING = 'nearest_parking'
CBB_SETTLEMENT = 'settlement'
CBB_PAYMENT_BY_CARD = 'payment_by_card'
CBB_PREPAYMENT = 'prepayment'
CBB_PAYMENT_MADE = 'payment_made'
CBB_BOOKING_CANCEL = 'booking_cancel'
CBB_SHOPS = 'shops'
CBB_TOWEL = 'towel'
CBB_GET_TO = 'get_to'
CBB_EAT = 'eat'
CBB_WHAT_PROVIDE = 'what_provide'

CBB_CHECK_IN = 'check_in'
CBB_PAYMENT = 'payment'
CBB_OTHER = 'other'
CBB_HOSTELS = 'hostels'

CBB_CAPTIONS = {
    CBB_PESTELYA: 'Пестеля',
    CBB_NEVSKY: 'Невский',

    CBB_CHECK_IN_TIME: 'Время заезда/ выезда.',
    CBB_EARLY_LATE_CHECK: 'Стоимость раннего заезда/позднего выезда.',
    CBB_IN_YARD_PARKING: 'Можно ли припарковать машину во дворе?',
    CBB_NEAREST_PARKING: 'Есть ли поблизости парковки?',
    CBB_SETTLEMENT: 'Как происходит процесс заселения?',
    CBB_PAYMENT_BY_CARD: 'Возможна ли оплата кредитной картой?',
    CBB_PREPAYMENT: 'Бронь напрямую. Предоплата.',
    CBB_PAYMENT_MADE: 'Каким образом происходит оплата?',
    CBB_BOOKING_CANCEL: 'Если я захочу отменить бронирование...',
    CBB_SHOPS: 'Есть ли рядом магазины?',
    CBB_TOWEL: 'Белье и полотенца.',
    CBB_GET_TO: 'Как доехать?',
    CBB_EAT: 'Где перекусить быстро/не дорого?',
    CBB_WHAT_PROVIDE:
        'Предоставляете ли тапочки, шапочки для душа, '
        'косметические средства?',

    CBB_CHECK_IN: 'Заезд...',
    CBB_PAYMENT: 'Оплата...',
    CBB_OTHER: 'Другое...',
    CBB_HOSTELS: 'Отель...',
}

HOSTELS = (
    CBB_NEVSKY,
    CBB_PESTELYA,
)

MESSAGES = {
    CBB_GET_TO: {
        CBB_PESTELYA:
            '*Аэропорт Пулково:*\n'
            'автобус 39 - ст.м. Московская - ст.м. Гостиный двор '
            '- пешком до ул. Пестеля 5,\n'
            'или "Яндекс такси" 650-850 руб.\n'
            '*Московский вокзал:*\n'
            'общ. транспорт по Невскому пр., до ст. Гостиный двор. '
            'Далее пешком 15 минут,\n'
            'или "Яндекс такси" 180-280 руб.',
        CBB_NEVSKY:
            '*Аэропорт Пулково:*\n'
            'автобус 39 - ст.м. Московская - ст.м. Пл. Восстания '
            '- пешком до Невский пр. 128 (5 минут).\n'
            'или "Яндекс такси" 650-850 руб.\n'
            '*Московский вокзал:*\n'
            'Пешком 5 минут до Невского пр., 128.',
    },
    CBB_CHECK_IN_TIME: {
        CBB_ALL: 'Заезд в любое время после 14.00, выезд до 11.00.',
    },
    CBB_EARLY_LATE_CHECK: {
        CBB_ALL:
            'Стоимость раннего заезда или позднего выезда '
            'составляет 70% от стоимости дня.',
    },
    CBB_SETTLEMENT: {
        CBB_ALL:
            'Заселение дистанционное, мы присылаем гостям подробную инструкцию, '
            'ключи в сейфе у квартиры, в случае возникновения вопросов '
            'звоните по телефону +7 (906) 256-65-23.',
    },
    CBB_PAYMENT_BY_CARD: {
        CBB_ALL: 'Оплата возможна только переводом или наличными.',
    },
    CBB_PREPAYMENT: {
        CBB_ALL:
            'Стоимость предоплаты составляет 30% от общей '
            'стоимости проживания.'
            'Только после внесения предоплаты мы закрепляем Вашу бронь.',
    },
    CBB_PAYMENT_MADE: {
        CBB_ALL: 'Оплата вносится после заезда переводом или наличными.',
    },
    CBB_BOOKING_CANCEL: {
        CBB_ALL: 'Бесплатная отмена не позднее 2-х недель до даты заезда.',
    },
    CBB_NEAREST_PARKING: {
        CBB_ALL: 'Все парковки в центре платные с 8 до 20.',
        CBB_PESTELYA: 'Открытый двор - ул. Чайковского, 2.',
    },
    CBB_IN_YARD_PARKING: {
        CBB_NEVSKY: 'Нет, заезда во двор, к сожалению, нет.',
        CBB_PESTELYA: 'По запросу.',
    },
    CBB_SHOPS: {
        CBB_PESTELYA:
            '"Дикси", ул. Пестеля, 12.\n'
            '"Фермер", ул. Пестеля, 13.\n'
            '"Азбука вкуса", Литейный пр., 26.',
        CBB_NEVSKY:
            '"ВкусВилл", Невский пр., 130.\n'
            '"Дикси", Невский пр., 126/2.',
    },
    CBB_EAT: {
        CBB_PESTELYA: 'Столовая "Тарелка", ул. Пестеля, 8.',
        CBB_NEVSKY:
            'Столовая №1, Невский пр., 126, '
            '(напротив железной кареты).',
    },
    CBB_TOWEL: {
        CBB_ALL:
            'Мы предоставляем постельное белье и по 2 полотенца на гостя.',
    },
    CBB_WHAT_PROVIDE: {
        CBB_ALL: 'Нет 😙. Только средство д/мытья посуды и жидкое мыло.',
    },
}

# Questions groups
CATEGORIES = {
    CBB_CHECK_IN: (
        CBB_GET_TO,
        CBB_CHECK_IN_TIME,
        CBB_EARLY_LATE_CHECK,
        CBB_SETTLEMENT,
    ),
    CBB_PAYMENT: (
        CBB_PAYMENT_MADE,
        CBB_PAYMENT_BY_CARD,
        CBB_PREPAYMENT,
        CBB_BOOKING_CANCEL,
    ),
    CBB_OTHER: (
        CBB_NEAREST_PARKING,
        CBB_IN_YARD_PARKING,
        CBB_TOWEL,
        CBB_WHAT_PROVIDE,
        CBB_SHOPS,
        CBB_EAT,
    ),
    CBB_HOSTELS: (
        CBB_NEVSKY,
        CBB_PESTELYA,
    )
}


class ILButton(InlineKeyboardButton):
    """Класс кнопки, инициируемой текстом."""
    def __init__(self, cbb: str, **_kwargs: Any):
        super().__init__(text=CBB_CAPTIONS[cbb], callback_data=cbb, **_kwargs)


def _get_il_kbd_v(items: List[str]) -> List[ILButton]:
    btns = [[ILButton(item)] for item in items]
    return btns


def _get_il_kbd_h(items: List[str]) -> List[ILButton]:
    return [[ILButton(item) for item in items]]


def _get_il_kbd_vh(items_v: List[str], items_h: List[str]):
    kbd = _get_il_kbd_v(items_v)
    kbd.extend(_get_il_kbd_h(items_h))
    return kbd


def _get_item(query, items: Iterable) -> str:
    """Ищет nik пункта меню.
    Предполагает что, data - это nik пункта меню,
    или nik пункта меню содержится в переданной строке msg_text.
    """
    if query:
        data = query.data
        msg_text = query.message.text
        if data in items:
            return data
        for item in items:
            if CBB_CAPTIONS[item] in msg_text:
                return item
    return ''


def _format_by_markdown(text: str) -> str:
    """Фоматирует текст в соответствии с форматом MARKDOWN."""
    CHARS = '_*[]()~`>#+-=|{}.!'
    for ch in CHARS:
        text = text.replace(ch, f'\{ch}')
    return text


def _get_caption(base_str: str, key: str) -> str:
    """Возвращает форматированную строку."""
    return base_str.format(
        _format_by_markdown(CBB_CAPTIONS[key])
    ) if key else ''

def _get_message(hostel: str, data: str) -> str:
    """Формирует и возвращает строковое сообщение,
    соответсвующее ключу data.
    """
    for key, value in MESSAGES.items():
        if key == data:
            text = ('\n').join((
                value.get(CBB_ALL, ''),
                value.get(hostel, '')
            )).strip()
            return _format_by_markdown(text)
    return ''


def get_markup(hostel: str = '', category: str = '') -> InlineKeyboardMarkup:
    if not hostel:
        kbd = _get_il_kbd_v(HOSTELS)
    elif not category:
        kbd = _get_il_kbd_h(CATEGORIES.keys())
    else:
        kbd = _get_il_kbd_vh(CATEGORIES.get(category), CATEGORIES.keys())
    return InlineKeyboardMarkup(kbd)


def get_message(query = None) -> str:
    """Формирует сообщение для вывода."""
    hostel = _get_item(query, HOSTELS)
    category = _get_item(query, CATEGORIES.keys())
    if category == CBB_HOSTELS:
        hostel = category = item = ''
    if query and query.data in CATEGORIES.keys():
        item = ''
    else:
        item = _get_item(query, MESSAGES.keys())

    text = _get_message(hostel, item)
    text = ('\n').join((
        _get_caption('*Выбран отель "{}"*', hostel),
        _get_caption('*{}*', category),
        _get_caption('__*{}*__', item),
        text,
    )).strip()
    if not text:
        text = 'Привет ✌️\.\nВыберите отель:'
    return (text, get_markup(hostel, category))
