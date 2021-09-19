import Vue from 'vue'
import Vuex from 'vuex'

import state from './_state'
import mutations from './_mutations'
import actions from './_actions'
import getters from './_getters'

Vue.use(Vuex)

export default new Vuex.Store({
    state,
    mutations,
    actions,
    getters
})
