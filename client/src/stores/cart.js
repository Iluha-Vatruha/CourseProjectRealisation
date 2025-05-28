import { defineStore } from 'pinia'
import { ref, watch } from 'vue'

export const useCartStore = defineStore('cart', () => {
  // Загружаем корзину из localStorage при инициализации
  const items = ref(JSON.parse(localStorage.getItem('cartItems')) || [])
  
  // Сохраняем корзину в localStorage при любом изменении
  watch(items, (newItems) => {
    localStorage.setItem('cartItems', JSON.stringify(newItems))
  }, { deep: true })
  
  function addItem(vent) {
    items.value.push({
      ...vent,
      param: '',
      quantity: 1
    })
  }
  
  function removeItem(id) {
    const index = items.value.findIndex(item => item.id === id)
    if (index !== -1) {
      items.value.splice(index, 1)
    }
  }
  
  function updateItem(id, updates) {
    const index = items.value.findIndex(item => item.id === id)
    if (index !== -1) {
      items.value[index] = { ...items.value[index], ...updates }
    }
  }
  
  function clearCart() {
    items.value = []
  }
  
  return {
    items,
    addItem,
    removeItem,
    updateItem,
    clearCart
  }
})