import handler.helper as helper

from telegram.ext import CommandHandler

class NewEventCommandHandler(CommandHandler):
  def __init__(self):
    # TODO on args
    # pass_job_queue - should be possible to use to e.g. schedule a reminder message
    # pass_chat_data - keep data related to the specific chat, how to make it survive bot restarts?
    # 
    CommandHandler.__init__(self, "newevent", self.neweventCommand)

  # TODO:
  # [] Print message similar to other poll bots inc. options
  # [] Add answer buttons
  # [] Connect answer buttons to data
  # [] Update original message with updated data
  # [] Add status command to reprint active poll
  # [] Cancel/close command
  # [] Basic error handling if already exist a poll
  # [] Add end time for a poll (auto close)
  # [] Decide creation of poll (manual vs. automated)
  # [] Persistent storage for current poll
  # [] Multiple active polls
  # [] Add custom polls (other than CS events)
  # [] Add Configurable or random answer options
  def neweventCommand(self, bot, update):
    """Create a poll as result of command /newevent"""
    message = update.message
    text = helper.assembleEventHeader("None")
    reply_markup = helper.assembleEventButtons()
    message.reply_text(text, quote=False, reply_markup=reply_markup)
    