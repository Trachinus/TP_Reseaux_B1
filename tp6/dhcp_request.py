from scapy.all import *



client_mac = "08:00:27:c2:a9:42"
dhcp_server_ip = "10.6.1.253"
dhcp_server_mac = "08:00:27:a1:ec:42"
requested_ip = "10.6.1.108"

client_mac_bytes = mac2str(client_mac)

dhcp_request = (
    Ether(dst=dhcp_server_mac, src=client_mac, type=0x0800) /  
    IP(src="10.6.1.137", dst=dhcp_server_ip) /  
    UDP(sport=68, dport=67) / 
    BOOTP(chaddr=client_mac_bytes + b'\x00' * 10) /  
    DHCP(options=[
        ("message-type", "request"),   
        ("server_id", dhcp_server_ip),  
        ("requested_addr", requested_ip), 
        ("end")
    ])
)

response = srp1(dhcp_request, iface="enp0s3", timeout=10, verbose=0)
