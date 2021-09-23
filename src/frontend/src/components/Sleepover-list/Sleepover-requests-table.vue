<template>
  <v-data-table
      :headers="headers"
      :items="data"
      :loading="loading"
  >
    <template v-slot:item.coitus="{ item }">
      <v-checkbox v-model="item.coitus" readonly/>
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

import {fetchSleepoverRequestList} from "@/components/New-sleepover-request/api";

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
      loading: true
    }
  },
  async mounted()  {
    await fetchSleepoverRequestList()
    .then(response => {
      this.data = response.data
    })
    this.loading = false;
  }
}
</script>