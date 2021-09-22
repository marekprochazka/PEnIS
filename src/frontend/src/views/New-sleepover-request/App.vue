<template>
  <div class="NewSleepoverRequest__container">
    <h1 class="mt-3 mb-3">Žádost o přespání</h1>
    <NewSleepoverRequestForm/>
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