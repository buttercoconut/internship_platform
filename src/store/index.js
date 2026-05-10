import { createStore } from 'vuex'

const store = createStore({
  state() {
    return {
      user: null,
    }
  },
  mutations: {
    setUser(state, payload) {
      state.user = payload
    },
  },
  actions: {
    login({ commit }, user) {
      commit('setUser', user)
    },
  },
})

export default store
