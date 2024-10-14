☀️ Uniquement avec des commandes, prouvez-que :

- vous avez bien configuré les adresses IP demandées (un ip a suffit hein)

```
dorian@client1:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:25:26:52 brd ff:ff:ff:ff:ff:ff
    inet 10.5.1.11/24 brd 10.5.1.255 scope global enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe25:2652/64 scope link
       valid_lft forever preferred_lft forever


dorian@client2:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:92:4d:ba brd ff:ff:ff:ff:ff:ff
    inet 10.5.1.12/24 brd 10.5.1.255 scope global enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe92:4dba/64 scope link
       valid_lft forever preferred_lft forever


[durian@routeur ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:06:a6:d3 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute enp0s3
       valid_lft 85164sec preferred_lft 85164sec
    inet6 fe80::a00:27ff:fe06:a6d3/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:8c:95:ed brd ff:ff:ff:ff:ff:ff
    inet 10.5.1.254/24 brd 10.5.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe8c:95ed/64 scope link
       valid_lft forever preferred_lft forever
```

- tout le monde peut se ping au sein du réseau 10.5.1.0/24

```
PS C:\Users\doria> ping 10.5.1.254

Envoi d’une requête 'Ping'  10.5.1.254 avec 32 octets de données :
Réponse de 10.5.1.254 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.254 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.254 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.254 : octets=32 temps<1ms TTL=64

Statistiques Ping pour 10.5.1.254:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 0ms, Maximum = 0ms, Moyenne = 0ms
PS C:\Users\doria> ping 10.5.1.11

Envoi d’une requête 'Ping'  10.5.1.11 avec 32 octets de données :
Réponse de 10.5.1.11 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.11 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.11 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.11 : octets=32 temps<1ms TTL=64

Statistiques Ping pour 10.5.1.11:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 0ms, Maximum = 0ms, Moyenne = 0ms
PS C:\Users\doria> ping 10.5.1.12

Envoi d’une requête 'Ping'  10.5.1.12 avec 32 octets de données :
Réponse de 10.5.1.12 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.12 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.12 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.12 : octets=32 temps<1ms TTL=64

Statistiques Ping pour 10.5.1.12:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 0ms, Maximum = 0ms, Moyenne = 0ms
```

- vous avez bien configuré les hostnames demandés

```
dorian@client1:~$ sudo hostnamectl
[sudo] password for dorian:
Sorry, try again.
[sudo] password for dorian:
 Static hostname: client1.tp5.b1
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 44ae4d4fdf3a4d60aed1f8eb465a73c6
         Boot ID: 24892bc1afa0452180b81f21eae7f1a1
  Virtualization: oracle
Operating System: Ubuntu 24.04.1 LTS
          Kernel: Linux 6.8.0-45-generic
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Firmware Version: VirtualBox
   Firmware Date: Fri 2006-12-01
    Firmware Age: 17y 10month 1w 6d


dorian@client2:~$ sudo hostnamectl
[sudo] password for dorian:
 Static hostname: client2.tp5.b1
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 44ae4d4fdf3a4d60aed1f8eb465a73c6
         Boot ID: 32716e741362454fa4803b39927399b9
  Virtualization: oracle
Operating System: Ubuntu 24.04.1 LTS
          Kernel: Linux 6.8.0-45-generic
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Firmware Version: VirtualBox
   Firmware Date: Fri 2006-12-01
    Firmware Age: 17y 10month 1w 6d


[durian@routeur ~]$ sudo hostnamectl
[sudo] password for durian:
 Static hostname: routeur.tp5.b1
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 66a7dc15545f45b09ebc58c3364b5d02
         Boot ID: b955bc8ca0954b878907474976188eb0
  Virtualization: oracle
Operating System: Rocky Linux 9.4 (Blue Onyx)
     CPE OS Name: cpe:/o:rocky:rocky:9::baseos
          Kernel: Linux 5.14.0-427.13.1.el9_4.x86_64
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Firmware Version: VirtualBox
```

☀️ Déjà, prouvez que le routeur a un accès internet

```
PING google.com (216.58.214.174) 56(84) bytes of data.
64 bytes from mad01s26-in-f14.1e100.net (216.58.214.174): icmp_seq=1 ttl=109 time=25.8 ms
64 bytes from mad01s26-in-f14.1e100.net (216.58.214.174): icmp_seq=2 ttl=109 time=28.5 ms
```

☀️ Activez le routage

```
[durian@routeur ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources:
  services: cockpit dhcpv6-client ssh
  ports:
  protocols:
  forward: yes
  masquerade: yes
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

☀️ Prouvez que les clients ont un accès internet

```
dorian@client1:~$ ping google.com
PING google.com (172.217.18.206) 56(84) bytes of data.
64 bytes from par10s38-in-f14.1e100.net (172.217.18.206): icmp_seq=1 ttl=109 time=51.8 ms
64 bytes from par10s38-in-f14.1e100.net (172.217.18.206): icmp_seq=2 ttl=109 time=41.2 ms
64 bytes from par10s38-in-f14.1e100.net (172.217.18.206): icmp_seq=3 ttl=109 time=46.7 ms


dorian@client2:~$ ping google.com
PING google.com (172.217.20.206) 56(84) bytes of data.
64 bytes from par10s50-in-f14.1e100.net (172.217.20.206): icmp_seq=1 ttl=108 time=58.6 ms
64 bytes from par10s50-in-f14.1e100.net (172.217.20.206): icmp_seq=2 ttl=108 time=80.7 ms
64 bytes from par10s50-in-f14.1e100.net (172.217.20.206): icmp_seq=3 ttl=108 time=45.3 ms
```

☀️ Montrez-moi le contenu final du fichier de configuration de l'interface réseau

```
dorian@client2:~$ sudo cat /etc/netplan/01-netcfg.yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: no
      addresses: [10.5.1.12/24]
      gateway4: 10.5.1.254
      nameservers:
        addresses: [1.1.1.1]
```

☀️ Sur routeur.tp5.b1, déterminer sur quel port écoute le serveur SSH

```
[durian@routeur ~]$ sudo ss -lnpt | grep 22
LISTEN 0      128          0.0.0.0:22        0.0.0.0:*    users:(("sshd",pid=698,fd=3))
LISTEN 0      128             [::]:22           [::]:*    users:(("sshd",pid=698,fd=4))
```

☀️ Sur routeur.tp5.b1, vérifier que ce port est bien ouvert

```
[durian@routeur ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources:
  services: cockpit dhcpv6-client ssh
  ports:
  protocols:
  forward: yes
  masquerade: yes
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
[durian@routeur ~]$ cat /etc/services| grep ssh
ssh             22/tcp                          # The Secure Shell (SSH) Protocol
ssh             22/udp                          # The Secure Shell (SSH) Protocol
```

☀️ Installez et configurez un serveur DHCP sur la machine routeur.tp5.b1

```
[durian@routeur ~]$ sudo dnf -y install dhcp-server
[durian@routeur ~]$ sudo nano /etc/dhcp/dhcpd.conf
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#

# default lease time
default-lease-time 600;
# max lease time
max-lease-time 7200;
# this DHCP server to be declared valid
authoritative;
# specify network address and subnetmask
subnet 10.5.1.0 netmask 255.255.255.0 {
    # specify the range of lease IP address
    range dynamic-bootp 10.5.1.137 10.5.1.237;
    # specify broadcast address
    option broadcast-address 10.5.1.255;
    # specify gateway
    option routers 10.5.1.254;

    option domain-name-servers 1.1.1.1;
}

sudo systemctl enable --now dhcpd
systemctl start dhcpd
```

☀️ Créez une nouvelle machine client client3.tp5.b1

- définissez son hostname

```
dorian@client3:~$ sudo hostnamectl
[sudo] password for dorian:
 Static hostname: client3.tp5.b1
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 44ae4d4fdf3a4d60aed1f8eb465a73c6
         Boot ID: 7fbd4671a90f4e34a70ff8cfb05c6260
  Virtualization: oracle
Operating System: Ubuntu 24.04.1 LTS
          Kernel: Linux 6.8.0-45-generic
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Firmware Version: VirtualBox
   Firmware Date: Fri 2006-12-01
    Firmware Age: 17y 10month 2w
```

- définissez une IP en DHCP

```
dorian@client3:~$ sudo cat /etc/netplan/01-netcfg.yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: yes
```

- vérifiez que c'est bien une adresse IP entre .137 et .237

```
dorian@client3:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:a0:86:f3 brd ff:ff:ff:ff:ff:ff
    inet 10.5.1.200/24 metric 100 brd 10.5.1.255 scope global dynamic enp0s3
       valid_lft 365sec preferred_lft 365sec
```

- prouvez qu'il a immédiatement un accès internet

```
dorian@client3:~$ ping google.com
PING google.com (172.217.20.206) 56(84) bytes of data.
64 bytes from waw02s08-in-f14.1e100.net (172.217.20.206): icmp_seq=1 ttl=112 time=45.1 ms
64 bytes from waw02s08-in-f14.1e100.net (172.217.20.206): icmp_seq=2 ttl=112 time=117 ms
64 bytes from waw02s08-in-f14.1e100.net (172.217.20.206): icmp_seq=3 ttl=112 time=71.2 ms
```