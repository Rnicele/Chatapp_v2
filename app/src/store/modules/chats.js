import { getAll } from "@/services/chatService";

const state = () => ({
  room: null,
  chatsLoading: false
});

const getters = {
  getChats: state => state.room.conversations,
  getChatsLoading: state => state.chatsLoading
};

const mutations = {
  setChats(state, payload) {
    state.chats = payload;
  },
  setChatsLoading(state, payload) {
    state.chatsLoading = payload;
  }
};

const actions = {
  setChats: async ({ commit }, {uid, cuid}) => {
    console.log(uid, cuid);
    try {
      commit("setChatsLoading", true);
      const { data } = await getAll(uid, cuid);
      commit("setChats", data);
    } catch (error) {
      console.error("[setChats]", error);
    }

    commit("setChatsLoading", false);
  },
  setChatsLoading: ({ commit }, payload) => commit("setChatsLoading", payload)
};

export default {
  state,
  actions,
  mutations,
  getters
};
