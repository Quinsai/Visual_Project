<script setup>
import {onMounted, watch} from "vue";
import * as echarts from "echarts";
import axios from "axios";
import {prefixUrl} from "@/main.js";
import {useYearStore} from "@/stores/year.js";
import {usePollutantStore} from "@/stores/pollutant.js";

const year = useYearStore()
const pollutant_id = usePollutantStore()

const loadBarChart = async(year, pollutant_id) => {
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
                type: 'shadow'
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
    loadBarChart(2013, 0)
})
watch(
  () => [year.getSelectedYear, pollutant_id.getSelectedPollutant],
  (value, oldValue) => {
    if (value !== oldValue) {
        console.log('aaa')
        loadBarChart(year.getSelectedYear, pollutant_id.getSelectedPollutant)
    }
  }
)

const handleSelect = (value) => {
  pollutant_id.setSelectedPollutant(pollutant_id, value)
}
</script>

<template>
    <a-select 
        placeholder="PM2.5" 
        :style="{width: '40%', height: '5%', background: 'rgb(22, 93, 255)', color: 'white',  'input::placeholder': {color: 'white'}}"  
        @change="value => handleSelect(value)"
    >
        <a-option :value="0">PM2.5</a-option>
        <a-option :value="1">PM10</a-option>
        <a-option :value="2">SO2</a-option>
        <a-option :value="3">NO2</a-option>
        <a-option :value="4">CO</a-option>
        <a-option :value="5">O3</a-option>
    </a-select>
    <div id="main"></div>
</template>

<style lang="scss" scoped>
    #main {
        height: 95%;
        width: 100%;
    }
</style>
