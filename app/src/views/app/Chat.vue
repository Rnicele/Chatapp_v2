<template>
  <div class="chat" style="height: 100%;">
    <v-container fill-height fluid>
      <v-card elevation="1" width="19%" style="margin: 0 0.5%;height: 100%;">
        <div class="header" style="margin: 0 10px">
          <h1>Chat</h1>
          <v-divider></v-divider>
        </div>
        <div class="body" style="margin: 0 10px 10px 10px;">
          <v-list dense>
            <v-list-item-group
              v-model="selectedItem"
              color="primary"
            >
              <v-list-item
                v-for="(item, i) in items"
                :key="i" @click="chatName(item)"
              >
                <v-list-item-icon style="margin-right: 10px;">
                  <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="item.text" style="font-size: 17px;"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
      </v-card>
      <v-card elevation="1" width="79%" style="margin: 0 0.5%;height: 100%;">
        <div v-if="hasClick" style="height: 100%;">
          <div class="header" style="margin: 0 10px">
            <h1 v-text="name"></h1>
            <v-divider></v-divider>
          </div>
          <div class="body" style="margin: 0 10px 10px 10px;height: 85%;">
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
                      <v-text-field v-model="msg" placeholder="Type Something" @keypress.enter="send"></v-text-field>
                      <v-btn icon class="ml-4" @click="send"><v-icon>mdi-send</v-icon></v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-container>
            </v-footer>
          </div>
        </div>
        <div v-else style="height: 100%;">
          <div class="body" style="margin: 0 10px 10px 10px;height: 100%;">
            <h1 style="text-align: center;padding: 100px;padding-top: 450px;"> NO MESSAGES </h1>
          </div>
        </div>
      </v-card>
      
    </v-container>
  </div>
</template>

<script>
  export default {
    data: () => ({
      hasClick: false,
      items: [
        { text: 'Juan Dela Cruz', icon: 'mdi-account' },
        { text: 'Coco Martin', icon: 'mdi-account' },
        { text: 'Tao po', icon: 'mdi-account' },
      ],
      name: '',
    }),
    methods: {
      async chatName(name){
        this.hasClick = true;
        console.log("click", name)
        this.name = name.text;
      }
    }
  }

  
</script>
