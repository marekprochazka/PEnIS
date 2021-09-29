<template>
  <div class="shoppingList__container">
    <ShoppingItemForm class="pa-4" />
    <ShoppingList />
  </div>
</template>

<script>
import ShoppingList from '@/components/Shopping-list/Shopping-list'
import ShoppingItemForm from '@/components/Shopping-list/Shopping-item-form'

export default {
  name:'Shopping-list',
  components: {
    ShoppingList,
    ShoppingItemForm
  }
}
</script>