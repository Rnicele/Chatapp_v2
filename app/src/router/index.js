import Vue from "vue";
import VueRouter from "vue-router";
import Signin from "../views/Signin.vue";
// import Home from '../views/Home.vue'
<<<<<<< HEAD
import SignUp from '../views/Signup.vue'
import Signin from '../views/Signin.vue'
import Chat from '../views/Chat.vue'
Vue.use(VueRouter)
=======
import SignUp from "../views/Signup.vue";
Vue.use(VueRouter);
>>>>>>> 1679ea4835bafaf6a47ae08d9667acea1c318645

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  {
    path: "/Signup",
    name: "Signup",
    component: SignUp,
  },
  {
<<<<<<< HEAD
    path: '/Signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/Chat',
    name: 'Chat',
    component: Chat
  }
]
=======
    path: "/Signin",
    name: "Signin",
    component: Signin,
  },
];
>>>>>>> 1679ea4835bafaf6a47ae08d9667acea1c318645

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
