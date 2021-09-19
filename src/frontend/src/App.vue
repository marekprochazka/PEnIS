<template>
  <v-app>
    <v-main>
      <!-- TODO NAVBAR -->
      <p>{{test}}</p>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import reverse from 'django-reverse'

export default Vue.extend({
  name: 'App',
  computed: {
    test() {
      return reverse('core:test')
    }
  },

  data: () => ({
    //
  }),
});
</script>
