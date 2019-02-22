from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

import handler.helper as helper


class StartCommandHandler(CommandHandler):
    def __init__(self):
        CommandHandler.__init__(self, "start", self.startCommand)

    # TODO: Extract commands into their own handlers and files
    def startCommand(self, update: Update, context: CallbackContext):
        """Print the help text for a /start or /help command"""
        update.message.reply_text(helper.helpText())

