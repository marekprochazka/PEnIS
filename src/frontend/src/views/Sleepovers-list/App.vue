<template>
  <div class="sleepoversList__container">
    <SleepoverRequestsTable />
  </div>
</template>

<script>

import SleepoverRequestsTable from '@/components/Sleepover-list/Sleepover-requests-table'

export default {
  name: 'Sleepovers-list',
  components: {
    SleepoverRequestsTable
  }
}

</script>