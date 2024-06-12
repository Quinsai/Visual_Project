<script setup>
import {onMounted, watch} from "vue";
import * as echarts from "echarts";
import $ from 'jquery'
import axios from "axios";
import {prefixUrl} from "@/main.js";
import {useYearStore} from "@/stores/year.js";
import {useProvinceStore} from "@/stores/province.js";

const colors = [
  {range: "<70", color: "#00E400"},
  {range: "70-100", color: "#FFFF00"},
  {range: "100-130", color: "#FF7E00"},
  {range: "130-160", color: "#FF0000"},
  {range: "160-190", color: "#8F3F97"},
  {range: ">190", color: "#7E0023"}
]

const year = useYearStore()
const province = useProvinceStore()

let provinceData = []
let provinceRegion = []

const getDataAndLoadMap = async (year) => {
  const response = await axios.get(prefixUrl + "/api/provinces/average-aqi", {
    params: {
      year: year
    }
  })
  provinceData = response.data.province_list

  for (let i = 0; i <provinceData.length; i++) {
    let aqiData = provinceData[i].average_aqi
    let aqiColor
    if (aqiData < 70) {
      aqiColor = colors[0].color
    }
    else if (aqiData < 100) {
      aqiColor = colors[1].color
    }
    else if (aqiData < 130) {
      aqiColor = colors[2].color
    }
    else if (aqiData < 160) {
      aqiColor = colors[3].color
    }
    else if (aqiData < 190) {
      aqiColor = colors[4].color
    }
    else {
      aqiColor = colors[5].color
    }
    let fullName = provinceData[i].province
    let provinceName
    if (fullName[0] === '内' || fullName[0] === '黑') {
      provinceName = provinceData[i].province.slice(0, 3)
    }
    else {
      provinceName = provinceData[i].province.slice(0, 2)
    }
    let tooltipContent = [
      '地区: ' + provinceName,
      'AQI: ' + aqiData
    ].join('<br>')
    provinceRegion.push({
      name: provinceName,
      itemStyle: {
        areaColor: aqiColor,
        color: aqiColor
      },
      tooltip: {
        show: true,
        position: 'right',
        formatter: tooltipContent
      },
      data: {
        provinceId: provinceData[i].province_id
      },
      grid: {
        x: 800,
        y: 800
      }
    })
  }

  $.get('https://geojson.cn/api/data/china.json', function (china) {
    echarts.registerMap('china', china)
    const map = echarts.init(document.getElementById('map-container'))
    map.setOption({
      geo: {
        map: 'china',
        regions: provinceRegion,
      },
      tooltip: {
        trigger: 'item',
      }
    })

    map.on('click', (params) => {
      province.setSelectedProvince(province, {
        id: params.region.data.provinceId,
        name: params.region.name,
      })
    })
  })
}

onMounted(() => {
  getDataAndLoadMap(2013)
})

watch(
  () => year.getSelectedYear,
  (value, oldValue) => {
    if (value !== oldValue) {
      getDataAndLoadMap(value)
    }
  }
)

onMounted(() => {
  let container = document.getElementById('map-container')
  console.log(container.children)
})
</script>

<template>
  <div class="map">
    <div class="legend-outer">
      <div class="legend-item-outer" v-for="color in colors">
        <div class="color-outer">
          <div class="color" :style="{backgroundColor: color.color}"></div>
        </div>
        <div class="range-outer">
          <div class="range">{{ color.range }}</div>
        </div>
      </div>
    </div>
    <div id="map-container" class="map-container"></div>
  </div>
</template>

<style lang="scss" scoped>
.map {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: nowrap;
  position: relative;
  top: -10vh;
  .legend-outer {
    height: 100%;
    width: 80px;
    position: relative;
    left: 40px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-content: flex-end;
    .legend-item-outer {
      width: 100%;
      height: 7%;
      display: flex;
      flex-wrap: nowrap;
      .color-outer {
        height: 100%;
        width: 30%;
        display: flex;
        justify-content: center;
        align-items: center;
        .color {
          height: 12px;
          width: 12px;
        }
      }
      .range-outer {
        height: 100%;
        width: 70%;
        display: flex;
        justify-content: flex-start;
        align-content: center;
        .range {
          font-size: 12px;
          display: flex;
          align-items: center;
          color: black;
        }
      }
    }
  }
  .map-container {
    position: relative;
    width: 100%;
    height: 100%;
  }
}
</style>
