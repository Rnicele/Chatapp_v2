import { getAll } from "@/services/userService";

const state = () => ({
  users: null,
  usersLoading: false
});

const getters = {
  getUsers: state => state.users,
  getUsersDefaultAvatar: () =>
    "https://t4.ftcdn.net/jpg/00/64/67/63/360_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg",
  getUsersLoading: state => state.usersLoading
};

const mutations = {
  setUsers(state, payload) {
    state.users = payload;
  },
  setUsersLoading(state, payload) {
    state.usersLoading = payload;
  }
};

const actions = {
  setUsers: async ({ commit }) => {
    try {
      commit("setUsersLoading", true);
      const { data } = await getAll();
      commit("setUsers", data);
    } catch (error) {
      console.error("[setUsers]", error);
    }

    commit("setUsersLoading", false);
  },
  setUsersLoading: ({ commit }, payload) => commit("setUsersLoading", payload)
};

export default {
  state,
  actions,
  mutations,
  getters
};
