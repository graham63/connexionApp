<template>
  <v-container class="fill-height">
    <v-responsive
      class="align-centerfill-height mx-auto"
      max-width="900"
    >
      <div class="text-center">
        {{ helloResponse }}
        <v-btn text="Get Hello" @click="getHello()"></v-btn>
      </div>
    </v-responsive>
  </v-container>
</template>

<script setup>
  import {storeToRefs} from 'pinia';
  import {useConnectionStore} from '@/store/connection';

  const connectionStore = useConnectionStore();

  const {helloResponse} = storeToRefs(connectionStore);

  function getHello() {
    connectionStore.fetchHello();
  }

</script>
