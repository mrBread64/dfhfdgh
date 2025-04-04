import psutil
import platform
import socket
import logging
import time

# Thiết lập logging
logging.basicConfig(level=logging.INFO, filename='system_monitor.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Ghi log hệ thống
def log_system_info():
    hostname = socket.gethostname()
    os_info = platform.system() + " " + platform.release()
    python_version = platform.python_version()

    logger.info(f"System Info: Hostname: {hostname}")
    logger.info(f"System Info: OS: {os_info}")
    logger.info(f"System Info: Python version: {python_version}")

# Ghi log mạng
def log_network():
    net = psutil.net_io_counters()
    logger.info(f"Network: Bytes Sent: {net.bytes_sent}, Bytes Received: {net.bytes_recv}")

# Ghi log tiến trình đang chạy
def log_software():
    software_list = psutil.process_iter(attrs=['pid', 'name', 'username'])
    logger.info("Software - Running processes:")
    for software in software_list:
        logger.info(f"{software.info['pid']}, {software.info['name']}, {software.info['username']}")

# Ghi log CPU, RAM
def log_cpu_memory():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    logger.info(f"CPU Usage: {cpu}%")
    logger.info(f"Memory Usage: {memory}%")

# Hàm chính
def monitor_system():
    log_system_info()
    while True:
        log_cpu_memory()
        log_network()
        log_software()
        logger.info("----- System Monitoring -----")
        time.sleep(60)

if __name__ == '__main__':
    monitor_system()
