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
      path: '/profile/:nickname',
      name: 'profile',
      component: () => import('@/views/Profile/ProfileView.vue')
    },
    {
      path: '/search/:searchword',
      name: 'search',
      component: () => import('@/views/Search/SearchView.vue')
    },
    {
      path: '/movie/:movie_id',
      name: 'movieDetail',
      component: () => import('@/views/Movie/MovieDetailView.vue')
    },
    {
      path: '/admin',
      name: 'Admin',
      component: () => import('@/views/Admin/AdminView.vue')
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    // always scroll to top
    return { top: 0 };
  },
});

export default router;
