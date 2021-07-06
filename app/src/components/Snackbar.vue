<template>
  <v-snackbar v-model="show">
    {{ message }}

    <template v-slot:action="{ attrs }">
      <v-btn text v-bind="attrs" @click="show = false">Close</v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      message: "",
    };
  },
  created() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === "setSnackBarMessage") {
        this.message = state.snackbar.snackBarMessage;
        this.show = true;
      }
    });
  },
};
</script>
