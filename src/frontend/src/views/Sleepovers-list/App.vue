<template>
  <div class="sleepoversList__container">
    <v-card elevation="2" class="mt-5 pa-7">
      <h1 class="mt-3 mb-3">Seznam návštěv</h1>
      <SleepoverRequestsTable/>
      <SleepoverRequestsCalendar class="mt-5"/>
    </v-card>
  </div>
</template>

<script>

import SleepoverRequestsTable from '@/components/Sleepover-list/Sleepover-requests-table'
import SleepoverRequestsCalendar from '@/components/Sleepover-list/Sleepover-requests-calendar'

export default {
  name: 'Sleepovers-list',
  components: {
    SleepoverRequestsTable,
    SleepoverRequestsCalendar
  }
}

</script>