☀️ Capturez un échange DHCP complet

```
ipconfig /release
puis j'active la capture Wireshark et :
ipconfig /renew
```

☀️ Directement dans Wireshark, vous pouvez voir toutes les infos que vous donne  le serveur DHCP

```
Option: (50) Requested IP Address (192.168.1.39)
    Length: 4
    Requested IP Address: 192.168.1.39

Option: (3) Router
    Length: 4
    Router: 192.168.1.1


Option: (6) Domain Name Server
    Length: 4
    Domain Name Server: 192.168.1.1
```

