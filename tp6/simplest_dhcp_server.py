from scapy.all import *

dhcp_server_ip = "10.6.1.253"  
client_ip = "10.6.1.100"  
client_mac = None  

def dhcp_discover_callback(packet):
    global client_mac
    
    if packet.haslayer(DHCP) and packet[DHCP].options[0][1] == 1:  
        client_mac = packet[Ether].src  
        print(f"DHCP Discover reçu de {client_mac}")
        
        dhcp_offer = (
            Ether(dst=client_mac, src="08:00:27:01:02:03") /  
            IP(src=dhcp_server_ip, dst="255.255.255.255") /
            UDP(sport=67, dport=68) /
            BOOTP(op=2, chaddr=mac2str(client_mac), yiaddr=client_ip) /  
            DHCP(options=[
                ("message-type", "offer"),
                ("server_id", dhcp_server_ip),
                ("lease_time", 3600), 
                ("end")
            ])
        )
        sendp(dhcp_offer, iface="enp0s3")  
        print(f"DHCP Offer envoyé à {client_mac}")

def dhcp_request_callback(packet):
    if packet.haslayer(DHCP) and packet[DHCP].options[0][1] == 3: 
        print(f"DHCP Request reçu de {packet[Ether].src}")

        
        dhcp_ack = (
            Ether(dst=packet[Ether].src, src="08:00:27:01:02:03") / 
            IP(src=dhcp_server_ip, dst="255.255.255.255") /
            UDP(sport=67, dport=68) /
            BOOTP(op=2, chaddr=mac2str(packet[Ether].src), yiaddr=client_ip) /
            DHCP(options=[
                ("message-type", "ack"),
                ("server_id", dhcp_server_ip),
                ("lease_time", 3600),  
                ("end")
            ])
        )
        sendp(dhcp_ack, iface="enp0s3")  
        print(f"DHCP ACK envoyé à {packet[Ether].src}")

print("Attente de DHCP Discover...")
sniff(filter="udp and (port 67 or port 68)", prn=dhcp_discover_callback, store=0)
print("Attente de DHCP Request...")
sniff(filter="udp and (port 67 or port 68)", prn=dhcp_request_callback, store=0)
