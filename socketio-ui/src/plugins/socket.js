// src/plugins/socketPlugin.js
import { io } from "socket.io-client";

const URL = 'http://localhost:8080';


// Enable verbose socket.io logging
// localStorage.debug = '*socket.io-client:socket';

console.log("Using Pipeline socket: " + URL);

// Create a Socket.IO client instance
const socket = io(URL, {
    // Socket.IO client options
    autoConnect: true,
});


export default socket;
