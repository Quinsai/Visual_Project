<script setup>
import {useYearStore} from "@/stores/year.js";

const year = useYearStore()

const handleSelect = (value) => {
  year.setSelectedYear(year, value)
}

</script>

<template>
  <a-dropdown @select="value => handleSelect(value)">
    <a-button>{{ year.getSelectedYear }}</a-button>
    <template #content>
      <a-doption :value="2013">2013</a-doption>
      <a-doption :value="2014">2014</a-doption>
      <a-doption :value="2015">2015</a-doption>
      <a-doption :value="2016">2016</a-doption>
      <a-doption :value="2017">2017</a-doption>
      <a-doption :value="2018">2018</a-doption>
    </template>
  </a-dropdown>
</template>

<style scoped lang="scss">

</style>
