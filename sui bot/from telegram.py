from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Define the start function
async def start(update: Update, context):
    await update.message.reply_text('Welcome to Sui Notification Bot!')

# Build the application with your bot token
app = ApplicationBuilder().token("7049965562:AAGaPyVExlT97lT3Km7HDwipSiLiZTNOqb0").build()

# Add the command handler for the /start command
app.add_handler(CommandHandler('start', start))

# Start polling
app.run_polling()
