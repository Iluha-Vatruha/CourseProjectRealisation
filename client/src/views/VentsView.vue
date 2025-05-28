<script setup>
import { ref, onMounted } from 'vue'
import { useCartStore } from '@/stores/cart'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const cartStore = useCartStore()
const vents = ref([])
const loading = ref(false)
const error = ref(null)

const fetchVents = async () => {
  try {
    loading.value = true
    const response = await axios.get('/api/vents/')
    vents.value = response.data
  } catch (err) {
    error.value = 'Ошибка загрузки заготовок: ' + (err.response?.data?.message || err.message)
  } finally {
    loading.value = false
  }
}

const addToCart = (vent) => {
  cartStore.addItem(vent)
  router.push('/cart')
}

onMounted(() => {
  fetchVents()
})
</script>

<template>
  <div class="vents-page">
    <h1>Каталог заготовок</h1>
    
    <div class="cart-indicator" @click="router.push('/cart')">
      Корзина ({{ cartStore.items.length }})
    </div>
    
    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    
    <div v-else class="vents-grid">
      <div v-for="vent in vents" :key="vent.id" class="vent-card">
        <div class="vent-image-container">
          <img v-if="vent.picture" :src="vent.picture" :alt="vent.ventName" class="vent-image" />
          <div v-else class="image-placeholder">Изображение отсутствует</div>
        </div>
        <div class="vent-info">
          <h3>{{ vent.ventName }}</h3>
          <button @click="addToCart(vent)" class="add-btn">
            Добавить в корзину
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.vents-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  position: relative;
}

.cart-indicator {
  position: absolute;
  top: 20px;
  right: 20px;
  padding: 10px 15px;
  background-color: #42b983;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.vents-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 25px;
  margin-top: 40px;
}

.vent-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.vent-card:hover {
  transform: translateY(-5px);
}

.vent-image-container {
  height: 200px;
  background-color: #f9f9f9;
  display: flex;
  align-items: center;
  justify-content: center;
}

.vent-image {
  max-height: 100%;
  max-width: 100%;
  object-fit: contain;
}

.image-placeholder {
  color: #888;
  font-style: italic;
}

.vent-info {
  padding: 15px;
  text-align: center;
}

.vent-info h3 {
  margin: 10px 0;
  color: #333;
}

.add-btn {
  padding: 8px 16px;
  background-color: #35495e;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.add-btn:hover {
  background-color: #42b983;
}

.loading, .error {
  text-align: center;
  padding: 40px;
  font-size: 18px;
}

.error {
  color: #e53935;
}
</style>