<script setup>
import {onMounted} from "vue";
import * as echarts from "echarts";
import axios from "axios";
import {prefixUrl} from "@/main.js";

onMounted(async() => {
    // const response = await axios.get(prefixUrl + "/api/province/allPollutants", {
    //   params: {
    //     year: 2013,
    //     province: '上海'
    //   }
    // })
    // const monthList = response.data.month_list;

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
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
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
                data: [120, 200, 150, 80, 70, 110, 130],
                type: 'bar'
            }
        ]
    };

    // option.yAxis.data.push('opp');
    option && myChart.setOption(option);
})

</script>

<template>
    <div id="main"></div>
</template>

<style lang="scss" scoped>
    #main {
        height: 100%;
        width: 100%;
    }
</style>
