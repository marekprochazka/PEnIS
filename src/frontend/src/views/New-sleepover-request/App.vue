<template>
  <div class="NewSleepoverRequest__container">
    <v-card elevation="2" class="mt-5 pa-7">
      <h1 class="mt-3 mb-3">Nová žádost o návštěvu</h1>
      <NewSleepoverRequestForm/>
    </v-card>
  </div>
</template>


<script>
import NewSleepoverRequestForm from '@/components/New-sleepover-request/New-sleepover-request-form'

export default {
  name: 'New-sleepover-request',
  components: {
    NewSleepoverRequestForm
  }
}
</script>