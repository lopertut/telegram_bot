import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Im a bot, please talk to me!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='what you need to know')


if __name__ == '__main__':
    application = ApplicationBuilder().token('7017559815:AAG7EZ86xMhVufKTpj16FFgQt7vxhCkUJSY').build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)

    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling()
