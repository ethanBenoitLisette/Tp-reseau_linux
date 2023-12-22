const WebSocket = require('ws');

const uri = "ws://10.0.3.17:8888";
const socket = new WebSocket(uri);

socket.on('message', (message) => {
    console.log(`Serveur a reçu : ${message}`);
});

// Fonction pour envoyer un message au serveur
function sendMessage(message) {
    socket.send(message);
}

// Exemple d'utilisation
sendMessage("Hello from JavaScript!");
