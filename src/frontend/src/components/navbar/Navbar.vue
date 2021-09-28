<template>
  <v-navigation-drawer
      dark
      permanent
      color="primary"
      app
      bottom
      :mini-variant="toggle"
  >
    <v-list
        nav
        dense
    >
      <v-list-item link @click="toggle = !toggle">
        <v-list-item-icon>
          <v-icon v-if="toggle">mdi-menu</v-icon>
          <v-icon v-else>mdi-close</v-icon>
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
          icon: 'mdi-home',
          text: 'Domů',
          route: 'Home'
        },
        {
          icon: 'mdi-calendar-plus',
          text: 'Nová žádost o pobyt',
          route: 'New-sleepover-request'
        },
        {
          icon: 'mdi-calendar',
          text: 'Seznam pobytů',
          route: 'Sleepovers-list'
        },
        {
          icon: 'mdi-cart',
          text: 'Nákupní seznam',
          route: 'Shopping-list'
        }
      ]

    }
  },

}
</script>