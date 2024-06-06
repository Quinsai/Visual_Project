import { defineStore } from 'pinia'

export const useProvinceStore = defineStore('province', {
  state: () => ({
    selectedProvinceId: 5,
    selectedProvinceName: "台湾"
  }),
  actions: {
    setSelectedProvince: (state, {id, name}) => {
      state.selectedProvinceId = id
      state.selectedProvinceName = name
    }
  },
  getters: {
    getSelectedProvince: (state) => {
      return {
        provinceId: state.selectedProvinceId,
        provinceName: state.selectedProvinceName
      }
    },
  }
})
