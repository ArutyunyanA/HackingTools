from scapy.all import ARP, Ether, srp

target_ip = "172.20.10.3/99"
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=3)[0]
clients = list(clients.append({'ip': received.psrc, 'mac': received.hwsrc}) for sent, received in result)
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))