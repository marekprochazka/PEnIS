<template>
  <div>
    <v-data-table
        :headers="headers"
        :items="data"
        :loading="loading"
        :server-items-length="dataLength"
    >
      <template v-slot:item.bought="{ item }">
        <v-checkbox v-model="item.bought" readonly/>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-btn v-if="!item.bought" color="primary" @click="setBought(item.id)" block>Koupeno</v-btn>
      </template>
    </v-data-table>
    <v-btn v-if="!boughtShown" @click="showBought" color="primary">Zobrazit koupené předměty</v-btn>
    <v-btn v-else @click="hideBought" color="primary">Zobrazit nekoupené předměty</v-btn>

  </div>

</template>

<script>

import {fetchShoppingList, updateShoppingItem} from "@/components/Shopping-list/api";

export default {
  name: 'Shopping-list-component',
  data() {
    return {
      headers: [
        {text: 'Popis', value: 'description', align: 'center'},
        {text: 'Množství', value: 'quantity', align: 'center'},
        {text: 'Naléhavost', value: 'urgency.description', align: 'center'},
        {text: 'Je koupeno', value: 'bought'},
        {text: '', value: 'actions'},
      ],
      data: [],
      loading: false,
      boughtShown: false
    }
  },
  async mounted() {
    await this.getData()
  },
  methods: {
    async getData(param) {
      this.loading = true
      await fetchShoppingList(param ? param : null)
          .then(response => {
            this.data = response.data
          })
      this.loading = false
    },
    async showBought() {
      await this.getData({bought: true})
      this.boughtShown = true
    },
    async hideBought() {
      await this.getData()
      this.boughtShown = false
    },
    setBought(id) {
      updateShoppingItem({bought: true}, id)
          .then(() => {
            this.$router.go()
          })
    }
  },

  computed: {
    dataLength() {
      return this.data.length
    }
  }
}
</script>