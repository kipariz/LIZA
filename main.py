import logging
from nltk.chat.util import Chat, reflections
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice
import os

from data import *
import eliza

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! 🎉')
    update.message.reply_text("My name is LIZA, and I'm a bot 🤖")
    update.message.reply_text('You can start conversation with me just taping wethever you want.')
    update.message.reply_text('Hope you will enjoy to have chat with me.')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Hello, my name is LIZA, and I'm a bot 🤖. I have a several pattern that makes pairs, that how I can speak. Please notice that I'm only not whery good writen computer program, so I can`t answer all of your question. I was make mostly like this program: \n(https://en.wikipedia.org/wiki/ELIZA). Hope you will enjoy to have chat with me. Peace!")


def answer(update, context):
    """Answer the user message."""
    model_chat = Chat(pairs, reflections)

    inp_text = update.message.text

    if (str(model_chat.respond(str(inp_text)))=="None"): 
        try:
            update.message.reply_text(eliza.eliza_chatbot.respond(str(inp_text)))
        except:
            update.message.reply_text("Sorry, I don't clearly understand. Let's talk about something else. By the way, " + str(choice(compliments)))
    else:
        update.message.reply_text(model_chat.respond(str(inp_text)))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == "__main__":
    """Start the bot."""
    NAME = "lizatelegrambot"
    TOKEN = os.environ["TOKEN"]

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, answer))
    dp.add_error_handler(error)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
