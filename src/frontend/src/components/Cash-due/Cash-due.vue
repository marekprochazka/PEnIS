<template>
  <div>
    <v-data-table
        :headers="headers"
        :items="data"
        :loading="loading">
      <template v-slot:item.paid-back="{item}">
        <v-checkbox v-model="item.paid_back" readonly/>
      </template>
      <template v-slot:item.actions="{item}">
        <v-btn v-if="!item.paid_back" color="primary" @click="setPaidBack(item.id)" block>Zaplaceno</v-btn>
      </template>
    </v-data-table>
    <v-btn v-if="!paidBackShown" @click="showPaidBack" color="primary">Zobrazit zaplacené předměty</v-btn>
    <v-btn v-else @click="hidePaidBack" color="primary">Zobrazit nezaplacené předměty</v-btn>
  </div>
</template>

<script>

import {fetchCashDueList, updateCashDueItem} from "@/components/Cash-due/api";

export default {
  name: "Cash-due-component",
  data() {
    return {
      headers: [
        {text: 'Popis', value: 'description', align: 'center'},
        {text: 'Koupil', value: 'user', align: 'center'},
        {text: 'Dlužná částka', value: 'money_amount', align: 'center'},
        {text: 'Je zaplaceno', value: 'paid_back'},
        {text: '', value: 'actions'},
      ],
      data: [],
      loading: false,
      paidBackShown: false
    }
  },
  async mounted() {
    await this.getData()
  },
  methods: {
    async getData(param) {
      this.loading = true
      await fetchCashDueList(param ? param : null)
          .then(response => {
            this.data = response.data
          })
      this.loading = false
    },
    async showPaidBack() {
      await this.getData({paid: true})
      this.paidBackShown = true
    },
    async hidePaidBack() {
      await this.getData()
      this.paidBackShown = false
    },
    setPaidBack(id) {
      updateCashDueItem({paid_back: true}, id)
          .then(() => {
            this.$router.go()
          })
    }
  }
}
</script>