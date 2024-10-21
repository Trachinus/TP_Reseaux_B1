from scapy.all import *

def dns_sniff_callback(packet):
    if packet.haslayer(DNS) and packet[DNS].qr == 1:  # Vérifie si c'est une réponse DNS (qr=1)
        print(f"Réponse DNS capturée : {packet[DNS].an.rdata}")

# Lance le sniffing avant d'envoyer la requête pour capturer les réponses DNS
sniff(filter="udp port 53", prn=dns_sniff_callback, timeout=5, store=0)

# Envoie la requête DNS après avoir commencé à écouter
send(IP(dst="10.6.2.12")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="thinkerview.com")))
