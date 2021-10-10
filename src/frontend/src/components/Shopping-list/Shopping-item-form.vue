<template>
  <v-form ref="ShoppingItemForm" @submit.prevent="sendData">
    <v-row>
      <v-col
          cols="12"
          md="3"
      >
        <v-text-field dense v-model="formData.description" label="Popis" outlined/>
      </v-col>
      <v-col
          cols="12"
          md="3"
      >
        <v-text-field dense v-model="formData.quantity" label="Množství" outlined/>
      </v-col>
      <v-col
          cols="12"
          md="3"
      >
        <v-select label="Naléhavost" outlined
                  v-model="formData.urgency"
                  :items="urgencies"
                  :item-text="value => value.description"
                  :item-value="value => value"
                  dense
        />
      </v-col>
      <v-col
          cols="12"
          md="3"
      >
        <v-btn color="primary" type="submit" block>Přidat položku</v-btn>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>

import {createShoppingItem, fetchUrgenciesList} from "@/components/Shopping-list/api";

export default {
  name: 'Shopping-item-form',
  data() {
    return {
      formData: {
        description: null,
        quantity: null,
        urgency: null
      },
      urgencies: []
    }
  },
  mounted() {
    fetchUrgenciesList()
        .then(response => {
          console.log(response)
          this.urgencies = response.data
        })
    console.log(this.urgencies)
  },
  methods: {
    sendData() {
      this.formData.urgency = this.formData.urgency.id
      createShoppingItem(this.formData)
          .then(() => {
            this.$router.go()
          })
    }
  }
}
</script>