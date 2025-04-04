import subprocess
from scapy.all import *

# Lấy danh sách giao diện mạng
def get_interfaces():
    result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]
    interfaces = [line.split()[3] for line in output_lines if len(line.split()) >= 4]
    return interfaces

# Xử lý khi bắt được gói tin
def packet_handler(packet):
    if packet.haslayer(Raw):
        print("🎯 Captured Packet:")
        print(str(packet))

# Bắt đầu chương trình
interfaces = get_interfaces()

# Hiển thị danh sách giao diện mạng
print("📶 Danh sách các giao diện mạng khả dụng:")
for i, iface in enumerate(interfaces, start=1):
    print(f"{i}. {iface}")

# Nhập lựa chọn từ người dùng
choice = int(input("👉 Chọn số tương ứng với giao diện mạng: "))
selected_iface = interfaces[choice - 1]

# Bắt gói tin TCP trên giao diện đã chọn
print(f"🚀 Đang bắt gói tin trên giao diện: {selected_iface}")
sniff(iface=selected_iface, prn=packet_handler, filter="tcp")
