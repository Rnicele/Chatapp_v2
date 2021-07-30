import axios from "axios";

export function getAll() {
  return axios.get("http://127.0.0.1:7000/users/");
}
