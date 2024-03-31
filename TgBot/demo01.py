from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    filters,
    MessageHandler,
)

import random
import yaml

configPath = "./Tgbot/config.yaml"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """响应start命令"""
    text = "你好~我是一个bot"
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"text+{update.effective_chat.id}"
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="我不会这个哦~"
    )


async def ohayo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texts = ["早上好呀", "我的小鱼你醒了，还记得清晨吗", "哦哈哟~"]
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=random.choice(texts)
    )


if __name__ == "__main__":
    config = yaml.safe_load(open(configPath))

    start_handler = CommandHandler("start", start)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    filter_ohayo = filters.Regex("早安|早上好|哦哈哟|ohayo")
    ohayo_handler = MessageHandler(filter_ohayo, ohayo)

    # 构建 bot
    TOKEN = config["token"]
    application = ApplicationBuilder().token(TOKEN).build()

    # 注册 handler
    application.add_handler(start_handler)
    application.add_handler(ohayo_handler)

    application.add_handler(unknown_handler)

    # run!
    application.run_polling()
