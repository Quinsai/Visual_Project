import { defineStore } from 'pinia'

export const useYearStore = defineStore('year', {
  state: () => ({
    selectedYear: 2013,
  }),
  actions: {
    setSelectedYear: (state, year) => {
      console.log(year)
      state.selectedYear = year
    }
  },
  getters: {
    getSelectedYear: (state) => state.selectedYear,
  }
})
