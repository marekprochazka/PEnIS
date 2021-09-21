import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

import DatePicker from './components/utils/Date-picker.vue'

import './styles/_entry.scss'
import './django-reverse/reverse.js'

Vue.config.productionTip = false


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
