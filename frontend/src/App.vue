<script setup>
import Map from "@/components/Map.vue";
import SelectYear from "@/components/SelectYear.vue";
import AqiLine from "@/components/AqiLine.vue";
import AreaChart from "./components/AreaChart.vue";
import BarChart from "./components/BarChart.vue";
</script>

<template>
  <div class="out-of-global">
    <div class="out-of-title">
      <div class="title">
        <div class="title-cn">
          空气质量分析
        </div>
        <div class="title-en">
          Air Pollutants Analysis
        </div>
      </div>
      <div class="out-of-year-select">
        <SelectYear></SelectYear>
      </div>
    </div>
    <div class="out-of-areaChart">
        <AreaChart></AreaChart>
    </div>
    <div class="out-of-graphic">
      <div class="out-of-map">
        <Map></Map>
      </div>
      <div class="out-of-aqiline">
        <AqiLine></AqiLine>
      </div>
    </div>
    <div class="out-of-barChart">
      <BarChart></BarChart>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.out-of-global {
  width: 100vw;
  height: 130vh;
  display: flex;
  flex-wrap: wrap;
  background: #f0f0f0;
  padding-bottom: 5px;
  .out-of-title {
    width: 100%;
    height: 12%;
    display: flex;
    justify-content: start;
    align-items: center;
    flex-wrap: nowrap;
    background: #c9dbff;
    .title {
      height: fit-content;
      position: relative;
      left: 30px;
      display: flex;
      flex-wrap: nowrap;
      color: #083cae;
      .title-cn {
        font-size: 32px;
        font-family: STZhongsong,serif;
      }
      .title-en {
        position: relative;
        left: 10px;
        font-size: 35px;
        font-family: "Californian FB",serif;
      }
    }
    .out-of-year-select {
      position: absolute;
      right: 55px;
    }
  }
  .out-of-graphic {
    width: 50%;
    height: 88%;
    display: flex;
    // justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    .out-of-map {
      width: 100%;
      height: 75%;
    }
    .out-of-aqiline {
      width: 100%;
      height: 25%;
    }
  }
  .out-of-areaChart {
    width: 25%;
    height: 88%;
  }
  .out-of-barChart {
    width: 25%;
    height: 88%;
  }
}
</style>
