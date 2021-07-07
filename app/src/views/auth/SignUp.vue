<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <v-card width="700" class="mx-auto">
        <v-card-title>SIGN UP</v-card-title>
        <v-divider></v-divider>

        <v-alert v-for="(item, index) in errors" :key="index" type="error">
          {{ item }}
        </v-alert>

        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
          style="margin: 20px 30px 0 30px;"
        >
          <v-text-field
            outlined
            v-model="first_name"
            label="First Name"
            :rules="[v => !!v || 'First Name is required']"
            required
          ></v-text-field>

          <v-text-field
            outlined
            v-model="last_name"
            label="Last Name"
            :rules="[v => !!v || 'Last Name is required']"
            required
          ></v-text-field>

          <v-text-field
            outlined
            v-model="username"
            label="Username"
            :rules="[v => !!v || 'Username is required']"
            required
          ></v-text-field>

          <v-text-field
            outlined
            v-model="email"
            label="E-mail"
            :rules="[v => !!v || 'Email is required']"
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
            <v-btn class="mr-4" @click="register" :loading="loading">
              Signup
            </v-btn>
          </v-card-actions>

          <v-card-text style="padding-left:0px">
            Already have an account?
            <router-link to="/sign-in">Log in</router-link>
          </v-card-text>
        </v-form>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Signup",
  data() {
    return {
      valid: false,
      first_name: null,
      last_name: null,
      email: null,
      username: null,
      password: null,
      errors: [],
      loading: false
    };
  },
  methods: {
    async register() {
      if (!this.$refs.form.validate()) {
        return;
      }

      this.loading = true;

      try {
        const { data } = await axios.post("http://127.0.0.1:7000/register/", {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          username: this.username,
          password: this.password
        });

        this.$store.dispatch("setUserToken", data);
        this.$snackbar.showMessage(`Welcome ${this.first_name}!`);
        this.$router.push("app/chat");
      } catch (error) {
        console.error(error.response.data);
        this.errors = error.response.data;
      }

      this.loading = false;
    }
  }
};
</script>
