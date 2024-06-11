import { defineStore } from 'pinia'

export const usePollutantStore = defineStore('pollutant', {
    state: () => ({
        selectedPollutantId: 0,
        selectedPollutantName: 'PM2.5'
    }),
    actions: {
        setSelectedPollutant: (state, id, name) => {
            state.selectedPollutantId = id
            state.selectedPollutantName = name
        }
    },
    getters: {
        getSelectedPollutant: (state) => {
            return {
                pollutantId: state.selectedPollutantId,
                pollutantName: state.selectedPollutantName
            }
        }
    }
})