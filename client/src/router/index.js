import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import SevicesView from '@/views/SevicesView.vue'
import CartsView from '@/views/CartsView.vue'
import ProfilesView from '@/views/ProfilesView.vue'
import VentsView from '@/views/VentsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/", 
      name: "MainView", 
      component: MainView
    },
    {
      path: "/service", 
      name: "SevicesView", 
      component: SevicesView
    },
    {
      path: "/cart", 
      name: "CartsView", 
      component: CartsView
    },
    {
      path: "/profile", 
      name: "ProfilesView", 
      component: ProfilesView
    },
    {
      path: "/vent", 
      name: "VentsView", 
      component: VentsView
    }
  ]
})

export default router
