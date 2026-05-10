import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import InternshipDetail from '../views/InternshipDetail.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/internship/:id', name: 'InternshipDetail', component: InternshipDetail },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
