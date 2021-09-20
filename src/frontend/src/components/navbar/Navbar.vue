<template>
  <v-navigation-drawer
      dark
      permanent
      expand-on-hover
      color="primary"
      app
      bottom
      v-model="toggle"
  >
    <v-list
        nav
        dense
    >
      <v-list-item link @click="toggle =!toggle ">
        <v-list-item-icon>
          <v-icon>mdi-menu</v-icon>
        </v-list-item-icon>
        <v-list-item-title>
          Menu
        </v-list-item-title>
      </v-list-item>
      <v-list-item link v-for="item in navItems" :key="item.route" @click="$router.push({name:item.route})">
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-title>
          {{ item.text }}
        </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>

export default {
  name: 'nav-bar',
  data() {
    return {
      toggle: true,
      navItems: [
        {
          icon: 'mdi-folder',
          text: 'TEST',
          route: 'Test'
        }
      ]

    }
  },

}
</script>