<template>
  <v-menu v-model="menu" offset-y :close-on-content-click="false">
    <template v-slot:activator="{ on }">
      <v-btn icon color="primary" elevation="0" v-on="on" small>
        <v-icon>mdi-clock</v-icon>
      </v-btn>
    </template>
    <v-time-picker v-model="picker" format="24hr"/>
  </v-menu>

</template>

<script>
export default {
  props: {
    value: {type: String, default: new Date().toISOString().substr(0, 10)},
    showCurrent: {type: String, required: false},
    allowedDates: {type: Function, required: false}
  },
  data() {
    return {
      menu: false
    }
  },
  computed: {
    picker: {
      get() {
        return this.value
      },
      set(val) {
        this.$emit('input', val)
      }
    }
  }
}

</script>