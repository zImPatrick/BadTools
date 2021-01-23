var mc = require('minecraft-protocol');
const POSITION_UPDATE_INTERVAL_MS = 50
console.log(process.argv[3]);
var client = mc.createClient({
  host: process.argv[3],   // optional
  port: parseInt(process.argv[4]),         // optional
  username: "Bottedes"+process.argv[2],
  version: "1.8.8"
});
var curX;
var curY;
var curZ;
client.on('position', function(packet) {
    curX = packet.x;
    curY = packet.y;
    curZ = packet.z;
});

setInterval(() => {
    if(curX == null || curY == null || curZ == null) return;
    var moveForward = Math.floor(Math.random() * Math.floor(6)) / 10;
    client.write("position_look", {
        yaw: 0,
        pitch: 0,
        x: curX,
        y: curY,
        z: curZ+moveForward,
        onGround: true
  });
  curZ += moveForward;
}, POSITION_UPDATE_INTERVAL_MS);

console.log("he")

exports.toNotchianYaw = yaw => toDegrees(PI - yaw)
exports.toNotchianPitch = pitch => toDegrees(-pitch)
exports.fromNotchianYawByte = yaw => fromNotchianYaw(yaw * FROM_NOTCH_BYTE)
exports.fromNotchianPitchByte = pitch => fromNotchianPitch(pitch * FROM_NOTCH_BYTE)