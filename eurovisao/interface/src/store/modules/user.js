// Utilities
import { make } from 'vuex-pathify'

// Globals
import { IN_BROWSER } from '@/util/globals'

const state = {
  dark: false,
  drawer: {
    image: 0,
    gradient: 0,
    mini: false,
  },
  gradients: [
    'rgba(0, 0, 0, .7), rgba(0, 0, 0, .7)',
    'rgba(228, 226, 226, 1), rgba(255, 255, 255, 0.7)',
  ],
  images: [
    'https://www.ukrainetogo.com/wp-content/uploads/2017/09/sobral-3.jpg',
    'https://www.middleeasteye.net/sites/default/files/styles/article_page/public/images-story/israelieurovision.afp_.jpg?itok=9uv2a_Au',
    'https://www.eurovision.de/niederlande1166_v-contentxl.jpg',
    'https://i1.wp.com/escxtra.com/wp-content/uploads/Maneskin-2021-e1621794952242.jpg?fit=1254%2C680&ssl=1',
  ],
  rtl: false,
}

const mutations = make.mutations(state)

const actions = {
  fetch: ({ commit }) => {
    const local = localStorage.getItem('vuetify@user') || '{}'
    const user = JSON.parse(local)

    for (const key in user) {
      commit(key, user[key])
    }

    if (user.dark === undefined) {
      commit('dark', window.matchMedia('(prefers-color-scheme: dark)'))
    }
  },
  update: ({ state }) => {
    if (!IN_BROWSER) return

    localStorage.setItem('vuetify@user', JSON.stringify(state))
  },
}

const getters = {
  dark: (state, getters) => {
    return (
      state.dark ||
      getters.gradient.indexOf('255, 255, 255') === -1
    )
  },
  gradient: state => {
    return state.gradients[state.drawer.gradient]
  },
  image: state => {
    return state.drawer.image === '' ? state.drawer.image : state.images[state.drawer.image]
  },
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
}
