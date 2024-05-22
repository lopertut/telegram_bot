import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler


# Logging system configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """send message when command /start called"""
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Im a bot, please talk to me!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """send message when command /help called"""
    await context.bot.send_message(chat_id=update.effective_chat.id, text='what you need to know')


if __name__ == '__main__':
    # create bot application
    application = ApplicationBuilder().token('7017559815:AAG7EZ86xMhVufKTpj16FFgQt7vxhCkUJSY').build()

    # create commands handlers
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)

    # add handlers
    application.add_handler(start_handler)
    application.add_handler(help_handler)

    # checking updates for bot
    application.run_polling()
