    from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
    from telegram.ext import Application, CommandHandler, ContextTypes
    import json
    from datetime import datetime, timedelta

    TOKEN = "7607156543:AAEdnu2_TtGMYOqLSuVeGyg2IOJm0Mm-UbA"
    WEB_APP_URL = "https://khurramov001.github.io/darsjadval2/"

    # Foydalanuvchilar sozlamalari
    users = {}

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        users[user_id] = {"notifications": True}  # Default holatda yoqilgan

        # Web App tugmasi
        button = KeyboardButton("📚 Dars Jadvali", web_app=WebAppInfo(url=WEB_APP_URL))
        keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
        await update.message.reply_text(
            "Dars jadvali va bildirishnomalar uchun:",
            reply_markup=keyboard
        )

    async def check_dars_time():
        with open('dars_jadvali.json', 'r') as f:
            darslar = json.load(f)

        hozir = datetime.now().strftime("%H:%M")
        for dars in darslar:
            if dars["vaqt"] == (datetime.now() + timedelta(minutes=5)).strftime("%H:%M"):
                for user_id in users:
                    if users[user_id]["notifications"]:
                        await context.bot.send_message(
                            chat_id=user_id,
                            text=f"⏰ 5 daqiqadan keyin {dars['fan']} darsi boshlanadi!"
                        )
            elif dars["vaqt"] == (datetime.now() - timedelta(minutes=5)).strftime("%H:%M"):
                for user_id in users:
                    if users[user_id]["notifications"]:
                        await context.bot.send_message(
                            chat_id=user_id,
                            text="✅ Dars tugadi. Uyga yaxshi yetib oling!"
                        )

    if __name__ == "__main__":
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))

        # Har minut tekshirish
        app.job_queue.run_repeating(check_dars_time, interval=60, first=0)

        app.run_polling()