#forty by croc100

import random
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Please enter your Telegram bot token.
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Define bot questions and answers.
questions = {
    "1 + 1": "2",
    "2 + 2": "4",
    "3 + 3": "6"
}

# Keyboard options to show users' chat messages.
chat_keyboard = [["Start Chatting"]]

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    context.user_data["is_bot"] = random.choice([True, False])

    if context.user_data["is_bot"]:
        # If the user is a bot, randomly present a question.
        question, answer = random.choice(list(questions.items()))
        context.user_data["answer"] = answer
        update.message.reply_text(f"{user.first_name}, {question} = ?")
    else:
        # If the user is not a bot, show a button to initiate chatting.
        reply_markup = ReplyKeyboardMarkup(chat_keyboard, one_time_keyboard=True)
        update.message.reply_text(f"{user.first_name}, click 'Start Chatting' to begin chatting.", reply_markup=reply_markup)

def check_answer(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    if "answer" in context.user_data and update.message.text == context.user_data["answer"]:
        # If the user answers correctly, show a button to start chatting.
        context.user_data["is_bot"] = False
        reply_markup = ReplyKeyboardMarkup(chat_keyboard, one_time_keyboard=True)
        update.message.reply_text(f"{user.first_name}, correct! Click 'Start Chatting' to begin chatting.", reply_markup=reply_markup)
    else:
        # If the user is a bot or answers incorrectly, present a new question.
        question, answer = random.choice(list(questions.items()))
        context.user_data["answer"] = answer
        update.message.reply_text(f"{user.first_name}, incorrect. Please try again! {question} = ?")

def chat_start(update: Update, context: CallbackContext) -> None:
    # Grant permission to the user who clicked the "Start Chatting" button.
    reply_markup = ReplyKeyboardRemove()
    update.message.reply_text("Chat initiation successful! Now, you can chat with all participants.", reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_answer))
    dispatcher.add_handler(MessageHandler(Filters.regex("^Start Chatting$"), chat_start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
