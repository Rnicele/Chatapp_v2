import store from "@/store";

export default async (to, from, next) => {
  if (!store.getters.isAuthenticated) {
    next("/sign-in");
  } else {
    next();
  }
};
