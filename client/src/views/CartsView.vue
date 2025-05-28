<script setup>
import { ref } from 'vue'
import { useCartStore } from '@/stores/cart'
import axios from 'axios'
import { useRouter } from 'vue-router'

const cartStore = useCartStore()
const router = useRouter()
const showParamModal = ref(false)
const currentItem = ref(null)
const paramInput = ref('')
const quantityInput = ref(1)
const submitting = ref(false)
const submitError = ref(null)
const submitSuccess = ref(false)

const openParamModal = (item) => {
  currentItem.value = item
  paramInput.value = item.param
  quantityInput.value = item.quantity
  showParamModal.value = true
}

const saveParams = () => {
  cartStore.updateItem(currentItem.value.id, {
    param: paramInput.value,
    quantity: quantityInput.value
  })
  showParamModal.value = false
}

const submitOrder = async () => {
  try {
    submitting.value = true
    submitError.value = null
    submitSuccess.value = false
    
    // Получаем текущего пользователя
    const currentUser = authService.getCurrentUser()
    if (!currentUser || !currentUser.client_id) {
      throw new Error('User not authenticated')
    }
    
    // Создаем заказ
    const orderResponse = await axios.post('/orders/', {
      comment: 'Заказ с сайта',
      date: new Date().toISOString().split('T')[0],
      user: currentUser.client_id // Используем client_id из аутентификации
    })
    
    // Добавляем элементы заказа
    await Promise.all(
      cartStore.items.map(item => 
        axios.post('/lists/', {
          orderNumber: orderResponse.data.id,
          ventName: item.id,
          param: item.param,
          quantity: item.quantity
        })
      )
    )
    
    // Успешное создание заказа
    submitSuccess.value = true
    cartStore.clearCart()
    
  } catch (error) {
    submitError.value = 'Ошибка оформления заказа: ' + 
      (error.response?.data?.message || error.message)
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <div class="cart-page">
    <h1>Ваша корзина</h1>
    
    <div v-if="submitSuccess" class="success-message">
      <h2>Заказ успешно оформлен!</h2>
      <p>Ваш заказ был принят в обработку.</p>
      <button @click="router.push('/vent')" class="back-btn">
        Вернуться к каталогу
      </button>
    </div>
    
    <div v-else-if="cartStore.items.length === 0" class="empty-cart">
      <p>Ваша корзина пуста</p>
      <button @click="router.push('/vent')" class="browse-btn">
        Перейти к каталогу
      </button>
    </div>
    
    <div v-else class="cart-container">
      <div class="cart-items">
        <div v-for="item in cartStore.items" :key="item.id" class="cart-item">
          <div class="item-header">
            <h3>{{ item.ventName }}</h3>
            <button @click="cartStore.removeItem(item.id)" class="remove-btn">
              &times;
            </button>
          </div>
          
          <div class="item-details">
            <div class="param-field">
              <label>Характеристики:</label>
              <input 
                :value="item.param" 
                @input="cartStore.updateItem(item.id, { param: $event.target.value })" 
                type="text" 
                placeholder="Введите характеристики"
              />
            </div>
            
            <div class="quantity-field">
              <label>Количество:</label>
              <input 
                :value="item.quantity" 
                @input="cartStore.updateItem(item.id, { quantity: $event.target.value })" 
                type="number" 
                min="1"
              />
            </div>
          </div>
        </div>
      </div>
      
      <div class="cart-actions">
        <button 
          @click="submitOrder" 
          :disabled="submitting" 
          class="submit-btn"
        >
          {{ submitting ? 'Оформление...' : 'Оформить заказ' }}
        </button>
        
        <button @click="router.push('/vent')" class="continue-btn">
          Добавить ещё
        </button>
      </div>
      
      <div v-if="submitError" class="error-message">
        {{ submitError }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.cart-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.success-message {
  text-align: center;
  padding: 40px;
  background-color: #f0fff4;
  border-radius: 8px;
  border: 1px solid #c6f6d5;
}

.success-message h2 {
  color: #2f855a;
}

.back-btn {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #2f855a;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.empty-cart {
  text-align: center;
  padding: 40px;
}

.browse-btn {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #35495e;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.cart-container {
  margin-top: 30px;
}

.cart-items {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
}

.cart-item {
  padding: 20px;
  border-bottom: 1px solid #eee;
}

.cart-item:last-child {
  border-bottom: none;
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.item-header h3 {
  margin: 0;
}

.remove-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #e53e3e;
  padding: 5px;
}

.item-details {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 15px;
}

.param-field, .quantity-field {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
  font-weight: 500;
  color: #4a5568;
}

input {
  padding: 10px;
  border: 1px solid #cbd5e0;
  border-radius: 4px;
  font-size: 16px;
}

.quantity-field input {
  max-width: 100px;
}

.cart-actions {
  margin-top: 30px;
  display: flex;
  gap: 15px;
}

.submit-btn {
  flex: 2;
  padding: 15px;
  background-color: #2f855a;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 18px;
  cursor: pointer;
}

.submit-btn:disabled {
  background-color: #cbd5e0;
  cursor: not-allowed;
}

.continue-btn {
  flex: 1;
  padding: 15px;
  background-color: #3182ce;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 18px;
  cursor: pointer;
}

.error-message {
  margin-top: 20px;
  padding: 15px;
  background-color: #fff5f5;
  border: 1px solid #fc8181;
  border-radius: 4px;
  color: #e53e3e;
}
</style>