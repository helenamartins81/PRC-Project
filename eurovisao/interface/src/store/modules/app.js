// Pathify
import { make } from 'vuex-pathify'

// Data
const state = {
  drawer: null,
  drawerImage: true,
  mini: false,
  items: [
    {
      title: 'Home',
      icon: 'mdi-home',
      to: '/',
    },
    {
      title: 'About',
      icon: 'mdi-plus',
      to: '/about',
    },
    {
      title: 'Edição',
      icon: 'mdi-calendar-star',
      to: '/edicao',
    },
    {
      title: 'Musicas',
      icon: 'mdi-music-note',
      to: '/musica',
    },
  ],
}

const mutations = make.mutations(state)

const actions = {
  ...make.actions(state),
  init: async ({ dispatch }) => {
  },
}

const getters = {}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
}
