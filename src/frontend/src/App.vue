<template>
  <v-app>
    <v-main>
      <Navbar />
      <router-view class="ma-4" />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import Navbar from '@/components/navbar/Navbar.vue'


export default Vue.extend({
  name: 'App',
  components: {
    Navbar
  }
});
</script>
