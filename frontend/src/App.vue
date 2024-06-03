<script setup>
import Map from "@/components/Map.vue";
</script>

<template>
  <div class="out-of-global">
    <div class="out-of-title">
      <div class="title">
        空气质量监测
      </div>
    </div>
    <div class="out-of-graphic">
      <div class="out-of-map">
        <Map></Map>
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
    height: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
    .title {
      height: fit-content;
      font-size: 20px;
    }
  }
  .out-of-graphic {
    width: 100%;
    height: 85%;
    display: flex;
    justify-content: center;
    align-items: center;
    .out-of-map {
      width: 70%;
      height: 80%;
    }
  }
}
</style>
