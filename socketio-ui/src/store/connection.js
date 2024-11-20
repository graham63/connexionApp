import { defineStore } from 'pinia';
import axios from 'axios'
import socket from '@/plugins/socket';

export const useConnectionStore = defineStore('connection', {
  state: () => ({
    socketConnected: false,
    helloResponse: '',
  }),

  actions: {
    // Socket actions
    connect() {
      if (!socket.connected) {
        socket.connect();
        console.log('Attempting socket connection...')
      }

      socket.on('connect', () => {
        console.log('----- Connected to Socket-----');
        this.socketConnected = true;
      });

      socket.on('disconnect', () => {
        console.log('----- Socket Disconnected-----');
        this.socketConnected = false;
      });

      socket.on('connect_error', (error) => {
        console.error('Connection error:', error)
      });
    },

    disconnect() {
      socket.disconnect();
    },

    async fetchHello() {
      try {
        const response = await axios.get('http://localhost:8080/hello');  // Replace with your Flask server URL
        this.helloResponse = response.data;  // Store the server's response
        console.log('GET /hello response:', response.data);
      } catch (error) {
        console.error('Error fetching /hello:', error);
      }
    },
  },
});
