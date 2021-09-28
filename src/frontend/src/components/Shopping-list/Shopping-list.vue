<template>
  <v-data-table
      :headers="headers"
      :items="data"
      :loading="loading"
      :server-items-length="dataLength"
  >

  </v-data-table>
</template>

<script>

import {fetchShoppingList} from "@/components/Shopping-list/api";

export default {
  name: 'Shopping-list-component',
  data() {
    return {
      headers: [
        {text: 'Popis', value: 'description', align: 'center'},
        {text: 'Množství', value: 'quantity', align: 'center'},
        {text: 'Naléhavost', value: 'urgency.description', align: 'center'},
        {text: 'Je koupeno', value: 'bought', align: 'center'},
        {text: '', value: 'actions'},
      ],
      data: [],
      loading: false
    }
  },
  async mounted() {
    this.loading = true
    await fetchShoppingList()
    .then(response => {
      this.data = response.data
    })
    this.loading = false
  },

  computed: {
    dataLength() {
      return this.data.length
    }
  }
}
</script>