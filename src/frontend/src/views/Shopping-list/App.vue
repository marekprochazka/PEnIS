<template>
  <div class="shoppingList__container">
    <v-card elevation="2" class="mt-5 pa-7">
      <h1 class="mt-3 mb-3">Nákupní seznam</h1>
      <ShoppingItemForm class="pa-4"/>
      <ShoppingList/>
    </v-card>
  </div>
</template>

<script>
import ShoppingList from '@/components/Shopping-list/Shopping-list'
import ShoppingItemForm from '@/components/Shopping-list/Shopping-item-form'

export default {
  name: 'Shopping-list',
  components: {
    ShoppingList,
    ShoppingItemForm
  }
}
</script>