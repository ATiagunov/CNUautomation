from logging import Filter
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

TOKEN = '5801504689:AAGVBwC22GT9oV23t56X_ueBrNo_oCV4p4g'
BOT_USERNAME = 'https://t.me/CNU_dispatch_bot'

# you will need the groub_b_id saved as a global variable or
# in some other document
group_b_id = -1001961687786

# create the bot, updater, and dispatcher
bot = telegram.Bot(TOKEN)
# updater = Updater(TOKEN)
# dp = updater.dispatcher

# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a CNU bot.')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text("This chat's id is: " + str(chat_id))


# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I\'m good!'

    return 'I don\'t understand'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # gets the chat_id of the current chat
    chat_id = update.effective_chat.id
    await update.message.reply_text("This chat's id is: " + str(chat_id))

async def auto_forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # automatically forwards messages from this chat to
    # chat_b
    
    # global bot, group_b_id
    chat_id = update.effective_chat.id
    username = update.effective_message.from_user.name
    chat_title = update.effective_message.chat.title
    msg_txt = update.effective_message.text
    telegram.Bot.forw()
    bot.send_message(
        group_b_id, 
        text=f"'{msg_txt}'\nwas just sent in chat {chat_title} by {username}"
    )
    
def auto_forward_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # get variables
    global bot, group_b_id
    chat_id = update.effective_chat.id
    username = update.effective_message.from_user.name
    chat_title = update.effective_message.chat.title
    
    # get the third best quality photo
    photos = len(update.message.photo)
    img_index = max(photos-3, 0) # change -3 to -2 to get second best etc
    img = update.message.photo[img_index]
    
    # send message to GroupB the group that you want the stuff forwarded to
    bot.send_message(group_b_id, str(username) + " just sent me an image from the `" + str(chat_title) + "` chat:")
    bot.send_photo(group_b_id, img)
        



# # Start the Bot
# updater.start_polling()
# updater.idle()

# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Forwarding
    app.add_handler(CommandHandler('get_chat_id', get_chat_id))
    # app.add_handler(MessageHandler(filters.Text, auto_forward))
    # app.add_handler(MessageHandler(filters._Photo, auto_forward_image))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
