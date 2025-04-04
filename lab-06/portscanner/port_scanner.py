from scapy.all import *
import socket

# Danh sách các cổng phổ biến
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

# Hàm quét port
def scan_common_ports(target_domain, timeout=2):
    open_ports = []
    target_ip = socket.gethostbyname(target_domain)

    for port in COMMON_PORTS:
        response = sr1(IP(dst=target_ip)/TCP(dport=port, flags="S"), timeout=timeout, verbose=0)

        # Nếu có phản hồi và cờ là SYN-ACK
        if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
            open_ports.append(port)
            # Gửi RST để đóng kết nối lại
            send(IP(dst=target_ip)/TCP(dport=port, flags="R"), verbose=0)

    return open_ports

# Hàm chính
def main():
    target_domain = input("🔎 Nhập domain hoặc IP cần quét: ")
    open_ports = scan_common_ports(target_domain)

    if open_ports:
        print("✅ Các cổng mở:")
        print(open_ports)
    else:
        print("❌ Không phát hiện cổng phổ biến nào đang mở.")

if __name__ == '__main__':
    main()
