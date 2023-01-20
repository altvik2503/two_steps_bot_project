from telegram_markup import ILButton, ILMarkup

ILB_LEFT = ILButton(
    'left',
    '👈',
)
ILB_RIGHT = ILButton(
    'right',
    '👉',
)
ILB_STEP = ILButton(
    'step',
    '👆',
)
ILB_RETURN = ILButton(
    'return',
    '👇',
)
KBD_DIRECTIONS = (
    (ILB_STEP,),
    (ILB_LEFT, ILB_RETURN, ILB_RIGHT),
)

tour_footer = info_footer = {
    'default': ILMarkup.markup_map(
        KBD_DIRECTIONS,
    ),
}
