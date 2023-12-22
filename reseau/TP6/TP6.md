Bien sûr, voici une présentation plus structurée avec une amélioration de la mise en forme en Markdown :

## 1. Premiers pas

### 🌞 **sleep_and_print.py**

[sleep_and_print.py](partie-2/sleep_and_print.py)

Le code va exécuter la première fonction (~5 secondes) puis la deuxième (à nouveau ~5 secondes) pour un total de ~10 secondes d'exécution. Pas de surprises.

### 🌞 **sleep_and_print_async.py**

[sleep_and_print_async.py](partie-2/sleep_and_print_async.py)

Dès que l'exécution de la première fonction commencera à produire de l'attente, l'exécution de la deuxième commencera.

## 2. Web Requests

### 🌞 **web_sync.py**

on peut l'appeler comme ça : `python web_sync.py https://www.ynov.com`

[web_sync.py](partie-2/web_sync.py)

### 🌞 **web_async.py**

[web_async.py](partie-2/web_async.py)

### 🌞 **web_sync_multiple.py**

[web_sync_multiple.py](partie-2/web_sync_multiple.py)

### 🌞 **web_async_multiple.py**

[web_async_multiple.py](partie-2/web_async_multiple.py)

### 🌞 **Mesure !**

```bash
[root@localhost TP6]# python web_sync_multiple.py urls.txt
Contenu écrit avec succès dans le fichier : /tmp/web_www.pokepedia.fr_
Contenu écrit avec succès dans le fichier : /tmp/web_www.ynov.com_
Contenu écrit avec succès dans le fichier : /tmp/web_www.monsterhunter.com_
Le programme a pris 2.08 secondes pour s'exécuter.

[root@localhost TP6]# python web_async_multiple.py urls.txt
Contenu écrit avec succès dans le fichier : /tmp/web_www.ynov.com_
Contenu écrit avec succès dans le fichier : /tmp/web_www.pokepedia.fr_
Contenu écrit avec succès dans le fichier : /tmp/web_www.monsterhunter.com_
Le programme a pris 0.35 secondes pour s'exécuter.
```

## 3. Chat

### 🌞 **chat_server_ii_2.py**

[chat_server_ii_2.py](partie-2/chat_server_ii_2.py)

### 🌞 **chat_client_ii_2.py**

[chat_server_ii_2.py](partie-2/chat_server_ii_2.py)

### 3.1. Client asynchrone

#### 🌞 **chat_client_ii_3.py**

[chat_server_ii_2.py](partie-2/chat_server_ii_2.py)

#### 🌞 **chat_server_ii_3.py**

[chat_server_ii_2.py](partie-2/chat_server_ii_2.py)

### 3.2. Un chat fonctionnel

#### 🌞 **chat_server_ii_4.py**

[chat_server_ii_4.py](partie-2/chat_server_ii_4.py)

### 3.3. Gérer des pseudos

#### 🌞 **chat_client_ii_5.py**

[chat_client_ii_5.py](partie-2/chat_client_ii_5.py)

Si vous avez encore le client qui envoie juste la string "Hello" à la connexion, enlevez-le ! Dès sa connexion, le client envoie donc un message contenant son pseudo. On peut utiliser ce savoir côté serveur : le premier message d'un client contient le pseudo.

#### 🌞 **chat_server_ii_5.py**

[chat_client_ii_5.py](partie-2/chat_client_ii_5.py)

### 3.4. Déconnexion

#### 🌞 **chat_server_ii_6.py et chat_client_ii_6.py**

côté client, si le serveur se déco

[chat_server_ii_6.py](partie-2/chat_server_ii_6.py)
[chat_client_ii_6.py](partie-2/chat_client_ii_6.py)

### Bonus

### 2. Logs

[chat_server_b-2.py](partie-3/chat_server_b-2.py)

### 6 Gestion d'historique

Quand tu rejoins la conversation en retard, t'as pas l'historique, relou. Gérer un historique de conversation.

#### 🌞 **chat_server_b-6.py**

[chat_server_b-6.py](partie-3/chat_server_b-6.py)

