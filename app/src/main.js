import axios from "axios";
import Vue from "vue";
import VueSocketIO from "vue-socket.io";
import App from "./App.vue";
import snackbarPlugin from "./plugins/snackbar";
import vuetify from "./plugins/vuetify";
import router from "./router";
import store from "./store";

Vue.use(
  new VueSocketIO({
    connection: "http://localhost:3000",
    vuex: {
      store,
      actionPrefix: "SOCKET_",
      mutationPrefix: "SOCKET_"
    }
  })
);

Vue.use(snackbarPlugin, { store });

Vue.config.productionTip = false;

if (localStorage.getItem("token")) {
  axios.defaults.headers.common[
    "Authorization"
  ] = `Token ${localStorage.getItem("token")}`;
}

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
