
TP1 : Maîtrise réseau du poste

I. Basics
II. Go further
III. Le requin


I. Basics

Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ Carte réseau WiFi
Déterminer...

l'adresse MAC de votre carte WiFi

l'adresse IP de votre carte WiFi

le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi

en notation CIDR, par exemple /16
```
PS C:\WINDOWS\system32> ipconfig /all
```
```
   Adresse physique . . . . . . . . . . . : 7C-B5-66-B2-82-0C
   Adresse IPv4. . . . . . . . . . . . . .: 192.168.43.215
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0/24

```





☀️ Déso pas déso

l'adresse de réseau du LAN auquel vous êtes connectés en WiFi
l'adresse de broadcast
le nombre d'adresses IP disponibles dans ce réseau

```
 réseau. . . . . . . . . : 192.168.43.0
broadcast. . . . . . . . : 192.168.43.255
254
```


☀️ Hostname

```
PS C:\WINDOWS\system32> ipconfig /all
```
```
   Nom de l’hôte . . . . . . . . . . : ethanBL
```

☀️ Passerelle du réseau

l'adresse IP de la passerelle du réseau
l'adresse MAC de la passerelle du réseau
```
PS C:\WINDOWS\system32> ipconfig /all
```
```
   Passerelle par défaut. . . . . . . . . : 192.168.43.150
```
```
PS C:\WINDOWS\system32> arp -a
```
```
Interface : 192.168.43.215 --- 0xc
  Adresse Internet      Adresse physique      Type
  192.168.43.150        a2-3e-22-7a-12-4f     dynamique
```

☀️ Serveur DHCP et DNS

l'adresse IP du serveur DHCP qui vous a filé une IP

l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet
```
PS C:\WINDOWS\system32> ipconfig /all
```
```
    Serveur DHCP . . . . . . . . . . . . . : 192.168.43.150
    Serveurs DNS. . .  . . . . . . . . . . : 192.168.43.150
```



☀️ Table de routage
Déterminer...

dans votre table de routage, laquelle est la route par défaut
```
   Adresse IPv4. . . . . . . . . . . . . .: 192.168.43.215(préféré)
```



II. Go further

Toujours tout en ligne de commande.


☀️ Hosts ?

faites en sorte que pour votre PC, le nom b2.hello.vous corresponde à l'IP 1.1.1.1
```
PS C:\WINDOWS\system32> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=12 ms TTL=57
```



Vous pouvez éditer en GUI, et juste me montrer le contenu du fichier depuis le terminal pour le compte-rendu.


☀️ Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...
```
PS C:\Users\Ethan> netstat -aon
  Proto  Adresse locale         Adresse distante       État
  TCP    192.168.1.23:49695     20.199.120.85:443      ESTABLISHED     5136
  ```


☀️ Requêtes DNS
Déterminer...

```
PS C:\Users\Ethan> netstat -aon
  Proto  Adresse locale         Adresse distante       État
  TCP    192.168.43.215:51106   104.18.131.236:https   ESTABLISHED     8860
 [chrome.exe]
 ```


Ca s'appelle faire un "lookup DNS".


à quel nom de domaine correspond l'IP 174.43.238.89
```
PS C:\WINDOWS\system32> ping -a 174.43.238.89

Envoi d’une requête 'ping' sur 89.sub-174-43-238.myvzw.com [174.43.238.89] avec 32 octets de données :
```

☀️ Hop hop hop
Déterminer...

par combien de machines vos paquets passent quand vous essayez de joindre www.ynov.com



☀️ IP publique
Déterminer...

l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)
```
$ ipconfig
Carte reseau sans fil Wi-Fi:

   Passerelle par défaut. . . . . . . . . : 192.168.43.43

```


☀️ Scan réseau
Déterminer...

combien il y a de machines dans le LAN auquel vous êtes connectés

```
$ arp -a
Interface▒: 192.168.43.215 --- 0xe
  Adresse Internet      Adresse physique      Type
  192.168.43.43         b6-d3-e9-da-f2-f0     dynamique
  192.168.43.255        ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique


```



III. Le requin
Faites chauffer Wireshark. Pour chaque point, je veux que vous me livrez une capture Wireshark, format .pcap donc.
Faites clean 🧹, vous êtes des grands now :

livrez moi des captures réseau avec uniquement ce que je demande et pas 40000 autres paquets autour

vous pouvez sélectionner seulement certains paquets quand vous enregistrez la capture dans Wireshark


stockez les fichiers .pcap dans le dépôt git et côté rendu Markdown, vous me faites un lien vers le fichier, c'est cette syntaxe :





☀️ Capture ARP

[Lien vers capture ARP](./captures/arp.pcap)
filtre utilisé "arp"

☀️ Capture DNS


[Lien vers capture DNS](./captures/dns.pcap)
filtre utilisé "dns"


☀️ Capture TCP


[Lien vers capture TCP](./captures/tcp.pcap)
filtre utilisé "tcp.port == 443"



Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.




Je sais que je vous l'ai déjà servi l'an dernier lui, mais j'aime trop ce meme hihi 🐈