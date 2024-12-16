import { defineStore } from 'pinia';
import socket from '@/plugins/socket';
import {hello, get_site_layout} from '@/lib/api_register'

export const useConnectionStore = defineStore('connection', {
  state: () => ({
    socketConnected: false,
    helloResponse: '',
    siteLayoutResponse: '',
  }),

  actions: {
    // Socket actions
    connect() {
      if (!socket.connected) {
        socket.connect();
        console.log('Attempting socket connection...')
      }

      socket.on('connect', () => {
        console.log('----- Connected to Socket-----', socket.id);
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

    // This could probably also go in the connect function, but it might
    // be more clear what's happening if the listeners are initialized separately
    async initializeListeners() {
      socket.on('broadcast', (message) => {
        console.log('----- Received broadcast-----', message);
      });
    },

    disconnect() {
      socket.disconnect();
    },

    async apiHello() {
      try {
        const response = await hello();
        this.helloResponse = response;
        console.log('GET /hello response:', response);
      } catch (error) {
        console.error('Error fetching /hello:', error);
      }
    },

    async apiGetSiteLayout() {
      try {
        const response = await get_site_layout();
        this.siteLayoutResponse = response;
        console.log('GET /site/layout response:', response);
      } catch (error) {
        console.error('Error fetching /site/layout:', error);
      }
    },

    async testSocketio() {
      try {
        socket.emit('socketioTest', { message: 'Hello from the client' })
      } catch (error) {
        console.error('Error emitting socketio message:', error);
      }
    },

  },
});
