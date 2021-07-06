const snackbarPlugin = {
  install: (Vue, { store }) => {
    if (!store) {
      throw new Error("Please provide vuex store.");
    }

    Vue.prototype.$snackbar = {
      showMessage: function(message) {
        store.commit("setSnackBarMessage", message, { root: true });
      },
    };
  },
};

export default snackbarPlugin;
