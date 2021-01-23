var { spawn } = require('child_process');
var processes = [];
var ip = "localhost";
var port = 25565;
for(var i = 0; i < 25; i++) {
    spawnBot(i);
}

function spawnBot(id) {
    var proc = spawn("node", ["bot.js",i,ip,port]);
    proc.stdout.on('data', (data) => {
        console.log(`[BOT ${id}] ${data}`);
    });
}