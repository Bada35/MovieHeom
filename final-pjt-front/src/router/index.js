import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/Home/HomeView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('@/views/Profile/ProfileView.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('@/views/Search/SearchView.vue')
    },
    {
      path: '/movieId',
      name:'movieDetail',
      component: () => import('@/views/Movie/MovieDetailView.vue')
    }
  ]
});

export default router;
