const state = () => ({
  snackBarMessage: null,
});

const mutations = {
  setSnackBarMessage(state, payload) {
    state.snackBarMessage = payload;
  },
};

export default {
  state,
  mutations,
};
