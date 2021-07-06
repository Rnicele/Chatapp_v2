<template>
  <v-app style="background-color: aquamarine;">
    <v-main>
      <router-view />
    </v-main>

    <Snackbar></Snackbar>
  </v-app>
</template>

<script>
import Snackbar from "@/components/Snackbar.vue";

export default {
  components: { Snackbar },
};
</script>
