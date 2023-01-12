from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help\n/calc')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[3])
    if items[2] == "+":
        await update.message.reply_text(f'{x} + {y} = {x+y}')
    elif items[2] == "-":
        await update.message.reply_text(f'{x} - {y} = {x - y}')
    elif items[2] == "*":
        await update.message.reply_text(f'{x} * {y} = {x * y}')
    elif items[2] == "/":
        await update.message.reply_text(f'{x} / {y} = {x / y}')
