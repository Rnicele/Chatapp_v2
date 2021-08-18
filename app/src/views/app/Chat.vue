
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
                @click="setSelectedUser(user); scrollToBottom;"

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
          <div class="body semi-full-height chat-body" style="max-height: 943px;">
            
            <v-container class="fill-height div-scroll" id="container" ref="container">
              <v-row class="fill-height pb-14" align="end">
                <v-col>
                  <v-list>
                    <v-list-item
                      class="px-0"
                      v-for="(chat, index) in getChats"
                      :key="index"
                    >
                      <template v-if="chat.user === selectedUser.id" class="chat-item" > 
                        <v-list-item-avatar>
                          <v-img :src="selectedUser.avatar || getUsersDefaultAvatar"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
                          <v-list-item-title
                            class="v-list-style"
                            v-text="chat.message"
                          ></v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-content></v-list-item-content>
                      </template>

                      <template v-else class="chat-item">
                        
                        <v-list-item-content></v-list-item-content>
                        <v-list-item-content>
                          <v-list-item-title
                            class="text-right v-list-style"
                            v-text="chat.message"
                          ></v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-avatar class="v-avatar">
                          <v-img :src="loginUser.avatar || getUsersDefaultAvatar"></v-img>
                        </v-list-item-avatar>
                        
                      </template>
                    </v-list-item>
                  </v-list>
                </v-col>
              </v-row>
            </v-container>
            <v-footer>
              <v-container class="ma-0 pa-0">
                <v-row no-gutters>
                  <v-col>
                    <div class="d-flex flex-row align-center">
                      <v-text-field
                        v-model="message"
                        @keypress.enter="send"
                        placeholder="Type Something"
                      ></v-text-field>
                      <v-btn icon class="ml-4" @click="send">
                        <v-icon>mdi-send</v-icon>
                      </v-btn>
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
import { mapGetters, mapActions } from "vuex";

export default {
  
  data: () => ({
    selectedUser: null,
    message: "",
    loginUser: null,
  }),
  mounted() {
    this.$store.dispatch("setUsers");
  },
  methods: {
    ...mapActions(["signOut", "setRoom", "sendChat"]),
    setSelectedUser(user) {
      this.selectedUser = user;
      this.setRoom({ uid: this.getUser.id, 
      cuid: user.id });
      this.loginUser = this.getUser;
      setTimeout(() => {
        const container = this.$refs.container;
        container.scrollTop = container.scrollHeight;
      }, 100);
    },
    send() {
      this.sendChat({ message: this.message, user: this.getUser.id });
      this.message = "";
      setTimeout(() => {
        const container = this.$refs.container;
        container.scrollTop = container.scrollHeight;
      }, 100);
    },
  },
  computed: {
    ...mapGetters([
      "getUsers",
      "getUsersDefaultAvatar",
      "getUsersLoading",
      "getUser",
      "getChats"
    ])
  },
  
  filters: {
    fullName(user) {
      return `${user.first_name} ${user.last_name}`;
    }
  }
};
</script>

<style lang="scss" scoped>
.chat-item {
  overflow: hidden;
}
.v-list-style {
   vertical-align: top;
   white-space: normal;
}
.div-scroll {
    //overflow: scroll;
    height: 100%;
    max-height: 100%;
    overflow-y: scroll;
}

.full-height {
  height: 100%;
  max-height: 949px;
}
.semi-full-height {
  height: 85%;
  max-height: 85%;
}
.v-card-custom {
  margin: 0 0.5%;
  height: 100%;
}
.v-card-width-1 {
  width: 19%;
}
.v-card-width-2 {
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
.v-avatar {
  margin-right: 10px;
}
.v-title {
  font-size: 17px !important;
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
