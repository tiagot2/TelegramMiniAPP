	from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

TOKEN = '7874407399:AAG5ZHpUIcI5Od2ebdeztuJ5Me5kxtHLat4'
URL_JOGO = 'https://github.com/tiagot2/TelegramMiniAPP/'

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Iniciar Jogo", web_app=WebAppInfo(url=URL_JOGO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Clique abaixo para iniciar o jogo:', reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
