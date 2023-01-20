from typing import Optional, List, Union, Tuple, Iterable
from telegram import (
    Update,
    ParseMode,
)
from telegram.ext import (
    Updater,
    Handler,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CallbackContext,
)

from Position import Position

from telegram_markup import ILMarkup
from tour_buttons import tour_footer

class Tour():
    """Продвигает пользователя по сети позиций."""

    def __init__(self, token: str, head: Position) -> None:
        """Принимает токен и начальную позицию."""
        self._active = head
        self._updater = Updater(
            token=token,
            request_kwargs={
                'connect_timeout': 0.5,
                'read_timeout': 1.0,
            },
            use_context=True,
        )
        self.add_handlers(
            (
                MessageHandler(
                    Filters.text,
                    self._start_message,
                ),
                CallbackQueryHandler(
                    callback=self._keyboard_callback_handler,
                    pass_chat_data=True,
                ),
            )
        )

    def _start_message(self, update: Update,
        context: CallbackContext
    ) -> None:
        message = update.message
        chat_id = message.chat_id
        message_id = message.message_id
        try:
            while True:
                context.bot.delete_message(chat_id, message_id)
                message_id -= 1
        except:
            pass
        text = self.get_message()
        update.message.reply_text(
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ILMarkup()(callback=message.text, footer=tour_footer),
        )

    def _keyboard_callback_handler(self,
        update: Update,
        context: CallbackContext
    ) -> None:
        query = update.callback_query
        text = self.get_message()

        query.edit_message_text(
            text=text,
            parse_mode='MarkdownV2',
            reply_markup=ILMarkup()(query.data, footer=tour_footer),
        )

    def get_message(self) -> str:
        return ''

    def _update(self) -> None:
        """Обновляет изобажение у пользователя."""
        pass

    def start(self):
        self._updater.start_polling()
        self._updater.idle()

    def stop(self):
        self._updater.stop()

    def step(self) -> None:
        """Переводит текущее положение в следующую позицию."""
        next = self._active.next
        if next:
            self._active = next
            self._update()

    def left(self) -> None:
        """Поворачивает влево."""
        self._active.left()
        self._update()

    def right(self) -> None:
        """Поворачивает вправо."""
        self._active.left()
        self._update()

    def add_handlers(self,
        handlers: Union[Iterable[Handler], Handler]
    ) -> None:
        """Добавляет полученные обработчики в список."""
        for handler in (handlers
            if isinstance(handlers, Iterable) else (handlers,)
        ):
            self._updater.dispatcher.add_handler(handler)
