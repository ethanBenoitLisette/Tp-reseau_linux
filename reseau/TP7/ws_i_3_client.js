const WebSocket = require('ws');

const uri = "ws://10.0.3.17:8888";
const socket = new WebSocket(uri);

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Choisissez un pseudo : ', (pseudo) => {
    socket.send(pseudo);

    rl.on('line', (userInput) => {
        if (userInput.toLowerCase() === 'exit') {
            rl.close();
        } else {
            socket.send(userInput);
        }
    });
});

socket.on('message', (message) => {
    console.log(message);
});

socket.on('close', () => {
    console.log("Connexion fermée par le serveur.");
    rl.close();
});
