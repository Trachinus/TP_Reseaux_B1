# SERVEUR WEB

🌞 Lister les ports en écoute sur la machine

```
[durian@web ~]$ sudo ss -lnpt | grep 80
LISTEN 0      511          0.0.0.0:80        0.0.0.0:*    users:(("nginx",pid=11274,fd=6),("nginx",pid=11273,fd=6))
LISTEN 0      511             [::]:80           [::]:*    users:(("nginx",pid=11274,fd=7),("nginx",pid=11273,fd=7))
```

🌞 Ouvrir le port dans le firewall de la machine


```
[durian@web ~]$ sudo firewall-cmd --permanent --add-port=80/tcp
success
[durian@web ~]$ sudo firewall-cmd --reload
success
```

🌞 Vérifier que ça a pris effet


- faites un ping vers sitedefou.tp7.b1
```
dorian@client1:~$ ping sitedefou.tp7.b1
PING sitedefou.tp7.b1 (10.7.1.11) 56(84) bytes of data.
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=1 ttl=64 time=1.13 ms
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=2 ttl=64 time=0.872 ms
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=3 ttl=64 time=1.02 ms
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=4 ttl=64 time=0.839 ms
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=5 ttl=64 time=1.15 ms
^C
--- sitedefou.tp7.b1 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4072ms
rtt min/avg/max/mdev = 0.839/1.001/1.152/0.128 ms
```

- visitez http://sitedefou.tp7.b1
```
dorian@client1:~$ curl http://sitedefou.tp7.b1
meow !
```

🌞 Voir la connexion établie

```
dorian@client1:~$ sudo ss -npt
State     Recv-Q     Send-Q               Local Address:Port               Peer Address:Port     Process
ESTAB     0          0                       10.7.1.101:60570            192.229.221.95:80        users:(("firefox",pid=11187,fd=134))
ESTAB     0          0                       10.7.1.101:60576            192.229.221.95:80        users:(("firefox",pid=11187,fd=135))
ESTAB     0          0                       10.7.1.101:54994              2.16.149.148:80        users:(("firefox",pid=11187,fd=127))
ESTAB     0          0                       10.7.1.101:47224            34.120.208.123:443       users:(("firefox",pid=11187,fd=101))
ESTAB     0          0                       10.7.1.101:55016              2.16.149.148:80        users:(("firefox",pid=11187,fd=129))
ESTAB     0          0                       10.7.1.101:50172             34.107.221.82:80        users:(("firefox",pid=11187,fd=99))
ESTAB     0          0                       10.7.1.101:50180             34.107.221.82:80        users:(("firefox",pid=11187,fd=113))
ESTAB     0          0                       10.7.1.101:53876             34.107.243.93:443       users:(("firefox",pid=11187,fd=138))
ESTAB     0          0                       10.7.1.101:55006              2.16.149.148:80        users:(("firefox",pid=11187,fd=128))
```

🌞 Lister les ports en écoute sur la machine

```
[durian@web ~]$ sudo ss -lnpt | grep 443
LISTEN 0      511        10.7.1.11:443       0.0.0.0:*    users:(("nginx",pid=11368,fd=6),("nginx",pid=11367,fd=6))
```

🌞 Gérer le firewall

```
[durian@web ~]$ sudo firewall-cmd --permanent --remove-port=80/tcp
success
[durian@web ~]$ sudo firewall-cmd --permanent --add-port=443/tcp
success
[durian@web ~]$ sudo firewall-cmd --reload
success
```

# SERVEUR VPN

🌞 Prouvez que vous avez bien une nouvelle carte réseau wg0

```
[durian@vpn ~]$ ip a
4: wg0: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state UNKNOWN group default qlen 1000
    link/none
    inet 10.7.200.1/24 scope global wg0
       valid_lft forever preferred_lft forever
```

🌞 Déterminer sur quel port écoute Wireguard

```
[durian@vpn ~]$ sudo ss -lnpu | grep 51820
UNCONN 0      0            0.0.0.0:51820      0.0.0.0:*
UNCONN 0      0               [::]:51820         [::]:*
```

🌞 Ouvrez ce port dans le firewall

```
[durian@vpn ~]$ sudo firewall-cmd --permanent --add-port=51820/udp
success
[durian@vpn ~]$ sudo firewall-cmd --reload
success
```

🌞 Ping ping ping !

```
dorian@client1:~$ ping 10.7.200.1
PING 10.7.200.1 (10.7.200.1) 56(84) bytes of data.
64 bytes from 10.7.200.1: icmp_seq=1 ttl=64 time=2.75 ms
64 bytes from 10.7.200.1: icmp_seq=2 ttl=64 time=1.22 ms
64 bytes from 10.7.200.1: icmp_seq=3 ttl=64 time=1.49 ms
^C
--- 10.7.200.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2245ms
rtt min/avg/max/mdev = 1.224/1.819/2.749/0.665 ms
```

🌞 Prouvez que vous avez toujours un accès internet

```
dorian@client1:~$ traceroute 1.1.1.1
traceroute to 1.1.1.1 (1.1.1.1), 30 hops max, 60 byte packets
 1  _gateway (10.7.200.1)  2.100 ms  3.178 ms  3.170 ms
 2  _gateway (10.7.1.254)  3.157 ms  4.428 ms  4.425 ms
 3  10.0.2.2 (10.0.2.2)  4.417 ms  5.006 ms  5.004 ms
```

🌞 Visitez le service Web à travers le VPN

```
dorian@client1:~$ curl https://sitedefou.tp7.b1 -k
meow !
```