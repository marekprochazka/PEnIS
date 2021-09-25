<template>
<div class="sleepoverRequestsCalendar__container">
  <v-calendar
   ref="calendar"
   v-model="value"
   :weekdays="weekday"
   locale="cs-CZ"

  >

  </v-calendar>
</div>
</template>

<script>

export default {
  name: 'Sleepover-request-calendar',
  data() {
    return {
      value:"",
      weekday: [0,1,2,3,4,5,6]
    }
  }

}
</script>