<template>
  <v-form ref="CashDueForm">
    <v-row>
      <v-col cols="12" md="3">
        <v-text-field v-model="formData.description" label="Popis" outlined/>
      </v-col>
      <v-col cols="12" md="3">
        <v-text-field v-model="formData.user" label="Koupil" outlined/>
      </v-col>
      <v-col>
        <v-text-field v-model="formData.money_amount" label="Dlužná částka" outlined/>
      </v-col>
      <v-col cols="12" md="3">
        <v-btn color="primary" type="submit" block>Přidat položku</v-btn>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>

import {createCashDueItem} from "@/components/Cash-due/api";

export default {
  name: 'Cash-due-form',
  data() {
    return {
      formData: {
        description: null,
        user: null,
        money_amount: null
      }
    }
  },
  methods: {
    sendData() {
      createCashDueItem(this.formData)
          .then(() => {
            this.$router.go()
          })
    }
  }
}
</script>