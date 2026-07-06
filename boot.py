from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '8888630605:AAEyxmE9CW8YVkQYe0000-0-00-0-0-0-0-0-0-0-0-0-0-0'
BOT_USERNAME = '@my_youseff_bot'

async def start_command (update:Update , context : ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"سلام {user.first_name or ' '} به یوسف بات خوش آمدید!")

async def help_command(update:Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('من یک ربات هستم و دستورات من / start / help / cusgtom هست همینطور به بعضی نوشته های شما پاسخ میدهم')

async def custom_command(update:Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("این یک دستور سفارشی هست")


def handle_response(text: str):
    if not text:
        return "چیزی دریافت نکردم"
    user_text = text.lower()
    if "hello" in user_text or "سلام" in user_text:
        return "علیک سلام"
    if "how are you" in user_text or "چطوری؟" in user_text:
        return "مرسی خوبم شما چطورید؟"
    if "what's new" in user_text or "چه خبر؟" in user_text:
        return "هیچ خبر خاصی نیست سلامتی!"
    if "i live coding" in user_text:
        return "عالی پس جای درستی اومدی"
    return "شرمنده متوجه نشدم"

async def handle_message (update:Update , context : ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    message = update.message
    text = message.text
    chat_type = message.chat.type

    print(f"user : {message.chat.id} , chat type : {chat_type} , text : {text}")

    if chat_type in ("group" , "supergroup"):
        if BOT_USERNAME.lower() in text.lower():
            t = text.replace(BOT_USERNAME , '').strip()
            response = handle_response(t)
        else:
            return
    else:
        response = handle_response(text)

    await message.reply_text(response)

async def error(update:Update , context : ContextTypes.DEFAULT_TYPE):
    print(f'update :  {update} cause error : {context.error}')


if __name__ == "__main__":
    print("bot is starting...")
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler("start" , start_command))
    app.add_handler(CommandHandler("help" , help_command))
    app.add_handler(CommandHandler("custom" , custom_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND , handle_message))
                    
    app.add_error_handler(error)

    print("polling")

    app.run_polling(poll_interval=3)


                    
