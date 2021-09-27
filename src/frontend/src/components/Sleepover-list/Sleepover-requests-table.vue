<template>
  <v-data-table
      :headers="headers"
      :items="data"
      :loading="loading"
      :server-items-length="dataLength"
  >
    <template v-slot:item.coitus="{ item }">
      <span>{{getCoitusText(item)}}</span>
    </template>
    <template v-slot:item.accepted="{ item }">
      <v-checkbox v-model="item.accepted" readonly/>
    </template>
    <template v-slot:item.accept_action="{ item }">
      <v-btn block color="primary" v-if="!item.accepted" @click="item.accepted=true">Schválit</v-btn>
      <v-btn block color="primary" v-else-if="item.accepted" @click="item.accepted=false">Zrušit</v-btn>
    </template>

  </v-data-table>

</template>

<script>

import {fetchSleepoverRequestList} from "@/components/Sleepover-list/api";

export default {
  name: 'Sleepover-requests-table',
  data() {
    return {
      headers: [
        {text: 'Jméno žadatele', value: 'requester_name', align: 'center'},
        {text: 'Datum od', value: 'sleepover_date_from', align: 'center'},
        {text: 'Datum do', value: 'sleepover_date_to', align: 'center'},
        {text: 'Počet osob', value: 'num_persons', align: 'center'},
        {text: 'Bude sex', value: 'coitus'},
        {text: 'Schváleno', value: 'accepted'},
        {text: 'Proces schválení', value: 'accept_action', align: 'center'},
      ],
      data: [],
      loading: true,
      dataLength: null,
    }
  },
  async mounted()  {
    await fetchSleepoverRequestList()
    .then(response => {
      this.data = response.data
      this.dataLength = this.data.length
    })
    this.loading = false;
  },
  methods: {
    getCoitusText(item) {
      if (item.coitus) {
        return item.coitus_probability ? item.coitus_probability.description_alt: 'Ano'
      } return 'Ne'
    }
  }
}
</script>