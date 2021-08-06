<template>
  <div class="chat full-height">
    <v-container fill-height fluid>
      <v-card elevation="1" class="v-card-custom v-card-width-1">
        <div class="header">
          <h1>Chat</h1> 
          <v-btn icon class="ml-4" @click="signOut">
            <v-icon>mdi-logout-variant</v-icon>
          </v-btn>
          <v-divider></v-divider>
        </div>
        <div class="body">
          <v-list dense>
            <v-list-item-group color="primary">
              <v-list-item
                v-for="user in getUsers"
                :key="user.id"
                @click="setSelectedUser(user)"
              >
                <v-list-item-avatar class="v-avatar">
                  <v-img :src="user.avatar || getUsersDefaultAvatar"></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title class="v-title">
                    {{ user | fullName }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
      </v-card>
      <v-card elevation="1" class="v-card-custom v-card-width-2">
        <div class="full-height" v-if="selectedUser">
          <div class="header">
            <h1>{{ selectedUser | fullName }}</h1>
            <v-divider></v-divider>
          </div>
          <div class="body semi-full-height">
            <v-container class="fill-height">
              <v-row class="fill-height pb-14" align="end">
                <!-- <v-col>
                  <div v-for="(item, index) in chat" :key="index"
                      :class="['d-flex flex-row align-center my-2', item.from == 'user' ? 'justify-end': null]">
                    <span v-if="item.from == 'user'" class="blue--text mr-3">{{ item.msg }}</span>
                    <v-avatar :color="item.from == 'user' ? 'indigo': 'red'" size="36">
                      <span class="white--text">{{ item.from[0] }}</span>
                    </v-avatar>
                    <span v-if="item.from != 'user'" class="blue--text ml-3">{{ item.msg }}</span>
                  </div>
                </v-col> -->
              </v-row>
            </v-container>

            <v-footer>
              <v-container class="ma-0 pa-0">
                <v-row no-gutters>
                  <v-col>
                    <div class="d-flex flex-row align-center">
                      <!-- <v-text-field v-model="msg" placeholder="Type Something" @keypress.enter="send"></v-text-field>
                      <v-btn icon class="ml-4" @click="send"><v-icon>mdi-send</v-icon></v-btn> -->
                      <v-text-field placeholder="Type Something"></v-text-field>
                      <v-btn icon class="ml-4"><v-icon>mdi-send</v-icon></v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-container>
            </v-footer>
          </div>
        </div>
        <div v-else>
          <div class="body full-height">
            <h1>
              NO MESSAGES
            </h1>
          </div>
        </div>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import { mapGetters, mapActions} from "vuex";

export default {
  data: () => ({
    selectedUser: null
  }),
  mounted() {
    this.$store.dispatch("setUsers");
  },
  methods: {
    ...mapActions(["signOut","setChats"]),
    setSelectedUser(user){

      console.log(this.getUser.id, user.id);
      this.selectedUser = user;

      this.setChats({uid: this.getUser.id, cuid: user.id});
    } 
  },
  computed: {
    ...mapGetters(["getUsers", "getUsersDefaultAvatar", "getUsersLoading", "getUser"])
  },
  filters: {
    fullName(user) {
      return `${user.first_name} ${user.last_name}`;
    }
  }
};
</script>

<style lang="scss" scoped>
// classes

.full-height {
  height: 100%;
}
.semi-full-height{
  height: 85%;
}
.v-card-custom {
  margin: 0 0.5%;
  height: 100%;
}
.v-card-width-1{
  width: 19%; 
}
.v-card-width-2{
  width: 79%; 
}
.body {
  margin: 0 10px 10px 10px;
  h1 {
    text-align: center;
    padding: 100px;
    padding-top: 450px;
  }
}
.v-avatar{
  margin-right: 10px;
}
.v-title{
  font-size: 17px!important;
}
.header {
  margin: 0 10px;
  button {
    right: 0;
    position: absolute;
    padding: 10px;
    margin: 5px;
  }
  h1 {
    display: inline-block;
  }
}
</style>
