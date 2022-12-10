# buttons.py

from typing import Any, List, Iterable, Tuple, Dict, ClassVar, Optional, Callable
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)



# Buttons
class ILButton:
    """Класс кнопки, инициируемой текстом.
    Параметры класса:
        get_by_callbacks
         - принимает список идентификаторов callback,
         - возвращает кортеж ссылок на объекты кнопок.

    Параметры объекта:
        свойства:
            callback - возвращаемый при нажатии идентификатор кнопки;
        методы-свойства:
            все методы-свойства принимают объект кнопки (родителя),
            при отсутствии берут объект текущей кнопки

            button
             - возвращает соответствующую кнопку Markup
            caption
             - возвращает соответствующую надпись на кнопке Markup;
        методы:
            add_captions
             - принимает пары (объект кнопки, соответствующая надпись)
             - создаёт кнопки Markup с полученными параметрами
               и связывает их с объектами кнопки.
    """

    class Children:
        """Содержит перечень подчинённых объектов ILButton."""

        def __init__(self, *children: 'ILButton') -> None:
            self._children: List['ILButton'] = []
            self.add(*children)

        @property
        def buttons(self):
            """Возвращает кортеж подчинённых объектов ILButton"""
            return tuple(self._children)

        @property
        def callbacks(self):
            """Возвращает кортеж параметров callback
            подчинённых объектов ILButton.
            """
            return (child.callback for child in self.buttons),

        def add(self, *children: 'ILButton'):
            """Добавляет полученные объекты ILButton в перечень."""
            for child in children:
                if not child or child in self._children:
                    continue
                self._children.append(child)
            return self

    # Словарь всех объектов ILButton и их параметров callback
    _buttons: ClassVar[Dict[str, 'ILButton']] = {}

    def __init__(self,
        callback: str,
        caption: Optional[str] = None,
        markup_func: Optional[Callable] = None,
        *children: 'ILButton',
        use_footer: bool = True,
        footer: Optional[List[List[InlineKeyboardButton]]] = None,
    ):
        self._buttons[callback] = self

        self._callback: str = callback

        self._markup_buttons: Dict[str, InlineKeyboardButton] = {
            callback:
            InlineKeyboardButton(
                caption if caption else callback,
                callback_data=callback,
            )
        }

        self._markup_func = markup_func

        self.children: 'ILButton.Children' = self.Children(*children)

        self._use_footer: bool = use_footer

        self._footer = footer

    def __str__(self) -> str:
        return self.callback

    def _get_btn(self, btn: Optional['ILButton']):
        """Возвращает self при отсутствии объекта ILButton."""
        return btn if btn else self

    @classmethod
    def item_by_callback(cls, callback: str):
        """Ищет объект ILButton по callbsck.
        Возвращает найденный объект. При отсутствии возвращает None.
        """
        relation = cls._buttons.get(callback) if callback else None
        return relation if relation else None

    @classmethod
    def button_by_callback(cls, callback: str):
        """Ищет объект ILButton по callbsck.
        Возвращает найденный объект. При отсутствии возвращает None.
        """
        return cls._buttons.get(callback) if callback else None

    @classmethod
    def buttons_by_callbacks(cls, *callbacks: str):
        """Ищет объекты ILButton по callbsck.
        Возвращает кортеж найденных объектов. При отсутствии возвращает путой кортеж.
        """
        return [cls.button_by_callback(callback) for callback in callbacks]

    @classmethod
    def find_button_in_text(cls, text: str, il_buttons: Iterable['ILButton']):
        for il_button in il_buttons:
            if il_button.caption() in text:
                return il_button

    @property
    def use_footer(self) -> bool:
        return self._use_footer

    @use_footer.setter
    def use_footer(self, use_footer: bool) -> None:
        self._use_footer = use_footer

    @property
    def footer(self) -> Optional[List[List[InlineKeyboardButton]]]:
        return self._footer

    @footer.setter
    def footer(self, footer: Optional[List[List[InlineKeyboardButton]]]) -> None:
        self._footer = footer

    @property
    def callback(self):
        """Возвращает callback текущего объекта ILButton."""
        return self._callback

    @property
    def markup_func(self):
        """Возвращает метод формирования markup."""
        return self._markup_func

    def markup_button(self,
        btn: Optional['ILButton'] = None
    ) -> InlineKeyboardButton:
        """Возвращает InlineKeyboardButton, соответствующую полученному,
        либо, при отствии полученного объекта, текущему объекту ILButton.
        """
        return self._markup_buttons.get(
            self._get_btn(btn).callback,
            self._markup_buttons.get(self.callback)
        )  # type: ignore

    def caption(self, btn: Optional['ILButton'] = None) -> str:
        """Возвращает подпись на InlineKeyboardButton,
        соответствующей полученному, либо, при отствии полученного объекта,
        текущему объекту ILButton.
        """
        return self.markup_button(self._get_btn(btn)).text

    def add_captions(self, *captions: Tuple[str, str]):
        """Получает перечень кортежей (callback, caption).
        Добавляет в перечень кнопок для полученных callback
        кнопки InlineKeyboardButton с полученными caption
        и callback текущего объекта кнопки.
        """
        for callback, caption in captions:
            self._markup_buttons[callback] = InlineKeyboardButton(
                caption,
                callback_data=self._callback,
            )
        return self

    def get_text(self, parents: Tuple['ILButton']) -> str:
        text = ''
        for parent in parents:
            btn = parent._markup_buttons.get(self.callback)
            text = '\n'.join((text, btn.text if btn else ''))
        return text.strip()


class ILMarkup:
    _footer: ClassVar[Dict[str, List[List[InlineKeyboardButton]]]]

    @classmethod
    def __call__(cls,
        callback: str,
        markup_func: Optional[Callable] = None,
        *args,
        **kwargs
    ) -> InlineKeyboardMarkup:
        il_button = cls._callback_to_button(callback)
        kbd = [[]]
        if il_button:
            add_footer = il_button.use_footer
            markup_func = markup_func if markup_func else il_button.markup_func
            if markup_func:
                kbd = markup_func(il_button, *args, **kwargs)
            if add_footer:
                footer = kwargs.get('footer')
                if not footer and ILMarkup.footer:
                    footer = ILMarkup.footer
                if footer:
                    kbd.extend(cls.markup_selected(il_button, footer))
        return InlineKeyboardMarkup(kbd)

    @classmethod
    def _callback_to_button(cls,
        callback: str
    ) -> Optional[ILButton]:
        return ILButton.button_by_callback(callback)

    @property
    @classmethod
    def footer(cls):
        return cls._footer

    @footer.setter
    @classmethod
    def footer(cls, footer: Dict[str, List[List[InlineKeyboardButton]]]):
        cls._footer = footer

    @classmethod
    def markup_button(cls,
        btn: ILButton,
        *args, **kwargs
    ) -> List[List[InlineKeyboardButton]]:
        """Получает объект кнопки.
        Возвращает соответствующую markup-кнопку.
        """
        m_btn = btn.markup_button()
        text = m_btn.text
        text = text.center(len(text) + 8, ' ').center(40, '*')
        return [[
            InlineKeyboardButton(text,
            callback_data=m_btn.callback_data)
        ]]

    @classmethod
    def markup_line(cls,
        btn: ILButton,
        exclude: Tuple[ILButton] = tuple(),
        *args, **kwargs
    ) -> List[List[InlineKeyboardButton]]:
        """Получает объект кнопки и перечень исключений - объектов кнопок.
        Формирует список дочерних к полученному объекту объектов кнопок,
        исключив из него содержащиеся в перечне исключений.
        Возвращает список murkup-кнопок, соответствующих
        объектам кнопок в полученном списке
        в формате для горизонтального отражения.
        """
        return [[chield_btn.markup_button()
            for chield_btn in btn.children.buttons
            if chield_btn not in exclude
        ]]

    @classmethod
    def markup_cell(cls,
        btn: ILButton,
        exclude: Tuple[ILButton] = tuple(),
        *args, **kwargs
    ) -> List[List[InlineKeyboardButton]]:
        """Получает объект кнопки и перечень исключений - объектов кнопок.
        Формирует список дочерних к полученному объекту объектов кнопок,
        исключив из него содержащиеся в перечне исключений.
        Возвращает список murkup-кнопок, соответствующих
        объектам кнопок в полученном списке
        в формате для вертикального отражения.
        """
        return [[item] for item in cls.markup_line(btn, exclude)[0]]

    @classmethod
    def markup_selected(cls,
        selection: ILButton,
        choice: Dict[str, List[List[InlineKeyboardButton]]],
        *args, **kwargs
    ) -> List[List[InlineKeyboardButton]]:
        return choice.get(selection.callback, choice.get('default', [[]]))
