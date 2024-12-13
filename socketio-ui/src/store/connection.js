import { defineStore } from 'pinia';
import axios from 'axios'
import socket from '@/plugins/socket';
import { DefaultApi, SiteApi } from '@/lib/src';

// Base level functions in .yaml (/hello => DefaultApi)
const defaultApi = new DefaultApi();
defaultApi.basePath = 'http://localhost:8080'

// Each namespace in openapi.yaml has an api (/site/layout => SiteApi)
const siteApi = new SiteApi();


// Fixes error: "Refused to set unsafe header "User-Agent"
defaultApi.apiClient.defaultHeaders = {}

const callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};

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

    async apiHello() {
      try {
        const response = await defaultApi.hello();
        this.helloResponse = response;
        console.log('GET /hello response:', response);
      } catch (error) {
        console.error('Error fetching /hello:', error);
      }
    },
    async apiGetSiteLayout() {
      try {
        const response = await siteApi.getSiteLayout();
        this.siteLayoutResponse = response;
        console.log('GET /site/layout response:', response);
      } catch (error) {
        console.error('Error fetching /site/layout:', error);
      }
    },
  },
});
