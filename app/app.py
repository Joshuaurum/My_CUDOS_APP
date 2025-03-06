from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from google import genai
import requests


API_KEY = "AIzaSyBeNnrkza7vWNeQXavO8MDnDMlfOvtKXBo"
MODEL = "gemini-2.0-flash"
TELEGRAM_TOKEN = "7869077851:AAECR_fJldU9DLFGjTP_PmQf9_zm6z6hans"

def chat_request(prompt):
    try:
        client = genai.Client(api_key=API_KEY)

        response = client.models.generate_content(
            model=MODEL,
            contents=[prompt])
        return response.text

    except requests.RequestException as e:
        print(f"Request Error: {e}")

    return ""

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your Gemini-Flash-2.0 Telegram bot. How can I help you?")

# Handle Messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    answer = chat_request(user_message)
    if answer:
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("Error. Try again.")

def main():
    try:
        print("Program Started")
        application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

        # Add Handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Run the Bot
        application.run_polling()
    except KeyboardInterrupt:
        print("Program Finished")


if __name__ == "__main__":
    main()