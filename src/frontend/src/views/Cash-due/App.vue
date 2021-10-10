<template>
  <div>
    <v-card elevation="2" class="mt-5 pa-7">
      <h1 class="mt-3 mb-3">Dlužná hotovost</h1>
      <CashDueForm class="pa-4"/>
      <CashDue/>
    </v-card>
  </div>
</template>

<script>
import CashDue from '@/components/Cash-due/Cash-due-list'
import CashDueForm from '@/components/Cash-due/Cash-due-form'

export default {
  name: "Cash-due",
  components: {
    CashDue,
    CashDueForm
  }
}
</script>