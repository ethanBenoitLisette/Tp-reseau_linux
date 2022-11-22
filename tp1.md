TP1 : Are you dead yet ?
Ce premier TP a pour objectif de vous familiariser avec les environnements GNU/Linux.
On va apprendre à quoi servent les commandes élémentaires comme cat, cd, ls... non c'est pas vrai, on va casser des machines d'abord. Hihi.
L'idée est de vous faire un peu expérimenter et explorer un OS GNU/Linux, par vous-mêmes dans un premier temps, autour d'un sujet qui ESSAIE (très fort) d'être ludique.

Munissez vous de :

votre créativité
votre meilleur moteur de recherche
une machine virtuelle GNU/Linux

p'tit snapshot ou clone de la VM avant de tout péter !





TP1 : Are you dead yet ?

I. Intro

II. Feu




I. Intro
Le but va être de péter la machine virtuelle.
Par "péter" on entend la rendre inutilisable :
➜ Si la machine boot même plus, c'est valide
➜ Si la machine boot, mais que en mode rescue, et qu'on peut pas rétablir, c'est valide
➜ Si la machine boot, mais que l'expérience utilisateur est tellement dégradée qu'on peut rien faire, c'est valide
Bref si on peut pas utiliser la machine normalement, c'est VA-LI-DE.


Le but c'est de casser l'OS ou le noyau en soit, ou surcharger les ressources matérielles (disque, ram, etc), ce genre de choses.
Pour rappel : parmi les principaux composants d'un OS on a :

un filesystem ou système de fichiers

des partitions quoi, des endroits où on peut créer des dossiers et des fichiers


des utilisateurs et des permissions

des processus

une stack réseau

genre des cartes réseau, avec des IP dessus, toussa


un shell pour que les humains puissent utiliser la machine

que ce soit une interface graphique (GUI) ou un terminal (CLI)


des devices ou périphériques

écran, clavier, souris, disques durs, etc.




Essayez de penser par vous-mêmes, de raisonner. Et pas direct Google "how to break a linux machine" comme des idiots. (quand je dis de pas faire un truc, il faut le faire, c'est genre la règle n°1. Mais réfléchissez un peu quand même avant de Google ça ou des trucs similaires)

Evidemment, tout doit être fait depuis le terminal, et vous faites ça avec l'OS que vous voulez (Ubuntu, Rocky, autres). Bien entendu, avec une VM.
Aucune contrainte d'utilisateur, vous pouvez utiliser l'utilisateur root ou la commande sudo pour tout ça.

II. Feu
🌞 Trouver au moins 4 façons différentes de péter la machine
 
 La première méthode est simple on reduit à 0 est ainsi la vm ne ce lance plus (elle compte mais je ferais en sorte d'en trouver 4 autre)

 la seconde méthode est un peu plus compliquer puisqu'il faut supprimer les fichier de boot 
 ```
 rm /boot/vmlinuz-0-rescue-cd7ef545548d4529aa60684a1eb8c2be.img
 rm /boot/vmlinuz-5.14.0-70.13.1.e19_0.x86_64
 ```
 pour la 3eme methode on continuer de tapper sur le boot sauf que cette fois on va le déplacer
 ```
 mv /boot/vmlinuz-0-rescue-cd7ef545548d4529aa60684a1eb8c2be.img /etc/
 mv /boot/vmlinuz-5.14.0-70.13.1.e19_0.x86_64 /etc/
 ```
 


