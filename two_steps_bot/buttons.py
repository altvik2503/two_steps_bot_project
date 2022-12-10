from typing import Tuple, Optional, Iterable
from telegram import (
    InlineKeyboardMarkup,
    CallbackQuery,
)
from telegram_markup import ILButton, ILMarkup

ILB_CHECK_IN_TIME = ILButton(
    'check_in_time',
    'Время заезда/ выезда.',
    ILMarkup.markup_cell,
)
ILB_EARLY_LATE_CHECK = ILButton(
    'early_check',
    'Стоимость раннего заезда/позднего выезда.',
    ILMarkup.markup_cell,
)
ILB_IN_YARD_PARKING = ILButton(
    'in_yard_parking',
    'Можно ли припарковать машину во дворе?',
    ILMarkup.markup_cell,
)
ILB_NEAREST_PARKING = ILButton(
    'nearest_parking',
    'Есть ли поблизости парковки?',
    ILMarkup.markup_cell,
)
ILB_SETTLEMENT = ILButton(
    'settlement',
    'Как происходит процесс заселения?',
    ILMarkup.markup_cell,
)
ILB_PAYMENT_BY_CARD = ILButton(
    'payment_by_card',
    'Возможна ли оплата кредитной картой?',
    ILMarkup.markup_cell,
)
ILB_PREPAYMENT = ILButton(
    'prepayment',
    'Бронь напрямую. Предоплата.',
    ILMarkup.markup_cell,
)
ILB_PAYMENT_MADE = ILButton(
    'payment_made',
    'Каким образом происходит оплата?',
    ILMarkup.markup_cell,
)
ILB_BOOKING_CANCEL = ILButton(
    'booking_cancel',
    'Если я захочу отменить бронирование...',
    ILMarkup.markup_cell,
)
ILB_SHOPS = ILButton(
    'shops',
    'Есть ли рядом магазины?',
    ILMarkup.markup_cell,
)
ILB_TOWEL = ILButton(
    'towel',
    'Белье и полотенца.',
    ILMarkup.markup_cell,
)
ILB_GET_TO = ILButton(
    'get_to',
    'Как доехать?',
    ILMarkup.markup_cell,
)
ILB_EAT = ILButton(
    'eat',
    'Где перекусить быстро/не дорого?',
)
ILB_WHAT_PROVIDE = ILButton(
    'what_provide',
    'Предоставляете ли тапочки, шапочки для душа, '
    'косметические средства?',
)

CHILDREN_CHECK_IN = (
    ILB_GET_TO,
    ILB_CHECK_IN_TIME,
    ILB_EARLY_LATE_CHECK,
    ILB_SETTLEMENT,
)
CHILDREN_PAYMENT = (
    ILB_PAYMENT_MADE,
    ILB_PAYMENT_BY_CARD,
    ILB_PREPAYMENT,
    ILB_BOOKING_CANCEL,
    )
CHILDREN_OTHER = (
    ILB_NEAREST_PARKING,
    ILB_IN_YARD_PARKING,
    ILB_TOWEL,
    ILB_WHAT_PROVIDE,
    ILB_SHOPS,
    ILB_EAT,
    )

ILB_GET_TO.children.add(*CHILDREN_CHECK_IN)
ILB_CHECK_IN_TIME.children.add(*CHILDREN_CHECK_IN)
ILB_EARLY_LATE_CHECK.children.add(*CHILDREN_CHECK_IN)
ILB_SETTLEMENT.children.add(*CHILDREN_CHECK_IN)

ILB_PAYMENT_MADE.children.add(*CHILDREN_PAYMENT)
ILB_PAYMENT_BY_CARD.children.add(*CHILDREN_PAYMENT)
ILB_PREPAYMENT.children.add(*CHILDREN_PAYMENT)
ILB_BOOKING_CANCEL.children.add(*CHILDREN_PAYMENT)

ILB_NEAREST_PARKING.children.add(*CHILDREN_OTHER)
ILB_IN_YARD_PARKING.children.add(*CHILDREN_OTHER)
ILB_TOWEL.children.add(*CHILDREN_OTHER)
ILB_WHAT_PROVIDE.children.add(*CHILDREN_OTHER)
ILB_SHOPS.children.add(*CHILDREN_OTHER)
ILB_EAT.children.add(*CHILDREN_OTHER)

ILB_CHECK_IN = ILButton(
    'check_in',
    'Заезд...',
    ILMarkup.markup_cell,
    *CHILDREN_CHECK_IN,
)
ILB_PAYMENT = ILButton(
    'payment',
    'Оплата...',
    ILMarkup.markup_cell,
    *CHILDREN_PAYMENT
)
ILB_OTHER = ILButton(
    'other',
    'Другое...',
    ILMarkup.markup_cell,
    *CHILDREN_OTHER
)

CHILDREN_CATEGORY = (
    ILB_CHECK_IN,
    ILB_PAYMENT,
    ILB_OTHER,
)

ILB_PESTELYA = ILButton(
    'pestelya',
    'Пестеля',
    ILMarkup.markup_line,
).add_captions(
    (
        ILB_GET_TO.callback,
        '*Аэропорт Пулково:*\n'
        'автобус 39 - ст.м. Московская - ст.м. Гостиный двор '
        '- пешком до ул. Пестеля 5,\n'
        'или "Яндекс такси" 650-850 руб.\n'
        '*Московский вокзал:*\n'
        'общ. транспорт по Невскому пр., до ст. Гостиный двор. '
        'Далее пешком 15 минут,\n'
        'или "Яндекс такси" 180-280 руб.',
    ),
    (
        ILB_NEAREST_PARKING.callback,
        'Открытый двор - ул. Чайковского, 2.',
    ),
    (

        ILB_IN_YARD_PARKING.callback,
        'Нет, заезда во двор, к сожалению, нет.',
    ),
    (
        ILB_SHOPS.callback,
        '"Дикси", ул. Пестеля, 12.\n'
        '"Фермер", ул. Пестеля, 13.\n'
        '"Азбука вкуса", Литейный пр., 26.',
    ),
    (
        ILB_EAT.callback,
        'Столовая "Тарелка", ул. Пестеля, 8.',
    ),

)
ILB_NEVSKY = ILButton(
    'nevsky',
    'Невский',
    ILMarkup.markup_line,
).add_captions(
    (
        ILB_GET_TO.callback,
        '*Аэропорт Пулково:*\n'
        'автобус 39 - ст.м. Московская - ст.м. Пл. Восстания '
        '- пешком до Невский пр. 128 (5 минут).\n'
        'или "Яндекс такси" 650-850 руб.\n'
        '*Московский вокзал:*\n'
        'Пешком 5 минут до Невского пр., 128.',
    ),
    (
        ILB_IN_YARD_PARKING.callback,
        'По согласованию.',
    ),
    (
        ILB_SHOPS.callback,
        '"ВкусВилл", Невский пр., 130.\n'
        '"Дикси", Невский пр., 126/2.',
    ),
    (
        ILB_EAT.callback,
        'Столовая №1, Невский пр., 126, '
        '(напротив железной кареты).',
    ),
)
ILB_ALL = ILButton(
    'all'
).add_captions(
    (
        ILB_CHECK_IN_TIME.callback,
        'Заезд в любое время после 14.00, выезд до 11.00.'
    ),
    (
        ILB_EARLY_LATE_CHECK.callback,
        'Стоимость раннего заезда или позднего выезда '
        'составляет 70% от стоимости дня.',
    ),
    (
        ILB_SETTLEMENT.callback,
        'Заселение дистанционное, мы присылаем гостям подробную инструкцию, '
        'ключи в сейфе у квартиры, в случае возникновения вопросов '
        'звоните по телефону +7 (906) 256-65-23.',
    ),
    (
        ILB_PAYMENT_BY_CARD.callback,
        'Оплата возможна только переводом или наличными.',
    ),
    (
        ILB_PREPAYMENT.callback,
        'Стоимость предоплаты составляет 30% от общей '
        'стоимости проживания.'
        'Только после внесения предоплаты мы закрепляем Вашу бронь.',
    ),
    (
        ILB_PAYMENT_MADE.callback,
        'Оплата вносится после заезда переводом или наличными.',
    ),
    (
        ILB_BOOKING_CANCEL.callback,
        'Бесплатная отмена не позднее 2-х недель до даты заезда.',
    ),
    (
        ILB_NEAREST_PARKING.callback,
        'Все парковки в центре платные с 8 до 20.',
    ),
    (
        ILB_TOWEL.callback,
        'Мы предоставляем постельное белье и по 2 полотенца на гостя.',
    ),
    (
        ILB_WHAT_PROVIDE.callback,
        'Нет 😙. Только средство д/мытья посуды и жидкое мыло.',
    ),
)
ILB_SELECTED_HOSTEL = None
HOSTELS = (ILB_NEVSKY, ILB_PESTELYA)

# ILB_HOSTELS = ILButton(
#     'hostels',
#     'Отель...',
#     ILMarkup.markup_line,
#     *(ILB_NEVSKY, ILB_PESTELYA,)
# )

ILB_CATEGORIES = ILButton(
    'categories',
    'categories',
    None,
    *CHILDREN_CATEGORY,
)
ILB_START = ILButton(
    'start',
    'Привет ✌️\\.\nВыберите отель:',
    ILMarkup.markup_line,
    *(ILB_NEVSKY, ILB_PESTELYA),
    use_footer=False,
)

ILMarkup.footer = {
    'default': ILMarkup.markup_line(
        ILB_CATEGORIES,
    ),

    ILB_CHECK_IN.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_CHECK_IN,)
    ),
    ILB_GET_TO.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_CHECK_IN,)
    ),
    ILB_CHECK_IN_TIME.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_CHECK_IN,)
    ),
    ILB_EARLY_LATE_CHECK.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_CHECK_IN,)
    ),
    ILB_SETTLEMENT.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_CHECK_IN,)
    ),

    ILB_PAYMENT.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_PAYMENT,)
    ),
    ILB_PAYMENT_MADE.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_PAYMENT,)
    ),
    ILB_PAYMENT_BY_CARD.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_PAYMENT,)
    ),
    ILB_PREPAYMENT.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_PAYMENT,)
    ),
    ILB_BOOKING_CANCEL.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_PAYMENT,)
    ),

    ILB_OTHER.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_OTHER,)
    ),
    ILB_NEAREST_PARKING.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_OTHER,)
    ),
    ILB_IN_YARD_PARKING.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_OTHER,)
    ),
    ILB_TOWEL.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_OTHER,)
    ),
    ILB_WHAT_PROVIDE.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_OTHER,)
    ),
    ILB_SHOPS.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_OTHER,)
    ),
    ILB_EAT.callback: ILMarkup.markup_line(
        ILB_CATEGORIES, (ILB_OTHER,)
    ),
}


def get_selected_hostel(query: CallbackQuery) -> Optional[ILButton]:
    return ILButton.find_button_in_text(query.message.text, HOSTELS)  # type: ignore


def get_markup(query: CallbackQuery) -> Tuple[InlineKeyboardMarkup, str]:
    callback = query.data
    il_btn = ILButton.button_by_callback(callback)
    text = ''
    if il_btn:
        hostel = get_selected_hostel(query)
        if hostel:
            text = il_btn.get_text((ILB_ALL, hostel))  # type: ignore
    return ILMarkup()(callback), text

# def get_message(query) -> str:
#     """Формирует сообщение для вывода."""
#     hostel = _get_item(query, HOSTELS)  # type: ignore
#     category = _get_item(query, CATEGORIES.keys())
#     if category == ILB_HOSTELS:
#         hostel = category = item = ''
#     if query and query.data in CATEGORIES.keys():
#         item = ''
#     else:
#         item = _get_item(query, MESSAGES.keys())

#     text = _get_message(hostel, item)
#     text = ('\n').join((
#         _get_caption('*Выбран отель "{}"*', hostel),
#         _get_caption('*{}*', category),
#         _get_caption('__*{}*__', item),
#         text,
#     )).strip()
#     if not text:
#         text = 'Привет ✌️\\.\nВыберите отель:'
#     return text
