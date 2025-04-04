import psutil
import logging
import asyncio
import time
from telegram import Bot

# Token và chat_id của bạn
BOT_TOKEN = "7567415251:AAESDbbEXkGv-ezSEDpgKgYHh7ta9p-rgBQ"
CHAT_ID = "-4755662245"

# Cấu hình log
logging.basicConfig(level=logging.INFO, filename='system_monitor_bot.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Hàm gửi tin nhắn
async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Ghi log CPU, RAM và gửi
def monitor_cpu_memory():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    message = f"📊 System Monitor:\n- CPU: {cpu_percent}%\n- RAM: {memory_percent}%"
    logger.info(message)
    asyncio.run(send_telegram_message(message))

# Hàm chính
def monitor_system():
    logger.info("Bắt đầu giám sát hệ thống...")
    while True:
        monitor_cpu_memory()
        time.sleep(60)

if __name__ == "__main__":
    monitor_system()
