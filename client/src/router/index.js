import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import VentsView from '@/views/VentsView.vue'
import CartsView from '@/views/CartsView.vue'
import ProfilesView from '@/views/ProfilesView.vue'

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/vent',
    name: 'VentsView',
    component: VentsView,
    meta: { requiresAuth: true }
  },
  {
    path: '/cart',
    name: 'CartsView',
    component: CartsView,
    meta: { requiresAuth: true }
  },
  {
    path: '/profile',
    name: 'ProfilesView',
    component: ProfilesView
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// Проверка аутентификации
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true'
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/profile')
  } else {
    next()
  }
})

export default router