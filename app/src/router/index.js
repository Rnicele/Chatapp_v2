import Vue from "vue";
import VueRouter from "vue-router";
import Chat from "../views/app/Chat.vue";
import SignIn from "../views/auth/SignIn.vue";
import SignUp from "../views/auth/SignUp.vue";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/sign-up",
    name: "Sign Up",
    component: SignUp,
  },
  {
    path: "/sign-in",
    name: "Sign In",
    component: SignIn,
  },
  {
    path: "/chat",
    name: "Chat",
    component: Chat,
  },
];

export default new VueRouter({
  routes,
  mode: "history",
});
