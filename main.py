from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import *




app = ApplicationBuilder().token("5626705600:AAHn6ek83GYxmtGSd_ajRJp2W33XrxiHvWM").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))
print("server start")
app.run_polling()
