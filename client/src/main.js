import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import authService from '@/api/auth'

const app = createApp(App)

// Настройка базового URL для API
axios.defaults.baseURL = '/api/'

// Добавление интерсептора для авторизации
axios.interceptors.request.use(config => {
  const user = authService.getCurrentUser()
  
  if (user && user.token) {
    config.headers.Authorization = `Token ${user.token}`
  }
  
  return config
}, error => {
  return Promise.reject(error)
})

app.use(router)
app.mount('#app')
