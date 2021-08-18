import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";
import snackbar from "./modules/snackbar";
import users from "./modules/users";
import chats from "./modules/chats";


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    snackbar,
    users,
    chats
  }
});
