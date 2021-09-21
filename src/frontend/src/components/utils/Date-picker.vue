<template>
  <v-menu v-model="menu" offset-y :close-on-content-click="false">
    <template v-slot:activator="{ on }">
      <v-btn icon color="primary" elevation="0" v-on="on" small>
        <v-icon>mdi-calendar</v-icon>
      </v-btn>
    </template>
    <v-date-picker v-model="picker" @click="menu = false" :show-current="showCurrent" :allowed-dates="allowedDates"
                   locale="cs-CZ" :first-day-of-week="1"
                   v-bind="{...(showCurrent ? {showCurrent}:{}),...(allowedDates ? {allowedDates}: {})}"/>

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
        this.menu = false
        this.$emit('input', val)
      }
    }
  }
}

</script>