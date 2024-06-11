<script setup>
import {onMounted, watch} from "vue";
import * as echarts from "echarts";
import axios from "axios";
import {prefixUrl} from "@/main.js";
import {useYearStore} from "@/stores/year.js";
import {useProvinceStore} from "@/stores/province.js";

const year = useYearStore()
const province = useProvinceStore()

const loadAreaChart = async(year, province_id) => {
    const response = await axios.get(prefixUrl + "/api/province/allPollutants", {
      params: {
        year: year,
        province_id: province_id
      }
    })
    const monthList = response.data.month_list;

    var chartDom = document.getElementById('chart-container');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
        color: ['#8dd3c7', '#bebada', '#fdb462', '#80b1d3', '#fb8072'],
        // title: {
        //     text: 'Area Chart'
        // },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                label: {
                    backgroundColor: '#6a7985'
                }
            }
        },
        legend: {
            data: ['PM2.5', 'PM10', 'SO2', 'NO2', 'O3']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        yAxis: [
            {
                type: 'category',
                boundaryGap: false,
                inverse: true,
                data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            }
        ],
        xAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: 'PM2.5',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                showSymbol: false,
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                        offset: 0,
                        color: '#8dd3c7'
                    }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: []
            },
            {
                name: 'PM10',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                showSymbol: false,
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                        offset: 0,
                        color: '#bebada'
                    }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: []
            },
            {
                name: 'SO2',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                showSymbol: false,
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                        offset: 0,
                        color: '#fdb462'
                    }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: []
            },
            {
                name: 'NO2',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                showSymbol: false,
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                        offset: 0,
                        color: '#80b1d3'
                    }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: []
            },
            {
                name: 'O3',
                type: 'line',
                stack: 'Total',
                smooth: true,
                lineStyle: {
                    width: 0
                },
                showSymbol: false,
                label: {
                    show: true,
                    position: 'top'
                },
                areaStyle: {
                    opacity: 0.8,
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {
                        offset: 0,
                        color: '#fb8072'
                    }
                    ])
                },
                emphasis: {
                    focus: 'series'
                },
                data: []
            }
        ]
    };

    for (let i = 0; i < monthList.length; i++) {
        option.series[0].data.push(monthList[i].PM2_5);
        option.series[1].data.push(monthList[i].PM10);
        option.series[2].data.push(monthList[i].SO2);
        option.series[3].data.push(monthList[i].NO2);
        option.series[4].data.push(monthList[i].O3);
    }
    
    option && myChart.setOption(option);
}

onMounted(() => {
    loadAreaChart(2013, 5)
})

watch(
  () => [year.getSelectedYear, province.getSelectedProvince],
  (value, oldValue) => {
    if (value !== oldValue) {
      loadAreaChart(year.getSelectedYear, province.getSelectedProvince.provinceId)
    }
  }
)
</script>

<template>
    <div id="chart-container"></div>
</template>

<style lang="scss" scoped>
    #chart-container {
        height: 100%;
        width: 100%;
    }
</style>
