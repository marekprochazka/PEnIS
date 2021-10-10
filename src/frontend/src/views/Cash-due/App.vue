<template>
  <div>
    <CashDueForm class="pa-4" />
    <CashDue />
  </div>
</template>

<script>
import CashDue from '@/components/Cash-due/Cash-due'
import CashDueForm from '@/components/Cash-due/Cash-due-form'

export default {
  name: "Cash-due",
  components: {
    CashDue,
    CashDueForm
  }
}
</script>