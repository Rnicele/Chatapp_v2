import axios from "axios";

export function getAll(uid, cuid) {
  return axios.get(`http://127.0.0.1:7000/rooms/?uid=${uid}&cuid=${cuid}`);
}

export function create(payload) {
  return axios.post(`http://127.0.0.1:7000/chats/`, payload);
}
