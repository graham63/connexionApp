<template>
  <v-app>
    <v-main>
      <HelloWorld />
    </v-main>
  </v-app>
</template>

<script setup>
  import {onMounted} from 'vue';
  import {useConnectionStore} from '@/store/connection';
  import HelloWorld from '@/components/HelloWorld';
  const connectionStore = useConnectionStore();

  /* Connection */
  onMounted(() => {
    connectionStore.initializeListeners();
    connectionStore.connect();
  })

</script>
