import requests
from scapy.all import ARP, Ether, srp

def local_network_scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]
    print(f"DEBUG: Số thiết bị phản hồi: {len(result)}")

    devices = []
    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        vendor = get_vendor_by_mac(mac)
        print(f"ĐÃ PHÁT HIỆN: IP={ip}, MAC={mac}, Vendor={vendor}")
        devices.append({
            'ip': ip,
            'mac': mac,
            'vendor': vendor
        })
    return devices

def get_vendor_by_mac(mac):
    try:
        url = f"https://api.maclookup.app/v2/macs/{mac}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("company", "Unknown")
        else:
            return "Unknown"
    except Exception as e:
        print("Lỗi khi tra Vendor:", e)
        return "Unknown"

def main():
    ip_range = "192.168.1.1/24"  # Thay đổi nếu mạng bạn khác
    devices = local_network_scan(ip_range)

    print("\n📋 DANH SÁCH THIẾT BỊ PHÁT HIỆN:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")

if __name__ == '__main__':
    main()
