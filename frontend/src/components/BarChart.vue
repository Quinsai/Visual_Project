<script setup>
import {onMounted, watch} from "vue";
import * as echarts from "echarts";
import axios from "axios";
import {prefixUrl} from "@/main.js";
import {useYearStore} from "@/stores/year.js";
import {usePollutantStore} from "@/stores/pollutant.js";

const year = useYearStore()
const pollutant = usePollutantStore()

const loadBarChart = async(year, pollutant_id, pollutant_name) => {
    const response = await axios.get(prefixUrl + "/api/provinces/onePollutant", {
      params: {
        year: year,
        pollutant_id: pollutant_id
      }
    })
    const cityList = response.data.city_list;
    console.log(response.data.city_list)

    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow',
            },
            valueFormatter: (value) => {
                if(pollutant_id == 4) return value + ' mg/m³'
                else return value + ' μg/m³'
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        yAxis: {
            type: 'category',
            data: [],
            inverse: true,
            axisTick: {
                alignWithLabel: true
            }
        },
        xAxis: {
            type: 'value'
        },
        series: [
            {
                name: pollutant_name,
                data: [],
                type: 'bar'
            }
        ]
    };

    for (let i = 0; i < cityList.length; i++) {
        option.yAxis.data.push(cityList[i].cityName);
        option.series[0].data.push(cityList[i].value);
    }

    option && myChart.setOption(option);
}

onMounted(() => {
    loadBarChart(2013, 0, 'PM2.5')
})
watch(
  () => [year.getSelectedYear, pollutant.getSelectedPollutant.pollutantId],
  (value, oldValue) => {
    if (value !== oldValue) {
        loadBarChart(year.getSelectedYear, pollutant.getSelectedPollutant.pollutantId, pollutant.getSelectedPollutant.pollutantName)
    }
  }
)

const handleSelect = (item) => {
    console.log(item)
    pollutant.setSelectedPollutant(pollutant, item.value, item.label)
}

const map = [
    {value: 0, label: 'PM2.5'},
    {value: 1, label: 'PM10'},
    {value: 2, label: 'SO2'},
    {value: 3, label: 'NO2'},
    {value: 4, label: 'CO'},
    {value: 5, label: 'O3'},
]
</script>

<template>
  <div style="display: flex; justify-content: center; align-items: center;">
    <a-select
      :style="{
        width: '40%',
        height: '5%',
        background: 'rgb(22, 93, 255)',
        color: 'white',
        position: 'relative',
        left: '16px',
      }"
      @change="(item) => handleSelect(item)"
      v-model="value"
      :default-value="map[0]"
    >
      <a-option v-for="item of map" :value="item" :label="item.label" />
    </a-select>
  </div>
  <div id="main"></div>
</template>

<style lang="scss" scoped>
#main {
  height: 100%;
  width: 100%;
  position: relative;
  bottom: 10px;
}
</style>
