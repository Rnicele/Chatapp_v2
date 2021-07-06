import Vue from "vue";
import App from "./App.vue";
import snackbarPlugin from "./plugins/snackbar";
import vuetify from "./plugins/vuetify";
import router from "./router";
import store from "./store";

Vue.use(snackbarPlugin, { store });

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
