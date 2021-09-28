import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home/App.vue'
import NewSleepoverRequest from '../views/New-sleepover-request/App.vue'
import SleepoversList from '../views/Sleepovers-list/App.vue'
import ShoppingList from '../views/Shopping-list/App.vue'
Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/sleepovers/new',
    name: 'New-sleepover-request',
    component: NewSleepoverRequest
  },
  {
    path: '/sleepovers/list',
    name: 'Sleepovers-list',
    component: SleepoversList
  },
  {
    path: '/shopping/list',
    name: 'Shopping-list',
    component: ShoppingList
  }
]

const router = new VueRouter({
  routes,
  mode: 'hash'
})

export default router
