<template>
  <v-app v-if="!$route.meta.loginRequired">
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
  <v-app v-else>
    <v-main>
      <!-- TODO NAVBAR -->
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'App',

  data: () => ({
    //
  }),
});
</script>
