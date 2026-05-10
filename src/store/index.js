import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
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
  getters: {
    isAuthenticated: (state) => !!state.user,
  },
})
