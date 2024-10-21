☀️ Prouvez que...

```
[durian@dhcp ~]$ ping google.com
PING google.com (142.250.201.46) 56(84) bytes of data.
64 bytes from mrs08s20-in-f14.1e100.net (142.250.201.46): icmp_seq=1 ttl=111 time=17.5 ms
64 bytes from mrs08s20-in-f14.1e100.net (142.250.201.46): icmp_seq=2 ttl=111 time=16.4 ms
64 bytes from mrs08s20-in-f14.1e100.net (142.250.201.46): icmp_seq=3 ttl=111 time=17.8 ms
64 bytes from mrs08s20-in-f14.1e100.net (142.250.201.46): icmp_seq=4 ttl=111 time=17.6 ms
64 bytes from mrs08s20-in-f14.1e100.net (142.250.201.46): icmp_seq=5 ttl=111 time=17.2 ms
^C
--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 16.401/17.304/17.795/0.488 ms


[durian@web ~]$ ping google.com
PING google.com (142.251.37.174) 56(84) bytes of data.
64 bytes from mrs09s14-in-f14.1e100.net (142.251.37.174): icmp_seq=1 ttl=111 time=16.7 ms
64 bytes from mrs09s14-in-f14.1e100.net (142.251.37.174): icmp_seq=2 ttl=111 time=16.9 ms
64 bytes from mrs09s14-in-f14.1e100.net (142.251.37.174): icmp_seq=3 ttl=111 time=18.7 ms
64 bytes from mrs09s14-in-f14.1e100.net (142.251.37.174): icmp_seq=4 ttl=111 time=18.3 ms
64 bytes from mrs09s14-in-f14.1e100.net (142.251.37.174): icmp_seq=5 ttl=111 time=16.6 ms
^C
--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 16.608/17.453/18.722/0.892 ms


[durian@dhcp ~]$ ping 10.6.2.12
PING 10.6.2.12 (10.6.2.12) 56(84) bytes of data.
64 bytes from 10.6.2.12: icmp_seq=1 ttl=63 time=1.33 ms
64 bytes from 10.6.2.12: icmp_seq=2 ttl=63 time=1.43 ms
64 bytes from 10.6.2.12: icmp_seq=3 ttl=63 time=1.29 ms
64 bytes from 10.6.2.12: icmp_seq=4 ttl=63 time=1.26 ms
^C
--- 10.6.2.12 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3009ms
rtt min/avg/max/mdev = 1.256/1.324/1.425/0.063 ms
```

☀️ Prouvez que...

```
dorian@client1:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:c2:a9:42 brd ff:ff:ff:ff:ff:ff
    inet 10.6.1.37/24 brd 10.6.1.255 scope global dynamic noprefixroute enp0s3
       valid_lft 574sec preferred_lft 574sec
    inet6 fe80::a00:27ff:fec2:a942/64 scope link
       valid_lft forever preferred_lft forever


dorian@client1:~$ resolvectl
Global
         Protocols: -LLMNR -mDNS -DNSOverTLS DNSSEC=no/unsupported
  resolv.conf mode: stub

Link 2 (enp0s3)
    Current Scopes: DNS
         Protocols: +DefaultRoute -LLMNR -mDNS -DNSOverTLS DNSSEC=no/unsupported
Current DNS Server: 1.1.1.1
       DNS Servers: 1.1.1.1


dorian@client1:~$ ip route show
default via 10.6.1.254 dev enp0s3 proto dhcp src 10.6.1.137 metric 100
10.6.1.0/24 dev enp0s3 proto kernel scope link src 10.6.1.137 metric 100


dorian@client1:~$ ping google.com
PING google.com (142.251.37.46) 56(84) bytes of data.
64 bytes from mrs09s13-in-f14.1e100.net (142.251.37.46): icmp_seq=1 ttl=112 time=16.9 ms
64 bytes from mrs09s13-in-f14.1e100.net (142.251.37.46): icmp_seq=2 ttl=112 time=16.4 ms
64 bytes from mrs09s13-in-f14.1e100.net (142.251.37.46): icmp_seq=3 ttl=112 time=16.5 ms
64 bytes from mrs09s13-in-f14.1e100.net (142.251.37.46): icmp_seq=4 ttl=112 time=16.9 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3011ms
rtt min/avg/max/mdev = 16.446/16.687/16.936/0.226 ms
```

☀️ Déterminer sur quel port écoute le serveur NGINX

```
[durian@web ~]$ sudo ss -lnpt | grep 80
LISTEN 0      511          0.0.0.0:80        0.0.0.0:*    users:(("nginx",pid=1648,fd=6),("nginx",pid=1647,fd=6))
LISTEN 0      511             [::]:80           [::]:*    users:(("nginx",pid=1648,fd=7),("nginx",pid=1647,fd=7))
```

☀️ Ouvrir ce port dans le firewall

```
[durian@web ~]$ sudo firewall-cmd --permanent --add-port=80/tcp
success
[durian@web ~]$ sudo firewall-cmd --reload
success
[durian@web ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3
  sources:
  services: cockpit dhcpv6-client ssh
  ports: 80/tcp
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

☀️ Visitez le site web !

```
[durian@web ~]$ curl http://10.6.2.11
<!doctype html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>HTTP Server Test Page powered by: Rocky Linux</title>
    <style type="text/css">
      /*<![CDATA[*/
```

☀️ Déterminer sur quel(s) port(s) écoute le service BIND9

```
[durian@dns ~]$ sudo ss -lnpt | grep 53
LISTEN 0      10         127.0.0.1:53        0.0.0.0:*    users:(("named",pid=2045,fd=22))
LISTEN 0      4096       127.0.0.1:953       0.0.0.0:*    users:(("named",pid=2045,fd=28))
LISTEN 0      10         10.6.2.12:53        0.0.0.0:*    users:(("named",pid=2045,fd=25))
LISTEN 0      10             [::1]:53           [::]:*    users:(("named",pid=2045,fd=27))
LISTEN 0      4096           [::1]:953          [::]:*    users:(("named",pid=2045,fd=29))
```

☀️ Ouvrir ce(s) port(s) dans le firewall

```
[durian@dns ~]$ sudo firewall-cmd --permanent --add-port=53/tcp
success
[durian@dns ~]$ sudo firewall-cmd --permanent --add-port=53/udp
success
[durian@dns ~]$ sudo firewall-cmd --reload
success
[durian@dns ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3
  sources:
  services: cockpit dhcpv6-client ssh
  ports: 53/tcp 53/udp
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

☀️ Effectuez des requêtes DNS manuellement depuis le serveur DNS lui-même dans un premier temps

```
[durian@dns ~]$ dig web.tp6.b1 @10.6.2.12
;; ANSWER SECTION:
web.tp6.b1.             86400   IN      A       10.6.2.11


[durian@dns ~]$ dig dns.tp6.b1 @10.6.2.12
;; ANSWER SECTION:
dns.tp6.b1.             86400   IN      A       10.6.2.12


[durian@dns ~]$ dig ynov.com @10.6.2.12
;; ANSWER SECTION:
ynov.com.               300     IN      A       172.67.74.226
ynov.com.               300     IN      A       104.26.10.233
ynov.com.               300     IN      A       104.26.11.233


[durian@dns ~]$ dig -x 10.6.2.11 @10.6.2.12
;; ANSWER SECTION:
11.2.6.10.in-addr.arpa. 86400   IN      PTR     web.tp6.b1.


[durian@dns ~]$ dig -x 10.6.2.12 @10.6.2.12
;; ANSWER SECTION:
12.2.6.10.in-addr.arpa. 86400   IN      PTR     dns.tp6.b1.
```

☀️ Effectuez une requête DNS manuellement depuis client1.tp6.b1

```
dorian@client1:~$ dig web.tp6.b1 @10.6.2.12
;; ANSWER SECTION:
web.tp6.b1.             86400   IN      A       10.6.2.11
```

☀️ Capturez une requête DNS et la réponse de votre serveur

```
J'ai comme IP .137 
C'est moi qui ai fait de la merde deso
Mais sinon tout est bon tkt
```

☀️ Créez un nouveau client client2.tp6.b1 vitefé

```
dorian@client2:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:3f:6f:f8 brd ff:ff:ff:ff:ff:ff
    inet 10.6.1.37/24 brd 10.6.1.255 scope global dynamic noprefixroute enp0s3
       valid_lft 493sec preferred_lft 493sec
    inet 10.6.1.38/24 brd 10.6.1.255 scope global secondary dynamic enp0s3
       valid_lft 599sec preferred_lft 599sec
    inet6 fe80::a00:27ff:fe3f:6ff8/64 scope link
       valid_lft forever preferred_lft forever
dorian@client2:~$ resolvectl
Global
         Protocols: -LLMNR -mDNS -DNSOverTLS DNSSEC=no/unsupported
  resolv.conf mode: stub

Link 2 (enp0s3)
    Current Scopes: DNS
         Protocols: +DefaultRoute -LLMNR -mDNS -DNSOverTLS DNSSEC=no/unsupported
Current DNS Server: 10.6.2.12
       DNS Servers: 10.6.2.12





dorian@client2:~$ curl http://web.tp6.b1
<!doctype html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>HTTP Server Test Page powered by: Rocky Linux</title>
    <style type="text/css">
      /*<![CDATA[*/
```

# BONUS
Je fais tout sur le client1


🌞 ping.py

```

dorian@client1:~$ cat ping.py
from scapy.all import *


ping = ICMP(type=8)


packet = IP(src="10.6.1.137", dst="10.6.1.254")


frame = Ether(src="08:00:27:c2:a9:42", dst="08:00:27:66:7b:b2")


final_frame = frame/packet/ping


answers, unanswered_packets = srp(final_frame, timeout=10)


print(f"Pong reçu : {answers[0]}")
dorian@client1:~$ sudo python3 ping.py
Begin emission
.*
Finished sending 1 packets

Received 2 packets, got 1 answers, remaining 0 packets
Pong reçu : QueryAnswer(query=<Ether  dst=08:00:27:66:7b:b2 src=08:00:27:c2:a9:42 type=IPv4 |<IP  frag=0 proto=icmp src=10.6.1.137 dst=10.6.1.254 |<ICMP  type=echo-request |>>>, answer=<Ether  dst=08:00:27:c2:a9:42 src=08:00:27:66:7b:b2 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=28 id=25524 flags= frag=0 ttl=64 proto=icmp chksum=0xff9a src=10.6.1.254 dst=10.6.1.137 |<ICMP  type=echo-reply code=0 chksum=0x0 id=0x0 seq=0x0 unused=b'' |<Padding  load=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>>)
```

🌞 dns_request.py

```
dorian@client1:~$ sudo python3 dns_request.py
Begin emission
........
Finished sending 1 packets
.....*
Received 14 packets, got 1 answers, remaining 0 packets
188.114.96.6
```

🌞 dhcp request.py

```
en sniffant grâce à un autre fichier:
from scapy.all import *
def dhcp_sniff_callback(packet):
    if packet.haslayer(DHCP):
        dhcp_options = packet[DHCP].options
        # Check for DHCP ACK (message type 5)
        if dhcp_options[0][1] == 5:  
            print("ACK reçu")
sniff(filter="udp port 67", prn=dhcp_sniff_callback, store=0)

On obtient:

dorian@client1:~$ sudo python3 dhcp_request.py
dorian@client1:~$ sudo python3 autrefichier.py 
ACK reçu
```

🌞 dhcp_starvation.py

```
Petit extrait de quand ça tourne (dans le dhcp bail, on voit bien que toutes les ip sont prises):

dorian@client1:~$ sudo python3 dhcp_starv.py 
Trying to occupy 10.6.1.128
NAK received
.
Sent 1 packets.
Trying to occupy 10.6.1.129
.NAK received
```

