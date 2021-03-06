import Vue from "vue";
import VueRouter from "vue-router";
import AlreadyAuthenticatedGuard from "../guards/alreadyAuthenticated";
import AuthGuard from "../guards/auth";
import Chat from "../views/app/Chat.vue";
import App from "../views/app/Index.vue";
import SignIn from "../views/auth/SignIn.vue";
import SignUp from "../views/auth/SignUp.vue";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/sign-up",
    name: "Sign Up",
    component: SignUp,
    beforeEnter: AlreadyAuthenticatedGuard
  },
  {
    path: "/sign-in",
    name: "Sign In",
    component: SignIn,
    beforeEnter: AlreadyAuthenticatedGuard
  },
  {
    path: "/app",
    component: App,
    beforeEnter: AuthGuard,
    redirect: "chat",
    children: [
      {
        path: "chat",
        name: "Chat",
        component: Chat
      }
    ]
  }
];

export default new VueRouter({
  routes,
  mode: "history"
});
