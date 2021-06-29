<template>
    <v-container fill-height fluid>
        <v-row align="center" justify="center">
            <v-card width="700" class="mx-auto">
                <v-card-title>SIGN UP</v-card-title>
                <v-divider></v-divider>
                <v-form 
                    ref="form"
                    v-model="valid"
                    lazy-validation style="margin: 20px 30px 0px 30px;"
                >
                    <v-text-field outlined
                    v-model="username"
                    label="Username"
                    :rules="[v => !!v || 'Username is required']"
                    required
                    ></v-text-field>

                    <v-text-field outlined
                    v-model="password"
                    type="password"
                    label="Password"
                    :rules="[v => !!v || 'Password is required']"
                    required
                    ></v-text-field>

                    <v-card-actions>
                        <v-btn class="mr-4" @click="login()">
                        Login
                        </v-btn>
                    </v-card-actions>
                    
                    <v-card-text style="padding-left:0px">
                        Don't have an account? <a href="#/Signup"> Sign up </a>
                    </v-card-text>
                </v-form>
                
            </v-card>
        </v-row>
     </v-container>
</template>

<script>
import axios from "axios"

  export default {
    name: 'Signin',
    data: function () {
        return {
            username: '',
            password: '',
            valid: false
        }
    },
    methods: {
        async login(){
            console.log("login")
            try {
                const userLogin = await axios.post('http://127.0.0.1:7000/login/', {
                    username: this.username,
                    password: this.password,
                });

                localStorage.setItem("auth", JSON.stringify(userLogin));
                this.$router.push('Chat')
                
            } catch (error) {
                alert(error.response.data);
            }
        }
    }
  }
</script>
