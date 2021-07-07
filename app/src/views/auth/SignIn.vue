<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <v-card width="700" class="mx-auto">
        <v-card-title>SIGN IN</v-card-title>
        <v-divider></v-divider>

        <v-alert v-if="hasError" type="error"
          >Username or password is incorrect.
        </v-alert>

        <v-form
          ref="form"
          v-model="valid"
          :disabled="loading"
          lazy-validation
          class="mx-7 my-5"
        >
          <v-text-field
            outlined
            v-model="username"
            label="Username"
            :rules="[v => !!v || 'Username is required']"
            required
          ></v-text-field>

          <v-text-field
            outlined
            v-model="password"
            type="password"
            label="Password"
            :rules="[v => !!v || 'Password is required']"
            required
          ></v-text-field>

          <v-card-actions>
            <v-btn class="mr-4" @click="login" :loading="loading">
              Login
            </v-btn>
          </v-card-actions>

          <v-card-text style="padding-left:0px">
            Don't have an account?
            <router-link to="/sign-up">Sign up</router-link>
          </v-card-text>
        </v-form>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Signin",
  data() {
    return {
      username: null,
      password: null,
      valid: false,
      hasError: false,
      loading: false
    };
  },
  methods: {
    async login() {
      if (!this.$refs.form.validate()) {
        return;
      }

      this.loading = true;

      try {
        const { data } = await axios.post("http://127.0.0.1:7000/login/", {
          username: this.username,
          password: this.password
        });
        this.$store.dispatch("setUserToken", data);
        this.$snackbar.showMessage("Signed in successfully.");
        this.$router.push("chat");
      } catch (error) {
        this.hasError = true;
        console.error(error.response.data);
      }

      this.loading = false;
    }
  }
};
</script>
