from typing import List, Any, Iterable, Tuple, Union
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyMarkup,
)

# Buttons
class ILButton1(InlineKeyboardButton):
    """Класс кнопки, инициируемой текстом."""
    _CENTER_WIDTH = 30
    _CENTER_FILL = '_'
    def __init__(self, cbb: str, caption = None, message: str = '', **_kwargs: Any):
        self._message = message
        _caption = caption if caption else ILB_CAPTIONS[cbb]
        super().__init__(text=_caption, callback_data=cbb, **_kwargs)

    def __str__(self) -> str:
        return self._message

    def center(self, fill=_CENTER_FILL, width=_CENTER_WIDTH):
        self.text.center(width, fill)
        return self


ILB_ALL = 'all'
ILB_PESTELYA = 'pestelya'
ILB_NEVSKY = 'nevsky'

ILB_CHECK_IN_TIME = 'check_in_time'
ILB_EARLY_LATE_CHECK = 'early_check'
ILB_IN_YARD_PARKING = 'in_yard_parking'
ILB_NEAREST_PARKING = 'nearest_parking'
ILB_SETTLEMENT = 'settlement'
ILB_PAYMENT_BY_CARD = 'payment_by_card'
ILB_PREPAYMENT = 'prepayment'
ILB_PAYMENT_MADE = 'payment_made'
ILB_BOOKING_CANCEL = 'booking_cancel'
ILB_SHOPS = 'shops'
ILB_TOWEL = 'towel'
ILB_GET_TO = 'get_to'
ILB_EAT = 'eat'
ILB_WHAT_PROVIDE = 'what_provide'

ILB_CHECK_IN = 'check_in'
ILB_PAYMENT = 'payment'
ILB_OTHER = 'other'
ILB_HOSTELS = 'hostels'

ILB_CAPTIONS = {
    ILB_PESTELYA: 'Пестеля',
    ILB_NEVSKY: 'Невский',

    ILB_CHECK_IN_TIME: 'Время заезда/ выезда.',
    ILB_EARLY_LATE_CHECK: 'Стоимость раннего заезда/позднего выезда.',
    ILB_IN_YARD_PARKING: 'Можно ли припарковать машину во дворе?',
    ILB_NEAREST_PARKING: 'Есть ли поблизости парковки?',
    ILB_SETTLEMENT: 'Как происходит процесс заселения?',
    ILB_PAYMENT_BY_CARD: 'Возможна ли оплата кредитной картой?',
    ILB_PREPAYMENT: 'Бронь напрямую. Предоплата.',
    ILB_PAYMENT_MADE: 'Каким образом происходит оплата?',
    ILB_BOOKING_CANCEL: 'Если я захочу отменить бронирование...',
    ILB_SHOPS: 'Есть ли рядом магазины?',
    ILB_TOWEL: 'Белье и полотенца.',
    ILB_GET_TO: 'Как доехать?',
    ILB_EAT: 'Где перекусить быстро/не дорого?',
    ILB_WHAT_PROVIDE:
        'Предоставляете ли тапочки, шапочки для душа, '
        'косметические средства?',

    ILB_CHECK_IN: 'Заезд...',
    ILB_PAYMENT: 'Оплата...',
    ILB_OTHER: 'Другое...',
    ILB_HOSTELS: 'Отель...',
}

HOSTELS = (
    ILB_NEVSKY,
    ILB_PESTELYA,
)

MESSAGES = {
    ILB_GET_TO: {
        ILB_PESTELYA:
            '*Аэропорт Пулково:*\n'
            'автобус 39 - ст.м. Московская - ст.м. Гостиный двор '
            '- пешком до ул. Пестеля 5,\n'
            'или "Яндекс такси" 650-850 руб.\n'
            '*Московский вокзал:*\n'
            'общ. транспорт по Невскому пр., до ст. Гостиный двор. '
            'Далее пешком 15 минут,\n'
            'или "Яндекс такси" 180-280 руб.',
        ILB_NEVSKY:
            '*Аэропорт Пулково:*\n'
            'автобус 39 - ст.м. Московская - ст.м. Пл. Восстания '
            '- пешком до Невский пр. 128 (5 минут).\n'
            'или "Яндекс такси" 650-850 руб.\n'
            '*Московский вокзал:*\n'
            'Пешком 5 минут до Невского пр., 128.',
    },
    ILB_CHECK_IN_TIME: {
        ILB_ALL: 'Заезд в любое время после 14.00, выезд до 11.00.',
    },
    ILB_EARLY_LATE_CHECK: {
        ILB_ALL:
            'Стоимость раннего заезда или позднего выезда '
            'составляет 70% от стоимости дня.',
    },
    ILB_SETTLEMENT: {
        ILB_ALL:
            'Заселение дистанционное, мы присылаем гостям подробную инструкцию, '
            'ключи в сейфе у квартиры, в случае возникновения вопросов '
            'звоните по телефону +7 (906) 256-65-23.',
    },
    ILB_PAYMENT_BY_CARD: {
        ILB_ALL: 'Оплата возможна только переводом или наличными.',
    },
    ILB_PREPAYMENT: {
        ILB_ALL:
            'Стоимость предоплаты составляет 30% от общей '
            'стоимости проживания.'
            'Только после внесения предоплаты мы закрепляем Вашу бронь.',
    },
    ILB_PAYMENT_MADE: {
        ILB_ALL: 'Оплата вносится после заезда переводом или наличными.',
    },
    ILB_BOOKING_CANCEL: {
        ILB_ALL: 'Бесплатная отмена не позднее 2-х недель до даты заезда.',
    },
    ILB_NEAREST_PARKING: {
        ILB_ALL: 'Все парковки в центре платные с 8 до 20.',
        ILB_PESTELYA: 'Открытый двор - ул. Чайковского, 2.',
    },
    ILB_IN_YARD_PARKING: {
        ILB_NEVSKY: 'По согласованию.',
        ILB_PESTELYA: 'Нет, заезда во двор, к сожалению, нет.',
    },
    ILB_SHOPS: {
        ILB_PESTELYA:
            '"Дикси", ул. Пестеля, 12.\n'
            '"Фермер", ул. Пестеля, 13.\n'
            '"Азбука вкуса", Литейный пр., 26.',
        ILB_NEVSKY:
            '"ВкусВилл", Невский пр., 130.\n'
            '"Дикси", Невский пр., 126/2.',
    },
    ILB_EAT: {
        ILB_PESTELYA: 'Столовая "Тарелка", ул. Пестеля, 8.',
        ILB_NEVSKY:
            'Столовая №1, Невский пр., 126, '
            '(напротив железной кареты).',
    },
    ILB_TOWEL: {
        ILB_ALL:
            'Мы предоставляем постельное белье и по 2 полотенца на гостя.',
    },
    ILB_WHAT_PROVIDE: {
        ILB_ALL: 'Нет 😙. Только средство д/мытья посуды и жидкое мыло.',
    },
}

# Questions groups
CATEGORIES = {
    ILB_CHECK_IN: (
        ILB_GET_TO,
        ILB_CHECK_IN_TIME,
        ILB_EARLY_LATE_CHECK,
        ILB_SETTLEMENT,
    ),
    ILB_PAYMENT: (
        ILB_PAYMENT_MADE,
        ILB_PAYMENT_BY_CARD,
        ILB_PREPAYMENT,
        ILB_BOOKING_CANCEL,
    ),
    ILB_OTHER: (
        ILB_NEAREST_PARKING,
        ILB_IN_YARD_PARKING,
        ILB_TOWEL,
        ILB_WHAT_PROVIDE,
        ILB_SHOPS,
        ILB_EAT,
    ),
    ILB_HOSTELS: (
        ILB_NEVSKY,
        ILB_PESTELYA,
    )
}


def _get_kbd(
    format: str = 'h',
    *args: Iterable[str],
    markup: ReplyMarkup = InlineKeyboardMarkup  # type: ignore
):
    """ Возвращает инлайн клавиатуру, формируемую по формату.
    В format получает строку букв формата,
    где 'h' - горизонтальное расположение клашиш, иначе - вертикальное.
    В args получает наборы имён кнопок для формирования клавиш.
    Порядок кнопок соответствует порядку букв в format.
    """
    btns = []
    for i, ch in enumerate(format):
        items = args[i]
        if items:
            btns.extend([
                (
                    lambda ch, btn: btn if ch == 'h' else [btn]
                )(
                    ch, ILButton1(item)
                ) for item in items
            ])
    return markup(btns)  # type: ignore


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
            if ILB_CAPTIONS[item] in msg_text:
                return item
    return ''


def _format_by_markdown(text: str) -> str:
    """Фоматирует текст в соответствии с форматом MARKDOWN."""
    CHARS = '_*[]()~`>#+-=|{}.!'
    for ch in CHARS:
        text = text.replace(ch, f'\\{ch}')
    return text


def _get_caption(base_str: str, key: str) -> str:
    """Возвращает форматированную строку."""
    return base_str.format(
        _format_by_markdown(ILB_CAPTIONS[key])
    ) if key else ''


def _get_message(hostel: str, data: str) -> str:
    """Формирует и возвращает строковое сообщение,
    соответсвующее ключу data.
    """
    for key, value in MESSAGES.items():
        if key == data:
            text = ('\n').join((
                value.get(ILB_ALL, ''),
                value.get(hostel, '')
            )).strip()
            return _format_by_markdown(text)
    return ''


def _get_category_kbd(category: str = ''):
    categories = CATEGORIES.keys()
    if category:
        categories.remove(category)  # type: ignore
    return _get_kbd(
        'vvh',
        [ILButton(category)] if category else None,  # type: ignore
        CATEGORIES.get(category, None),
        categories,
    )


def get_markup(hostel: str = '', category: str = '') -> InlineKeyboardMarkup:
    if not hostel:
        return _get_kbd('v', HOSTELS)
    elif not category:
        return _get_category_kbd()
    else:
        return _get_category_kbd(category)


def get_message(query = None) -> str:
    """Формирует сообщение для вывода."""
    hostel = _get_item(query, HOSTELS)
    category = _get_item(query, CATEGORIES.keys())
    if category == ILB_HOSTELS:
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
        text = 'Привет ✌️\\.\nВыберите отель:'
    return text
