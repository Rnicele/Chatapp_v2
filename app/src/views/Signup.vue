<template>
    <v-container fill-height fluid>
        <v-row align="center" justify="center">
            <v-card width="700" class="mx-auto">
                <v-card-title>SIGN UP</v-card-title>
                <v-divider></v-divider>
                <v-form 
                    ref="form"
                    v-model="valid"
                    lazy-validation style="margin: 20px 30px 0 30px;"
                >
                    <v-text-field outlined
                    v-model="first_name"
                    label="First Name"
                    :rules="[v => !!v || 'First Name is required']"
                    required
                    ></v-text-field>

                    <v-text-field outlined
                    v-model="last_name"
                    label="Last Name"
                    :rules="[v => !!v || 'Last Name is required']"
                    required
                    ></v-text-field>

                    <v-text-field outlined
                    v-model="username"
                    label="Username"
                    :rules="[v => !!v || 'Username is required']"
                    required
                    ></v-text-field>

                    <v-text-field outlined
                    v-model="email"
                    label="E-mail"
                    :rules="[v => !!v || 'Email is required']"
                    required
                    ></v-text-field>

                    <v-text-field outlined
                    v-model="password1"
                    type="password"
                    label="Password"
                    :rules="[v => !!v || 'Password is required']"
                    required
                    ></v-text-field>

                    <v-text-field outlined
                    v-model="password2"
                    type="password"
                    label="Confirm Password"
                    :rules="[v => !!v || 'Confirm Password is required']"
                    required
                    ></v-text-field>

                    <v-card-actions>
                        <v-btn class="mr-4">
                        Signup
                        </v-btn>
                    </v-card-actions>
                    
                    <v-card-text style="padding-left:0px">
                        Already have an account? <a href="#/Signin"> Log in </a>
                    </v-card-text>
                </v-form>
                
            </v-card>
        </v-row>
     </v-container>
</template>