🌞 Prouvez que votre configuration est effective

```
PS C:\Users\doria> Get-NetIPAddress -InterfaceAlias Ethernet

IPAddress         : fe80::6196:783:38e3:50ef%17
InterfaceIndex    : 17
InterfaceAlias    : Ethernet
AddressFamily     : IPv6
Type              : Unicast
PrefixLength      : 64
PrefixOrigin      : WellKnown
SuffixOrigin      : Link
AddressState      : Preferred
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : 10.1.1.1
InterfaceIndex    : 17
InterfaceAlias    : Ethernet
AddressFamily     : IPv4
Type              : Unicast
PrefixLength      : 24
PrefixOrigin      : Manual
SuffixOrigin      : Manual
AddressState      : Preferred
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore
```

🌞 Tester que votre LAN + votre adressage IP est fonctionnel

```
PS C:\Users\doria> ping 10.1.1.2

Envoi d’une requête 'Ping'  10.1.1.2 avec 32 octets de données :
Réponse de 10.1.1.2 : octets=32 temps<1ms TTL=128
Réponse de 10.1.1.2 : octets=32 temps<1ms TTL=128
Réponse de 10.1.1.2 : octets=32 temps<1ms TTL=128
Réponse de 10.1.1.2 : octets=32 temps<1ms TTL=128

Statistiques Ping pour 10.1.1.2:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 0ms, Maximum = 0ms, Moyenne = 0ms
```

🌞 Sur le PC serveur

```
PS C:\Users\doria> ncat -l 69
```

🌞 Sur le PC serveur toujours

```
PS C:\WINDOWS\system32> netstat -a -n -b

Connexions actives

  Proto  Adresse locale         Adresse distante       État
  TCP    0.0.0.0:69             0.0.0.0:0              LISTENING
 [ncat.exe]
```

🌞 Sur le PC client

```
Hugo Goncalves est le client
```

🌞 Echangez-vous des messages

```
PS C:\Users\doria> ncat -l 69
je t'aime - Serveur
Moi aussi <3 - client
```

🌞 Utilisez une commande qui permet de voir la connexion en cours

```
  TCP    10.1.1.1:69            10.1.1.2:3546          ESTABLISHED
 [ncat.exe]
```

🌞 Inversez les rôles

```
🌞 Echangez-vous des messages

PS C:\Users\doria> ncat 10.1.1.2 6
t bo - client
Je sais <3 - Serveur

🌞 Utilisez une commande qui permet de voir la connexion en cours

 TCP    10.1.1.1:61904         10.1.1.2:6             ESTABLISHED
 [ncat.exe]
```

🌞 Pour les 5 applications

```
PS C:\WINDOWS\system32> netstat -a -n -b | Select-String Spotify -Context 1,0

    TCP    0.0.0.0:57621          0.0.0.0:0              LISTENING
>  [Spotify.exe]
    TCP    0.0.0.0:62474          0.0.0.0:0              LISTENING
>  [Spotify.exe]
    TCP    10.33.77.157:25522     35.186.224.24:443      ESTABLISHED
>  [Spotify.exe]
    TCP    10.33.77.157:62478     104.199.65.9:4070      ESTABLISHED
>  [Spotify.exe]
    TCP    10.33.77.157:62479     35.186.224.45:443      ESTABLISHED
>  [Spotify.exe]
    TCP    10.33.77.157:62603     35.186.224.41:443      ESTABLISHED
>  [Spotify.exe]
    UDP    0.0.0.0:49826          35.186.224.24:443
```
Spotify se connecte donc à plusieurs adresses IP, par ex : 35.186.224.24 sur le port 443 (sur le pcap j'ai utilisé la connexion UDP pour filtrer)

```
PS C:\WINDOWS\system32> netstat -a -n -b | Select-String Firefox -Context 1,0

    TCP    10.33.77.157:26484     34.107.221.82:80       ESTABLISHED
>  [firefox.exe]
    TCP    10.33.77.157:26487     34.107.221.82:80       ESTABLISHED
>  [firefox.exe]
    TCP    10.33.77.157:26488     95.100.252.32:80       ESTABLISHED
>  [firefox.exe]
    TCP    10.33.77.157:26489     34.149.100.209:443     ESTABLISHED
>  [firefox.exe]
    TCP    10.33.77.157:26490     34.160.144.191:443     ESTABLISHED
>  [firefox.exe]
    TCP    10.33.77.157:26510     142.250.201.163:80     ESTABLISHED
```
Firefox se connecte donc à plusieurs adresses IP, par ex : 142.250.201.163 sur le port 80

```
PS C:\WINDOWS\system32> netstat -a -n -b | Select-String Discord -Context 1,0

    TCP    10.33.77.157:62466     162.159.130.234:443    ESTABLISHED
>  [Discord.exe]
    TCP    127.0.0.1:6463         0.0.0.0:0              LISTENING
>  [Discord.exe]
    UDP    0.0.0.0:58441          162.159.135.232:443
>  [Discord.exe]
```
Discord se connecte donc à plusieurs adresses IP, par ex : 162.159.130.234 sur le port 443

```
PS C:\WINDOWS\system32> netstat -a -n -b | Select-String Epic -Context 1,0

    TCP    10.33.77.157:9190      34.204.142.47:443      ESTABLISHED
>  [EpicGamesLauncher.exe]
    TCP    10.33.77.157:9192      184.72.165.52:443      ESTABLISHED
>  [EpicGamesLauncher.exe]
    TCP    10.33.77.157:9193      184.72.165.52:443      ESTABLISHED
>  [EpicGamesLauncher.exe]
    TCP    10.33.77.157:9195      184.72.165.52:443      ESTABLISHED
```
Epic Games se connecte donc à plusieurs adresses IP, par ex : 34.204.142.47 sur le port 443

```
PS C:\WINDOWS\system32> netstat -a -n -b | Select-String Xbox -Context 1,0

    TCP    10.33.77.157:9503      40.86.103.106:443      ESTABLISHED
>  [XboxPcAppFT.exe]
    TCP    10.33.77.157:9504      13.107.246.42:443      ESTABLISHED
>  [XboxPcAppFT.exe]
    TCP    10.33.77.157:9505      104.115.88.8:443       ESTABLISHED
>  [XboxPcApp.exe]
    TCP    10.33.77.157:9506      104.115.88.8:443       ESTABLISHED
```
L'Xbox app se connecte donc à plusieurs adresses IP, par ex : 40.86.103.106 sur le port 443