<script setup>
import {computed, ref, onBeforeMount} from 'vue';
import axios from "axios";  
import { storeToRefs } from 'pinia';


const vents = ref([]);

async function fetchVents(){
    loading.value = true;
    const r = await axios.get("/api/vents");
    console.log(r.data)
    vents.value = r.data;
    loading.value = false;
}

async function onLoadClick() {
  await fetchVents()
}

onBeforeMount(async () =>{
    await fetchVents()
})

</script>

<template>
    <div v-for="item in vents">
        {{ item.fio }}
    </div>
</template>

<style scooped>

</style>