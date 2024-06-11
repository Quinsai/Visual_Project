import { defineStore } from 'pinia'

export const usePollutantStore = defineStore('pollutant', {
    state: () => ({
        selectedPollutant: 0,
    }),
    actions: {
        setSelectedPollutant: (state, pollutant) => {
            console.log(pollutant)
            state.selectedPollutant = pollutant
        }
    },
    getters: {
        getSelectedPollutant: (state) => state.selectedPollutant,
    }
})