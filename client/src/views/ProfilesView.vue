<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import authService from '@/api/auth'

const router = useRouter()
const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

const handleLogin = async () => {
  try {
    loading.value = true
    error.value = ''
    
    const user = await authService.login(username.value, password.value)
    
    if (user.token) {
      router.push('/vent')
    } else {
      error.value = 'Ошибка авторизации'
    }
  } catch (err) {
    error.value = 'Неверные учетные данные'
    console.error('Login error:', err)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="login-page">
    <h1>Вход в систему</h1>
    
    <form @submit.prevent="handleLogin" class="login-form">
      <div class="form-group">
        <label>Имя пользователя:</label>
        <input v-model="username" type="text" required>
      </div>
      
      <div class="form-group">
        <label>Пароль:</label>
        <input v-model="password" type="password" required>
      </div>
      
      <button type="submit" :disabled="loading">
        {{ loading ? 'Вход...' : 'Войти' }}
      </button>
      
      <div v-if="error" class="error">{{ error }}</div>
    </form>
  </div>
</template>

<style scoped>
.login-page {
  max-width: 400px;
  margin: 100px auto;
  padding: 30px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.login-form {
  margin-top: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #cbd5e0;
  border-radius: 4px;
  font-size: 16px;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #3182ce;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

button:disabled {
  background-color: #a0aec0;
  cursor: not-allowed;
}

.error {
  margin-top: 15px;
  padding: 10px;
  background-color: #fff5f5;
  border: 1px solid #fc8181;
  border-radius: 4px;
  color: #e53e3e;
}
</style>