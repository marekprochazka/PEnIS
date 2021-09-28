<template>
  <div class="shoppingList__container">
    <ShoppingList />
  </div>
</template>

<script>
import ShoppingList from '@/components/Shopping-list/Shopping-list'

export default {
  name:'Shopping-list',
  components: {
    ShoppingList
  }
}
</script>