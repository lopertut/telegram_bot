import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, ConversationHandler
from weather import *


START, ASK_CITY = range(2)


# Logging system configuration
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    send message when command /start called

    args:
    update: contains info about message or event
    context: provides access to methods and data to perform operations with the bot
    """
    start_message = (
        'Hello! Im a bot that can provide weather information.\n\n'
         'Available commands:\n'
         '/start - Start a conversation with the bot\n'
         '/help - Get help about the bot\n'
         '/weather - Find out the weather in your city\n'
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)
    return START


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    send message when command /start called

    args:
    update: contains info about message or event
    context: provides access to methods and data to perform operations with the bot
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text='what you need to know')


async def weather_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отправляем запрос пользователю о названии города
    await context.bot.send_message(chat_id=update.effective_chat.id, text='enter city:')
    return ASK_CITY


def handle_city_input(update: Update):
    city = update.message.text
    forecast = Forecast(city)
    weather_data = forecast.weather()
    update.message.reply_text(weather_data)
    return ConversationHandler.END


def main():
    # create bot application
    application = ApplicationBuilder().token('7017559815:AAG7EZ86xMhVufKTpj16FFgQt7vxhCkUJSY').build()

    # create commands handlers
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)
    weather_handler = CommandHandler('weather', weather_info)

    # create conversation handler
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('weather', weather_info)],
        states={
            ASK_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_city_input)]
        },
        fallbacks=[]
    )

    # add handlers
    application.add_handler(conversation_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(weather_handler)

    # checking updates for bot
    application.run_polling()


if __name__ == '__main__':
    main()
