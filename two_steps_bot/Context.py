from typing import Iterable, Tuple, Dict, ClassVar, List
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, Handler

from telegram_markup import ILMarkup

class Context:
    """Связывает задачу с другими задачами.
    Реализует обработчики сообщений Телеграм.
    """
    def __init__(self,
        handlers: Iterable[Handler],
        markup_list: List[List[InlineKeyboardButton]],
    ) -> None:
        self._handlers: Iterable[Handler] = handlers

        self._markup_list: List[List[InlineKeyboardButton]] = markup_list

    @property
    def handlers(self):
        return self._handlers

    @property
    def markup(self) ->InlineKeyboardMarkup:
        return InlineKeyboardMarkup(self._markup_list)

    @property
    def markup_list(self) ->List[List[InlineKeyboardButton]]:
        return self._markup_list

    @property
    def message(self) -> str:
        return ''


class Contexts:
    """Управляет переключениями контекстов.
    Связывает контекст и бот.
    Управляет ботом.
    """

    DEFAULT_CONTEXT_NAME: ClassVar[str] = 'default'

    def __init__(self,
        updater: Updater,
        contexts_items: Iterable[Tuple[str, Context]],
    ) -> None:
        """Инициализация класса Contexts.
        Принимает token, список контекстов и клавиатуру.
        Создаёт и запускает Updater.
        Выводит принятую клавиатуру.
        """
        self._updater: Updater = updater

        self._contexts_items: Dict[str, Context] = {}

        self._context_selected: str = self.DEFAULT_CONTEXT_NAME

        for context in contexts_items:
            self.add_context(*context)

    @property
    def _get_current_context(self) -> Context:
        return self._contexts_items[self.DEFAULT_CONTEXT_NAME]

    def add_context(self, context_name: str, context: Context):
        """Добавляет Context в список контекстов."""
        self._contexts_items[context_name] = context
        for handler in context.handlers:
            self._updater.dispatcher.add_handler(handler)

    def keyboard_callback_handler(self,
        update: Update,
        callback_context: CallbackContext,
    ) -> None:
        """Анализирует callbacks.
        Переключает контексты при получении соответствующего callback,
        иначе вызывает дочерние обработчики.
        """
        callbacks = ILMarkup.get_callbacks(self._get_current_context.markup)

        query = update.callback_query
        callback = query.data

        if callback in callbacks:
            query.edit_message_text(
                text=self._get_current_context.message,
                parse_mode='MarkdownV2',
                reply_markup=self._get_current_context.markup,
            )
