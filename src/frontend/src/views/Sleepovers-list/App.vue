<template>
  <div class="sleepoversList__container">
    <SleepoverRequestsTable />
    <SleepoverRequestsCalendar class="mt-5" />
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