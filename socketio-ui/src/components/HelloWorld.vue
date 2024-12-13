<template>
  <v-container class="fill-height">
    <v-responsive
      class="align-center fill-height mx-auto"
      max-width="900"
    >
      <div class="text-center">
        <v-btn text="Get Hello" @click="getHello()"></v-btn>
        {{ helloResponse }}
      </div>
      <div class="text-center" style="margin-top: 15px;">
        <v-btn text="Get Site Layout" @click="getSiteLayout()"></v-btn>
        {{ siteLayoutResponse }}
      </div>

      <div class="text-center" style="margin-top: 30px;">
        <v-btn text="Clear Responses" @click="clear()"></v-btn>
      </div>
    </v-responsive>
  </v-container>
</template>

<script setup>
  import {storeToRefs} from 'pinia';
  import {useConnectionStore} from '@/store/connection';

  const connectionStore = useConnectionStore();

  const {
    helloResponse,
    siteLayoutResponse,
  } = storeToRefs(connectionStore);

  function getHello() {
    connectionStore.apiHello();
  }

  function getSiteLayout() {
    connectionStore.apiGetSiteLayout();
  }

  function clear() {
    helloResponse.value = '';
    siteLayoutResponse.value = '';
  }

</script>
