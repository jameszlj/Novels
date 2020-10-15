import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import HomeCate from "../views/HomeCate.vue"
import NovelIndex from "../views/NovelIndex.vue"
import NovelDetail from "../views/NovelDetail.vue"
import NovelSearch from '../views/NovelSearch.vue'

Vue.use(VueRouter)


// const originalPush = VueRouter.prototype.push
// VueRouter.prototype.push = function push(location) {
//   return originalPush.call(this, location).catch(err => err)
// }

const routes = [
  {
    // 首页
    path: '/',
    name: 'Home',
    component: Home
  },
  // 小说搜索
  {
    path: "/search",
    name: "NovelSearch",
    component: NovelSearch
  },

  // 分类页面
  {
    path: "/:cate_id",
    name: "HomeCate",
    component: HomeCate
  },
  // 单个小说的首页
  {
    path: "/novel/:book_id",
    name: "NovelIndex",
    component: NovelIndex
  },

  // 小说详情页 
  {
    path: "/novel/:book_id/:sort_id",
    name: "NovelDetail",
    component: NovelDetail
  },

  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  mode: "history", //去掉路由后的#/
  base: process.env.BASE_URL,
  routes
})

export default router
