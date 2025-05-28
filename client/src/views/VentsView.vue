<script setup>
import { ref, onBeforeMount } from 'vue';
import axios from "axios";

const vents = ref([]);
const loading = ref(false);
const error = ref(null);

async function fetchVents() {
  try {
    loading.value = true;
    error.value = null;
    const response = await axios.get("/api/vents/");
    vents.value = response.data;
  } catch (err) {
    error.value = err.message || "Failed to fetch vents";
    console.error("Error fetching vents:", err);
  } finally {
    loading.value = false;
  }
}

function onLoadClick() {
  fetchVents();
}

onBeforeMount(() => {
  fetchVents();
});
</script>

<template>
  <div class="vents-container">
    <h1>Vents List</h1>
    
    <button @click="onLoadClick" :disabled="loading">
      {{ loading ? 'Loading...' : 'Refresh List' }}
    </button>

    <div v-if="error" class="error-message">
      Error: {{ error }}
    </div>

    <div v-if="loading && !vents.length" class="loading-message">
      Loading vents...
    </div>

    <div v-else-if="vents.length" class="vents-list">
      <div v-for="vent in vents" :key="vent.id" class="vent-item">
        <h3>{{ vent.ventName }}</h3>
        <div v-if="vent.picture" class="vent-image">
          <img :src="vent.picture" :alt="vent.ventName" />
        </div>
      </div>
    </div>

    <div v-else class="no-vents">
      No vents found
    </div>
  </div>
</template>

<style scoped>
.vents-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #2c3e50;
  margin-bottom: 20px;
}

button {
  padding: 10px 15px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 20px;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.error-message {
  color: #ff4444;
  padding: 10px;
  background-color: #ffeeee;
  border-radius: 4px;
  margin-bottom: 20px;
}

.loading-message {
  color: #666;
  padding: 20px;
  text-align: center;
}

.vents-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.vent-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.vent-item h3 {
  margin-top: 0;
  color: #2c3e50;
}

.vent-image img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  margin-top: 10px;
}

.no-vents {
  padding: 20px;
  text-align: center;
  color: #666;
}
</style>