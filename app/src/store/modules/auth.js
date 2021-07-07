const state = () => ({
  user: null,
  token: null
});

const getters = {
  getUser: state => state.user,
  getToken: state => state.token,
  getUserName: state => state.user.first_name,
  getUserFullName: state => `${state.user.first_name} ${state.user.last_name}`
};

const mutations = {
  setUser(state, payload) {
    state.user = payload;
    localStorage.setItem("user", JSON.stringify(payload));
  },
  setToken(state, payload) {
    state.token = payload;
    localStorage.setItem("token", payload);
  }
};

const actions = {
  setUser: ({ commit }, payload) => commit("setUser", payload),
  setToken: ({ commit }, payload) => commit("setToken", payload),
  setUserToken: ({ commit }, payload) => {
    commit("setUser", payload.user);
    commit("setToken", payload.token);
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
