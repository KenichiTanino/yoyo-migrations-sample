import { getAccessorType } from 'typed-vuex'
import { GetterTree, ActionTree, MutationTree } from 'vuex'


export const state = () => ({
  addrs: [] as any
})

export type RootState = ReturnType<typeof state>

export const getters: GetterTree<RootState, RootState> = {
  getAddrs: function (state: { addrs: any } ) {
    return state.addrs
  },
  getAddr: (state: { addrs: any[] }) => (id: number) => {
    return state.addrs.find((addr) => addr.id == id)
  },
}

export const mutations: MutationTree<RootState> = {
  addAddr: function (state, payload) {
    if (state.addrs == undefined) {
      state.addrs = []
    }
    state.addrs.push(payload.addr)
  },
  updateAddr: function (state, payload) {
    state.addrs.forEach((addr, index) => {
      if (addr.id === payload.addr.id) {
        state.addrs.splice(index, 1, payload.addr)
      }
    })
  },
  removeAddr: function (state, payload) {
    state.addrs.forEach((addr, index) => {
      if (addr.id === payload.addr.id) {
        state.addrs.splice(index, 1)
      }
    })
  },
  clearAddr: function (state) {
    state.addrs = undefined
  }
}

import ApiClient from '~/lib/api';

let api = new ApiClient();

export const actions: ActionTree<RootState, RootState> = {
  async fetchNewAddrs({ state, commit }) {
    state.addrs = undefined;
    const addrs = await api.get_addrs(this.$axios);
    let addrsResult = addrs.Result;
    addrsResult.forEach((addr, index) => {
      commit('addAddr', {addr: addr})
    })
  },
  async removeAddrApi({ state, commit }, payload) {
    await api.post(this.$axios, 'delete', payload.addr);
    commit('removeAddr', {addr: payload.addr})
  },

}