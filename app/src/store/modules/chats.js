import { getAll } from "@/services/chatService";
import _ from "lodash";

const state = () => ({
  room: null,
  chatsLoading: false
});

const getters = {
  getRoom: state => state.room,
  getChats: state => _.get(state.room, "conversations"),
  getChatsLoading: state => state.chatsLoading
};

const mutations = {
  setRoom(state, payload) {
    state.room = payload;
  },
  setConversations(state, payload) {
    state.room.conversations = payload;
  },
  setChatsLoading(state, payload) {
    state.chatsLoading = payload;
  }
};

const actions = {
  setRoom: async ({ commit }, { uid, cuid }) => {
    try {
      commit("setChatsLoading", true);
      const { data } = await getAll(uid, cuid);
      commit("setRoom", data);
    } catch (error) {
      console.error("[setRoom]", error);
    }

    commit("setChatsLoading", false);
  },
  addConversation: ({ state, commit }, message) => {
    commit("setConversations", [
      ..._.get(state.room, "conversations"),
      message
    ]);
  },
  setChatsLoading: ({ commit }, payload) => commit("setChatsLoading", payload)
};

export default {
  state,
  actions,
  mutations,
  getters
};
