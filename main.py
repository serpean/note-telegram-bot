import logging
import os

from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler

from commands.help_command import help_command
from commands.note_command import note_command
from commands.start_command import start_command
from commands.unknown_command import unknown_command

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ.get("TOKEN")).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler('note', note_command))

    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    application.run_polling()
