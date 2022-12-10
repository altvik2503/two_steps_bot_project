from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyMarkup,
)
from telegram import (
    Update,
    ParseMode,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CallbackContext,
)

import keyboards
import telegram_markup
import settings
import buttons

from decorators import log_errors


@log_errors
def start_message(update: Update, context: CallbackContext):
    message = update.message
    chat_id = message.chat_id
    message_id = message.message_id
    try:пше
        while True:
            context.bot.delete_message(chat_id, message_id)
            message_id -= 1
    except Exception as err:
        pass
    text = keyboards.get_message(update.query)
    markup = telegram_markup.ILMarkup()(buttons.ILB_START.callback)
    update.message.reply_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


@log_errors
def keyboard_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    reply_text = keyboards.get_message(query)
    markup, text = buttons.get_markup(query)
    # markup = telegram_markup.ILMarkup()(query.data)

    print(query.message.message_id)
    query.edit_message_text(
        text=reply_text,
        parse_mode='MarkdownV2',
        reply_markup=markup,
    )


if __name__ == '__main__':
    updater = Updater(
        token=settings.TOKEN,
        request_kwargs={
            'connect_timeout': 0.5,
            'read_timeout': 1.0,
        },
        use_context=True,
    )
    handlers = [
        CommandHandler(['start'], start_message),
        CommandHandler(['help'], start_message),
        MessageHandler(Filters.text, start_message),
        CallbackQueryHandler(callback=keyboard_callback_handler, pass_chat_data=True)
    ]

    for handler in handlers:
        updater.dispatcher.add_handler(handler)

    print('Bot starts...')
    updater.start_polling()
    updater.idle()
