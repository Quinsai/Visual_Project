<script setup>
import Map from "@/components/Map.vue";
import SelectYear from "@/components/SelectYear.vue";
import AqiLine from "@/components/AqiLine.vue";
</script>

<template>
  <div class="out-of-global">
    <div class="out-of-title">
      <div class="title">
        空气质量监测
      </div>
      <div class="out-of-year-select">
        <SelectYear></SelectYear>
      </div>
    </div>
    <div class="out-of-graphic">
      <div class="out-of-map">
        <Map></Map>
      </div>
      <div class="out-of-aqiline">
        <AqiLine></AqiLine>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.out-of-global {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  .out-of-title {
    width: 100%;
    height: 12%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: nowrap;
    .title {
      height: fit-content;
      font-size: 20px;
    }
    .out-of-year-select {
      position: absolute;
      right: 10px;
    }
  }
  .out-of-graphic {
    width: 100%;
    height: 88%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    .out-of-map {
      width: 70%;
      height: 75%;
    }
    .out-of-aqiline {
      width: 70%;
      height: 25%;
    }
  }
}
</style>
