1. Premiers pas
🌞 sleep_and_print.py

écrire une fonction qui compte jusqu'à 10, affiche l'entier, et sleep 0.5 secondes entre chaque print
appeler deux fois la fonction


Le code va exécuter la première fonction (~5 secondes) puis la deuxième (à nouveau ~5 secondes) pour un total de ~10 secondes d'exécution. Pas de surprises.

🌞 sleep_and_print_async.py

version asynchrone

la fonction doit être une fonction asynchrone
vous l'appelez toujours deux fois à la fin du script


utilisez la mécanique de loop de asyncio



Dès que l'exécution de la première fonction commencera à produire de l'attente, l'exécution de la deuxième commencera.


2. Web Requests
🌞 web_sync.py

on peut l'appeler comme ça : python web_sync.py https://www.ynov.com

````
[root@localhost TP6]# python web_sync.py https://www.ynov.com
Contenu écrit avec succès dans le fichier : /tmp/web_page
````

🌞 web_async.py

pareil mais en asynchrone

utilisez bien aiohttp pour faire la requête web
et aiofiles pour l'écriture sur disque
référez-vous au cours sur l'asynchrone pour la syntaxe


les deux fonctions imposées précédemment doivent être converties en asynchrone
pas de loop utilisez la syntaxe moderne avec gather()



Ici on a deux appels qui peuvent générer de l'attente : la requête HTTP, et l'écriture sur le disque. L'un comme l'autre sont sujet à produire des temps d'attente, temps pendant lesquels Python pourra décider d'aller exécuter autre chose. L'asynchrone donc.

🌞 web_sync_multiple.py

synchrone (PAS asynchrone)
pareil web_sync.py que mais le script prend en argument un fichier qui contient une liste d'URL
il stocke le résultat dans /tmp/web_<URL> où l'URL c'est par exemple www.ynov.com (il faudra enlever le https:// devant car on peut pas mettre de / dans un nom de fichier)

🌞 web_async_multiple.py

version asynchrone de web_sync_multiple.py

pas de loop utilisez la syntaxe moderne avec gather()


🌞 Mesure !

utilisez la technique de votre choix pour chronométrer le temps d'exécution du script
comparez les deux pour par exemple 10 URLs passées en argument