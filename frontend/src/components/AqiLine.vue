<script setup>

import axios from "axios";
import {prefixUrl} from "@/main.js";
import {useProvinceStore} from "@/stores/province.js";
import {onMounted, watch} from "vue";
import {useYearStore} from "@/stores/year.js";
import * as echarts from "echarts";

const year = useYearStore()
const province = useProvinceStore()

const getDataAndLoadLine = async (year, provinceId) => {
  let response = await axios.get(prefixUrl + "/api/province/aqi", {
    params: {
      year: year,
      province_id: provinceId
    }
  })
  let provinceData = response.data.month_list

  let xData = []
  let aqiData = []
  for (let i = 0; i < provinceData.length; i++) {
    xData.push(i+1)
    aqiData.push(provinceData[i].aqi)
  }

  let line = echarts.init(document.getElementById('container-of-aqi-line'));
  line.setOption({
    xAxis: {
      type: 'category',
      data: xData
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: aqiData,
        type: 'line'
      }
    ],
    tooltip: {
      show: true,
      position: 'right',
      formatter: 'AQI: ' + '{c0}'
    },
  })
}

onMounted(() => {
  getDataAndLoadLine(2013, 5)
})

watch(
  () => [year.getSelectedYear, province.getSelectedProvince],
  (value, oldValue) => {
    if (value !== oldValue) {
      getDataAndLoadLine(year.getSelectedYear, province.getSelectedProvince.provinceId)
    }
  }
)
</script>

<template>
  <div class="aqi-line">
    <div id="container-of-aqi-line" class="line"></div>
    <div class="legend-of-aqi-line-outer">
      <div class="legend-of-aqi-line">{{ year.getSelectedYear }}年{{ province.getSelectedProvince.provinceName }}逐月AQI变化</div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.aqi-line {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  position: relative;
  top: -15vh;
  .line {
    height: 150%;
    width: 100%;
  }
  .legend-of-aqi-line-outer {
    height: 20%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    bottom: 5vh;
    .legend-of-aqi-line {
      font-family: STXihei,serif;
      color: black;
    }
  }
}
</style>
