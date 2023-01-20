from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
)

import settings
import buttons


if __name__ == '__main__':

    state = buttons.State()

    updater = Updater(
        token=settings.TOKEN,
        request_kwargs={
            'connect_timeout': 0.5,
            'read_timeout': 1.0,
        },
        use_context=True,
    )
    handlers = [
        CommandHandler(['start'], state.start_handler),
        CommandHandler(['help'], state.start_handler),
        MessageHandler(Filters.text, state.start_handler),
        CallbackQueryHandler(
            callback=state.keyboard_callback_handler,
            pass_chat_data=True,
        )
    ]

    for handler in handlers:
        updater.dispatcher.add_handler(handler)

    print('Bot starts...')
    updater.start_polling()
    updater.idle()
