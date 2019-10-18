<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <v-layout column>
              <v-list-item>
                <v-list-item-content>
                  <!-- <v-list-item-subtitle style="white-space:initial">{{ name }}</v-list-item-subtitle> -->
                  <v-list-item-title class="headline" style="white-space:initial">{{ main.name }}</v-list-item-title>
                  <v-list-item-subtitle style="white-space:initial">
                    <span>{{ sideStr }}</span>
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-card-text>
                <v-layout justify-center>
                  <div class="grey--text ml-4">{{ kcal }} kcal</div>
                </v-layout>
              </v-card-text>
              <v-card-text>
                <v-layout justify-center>
                  <v-img :src="main.image" max-width="200px" />
                </v-layout>
              </v-card-text>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      default: ""
    },
    kcal: {
      type: Number,
      default: 0
    },
    main: {
      type: Object,
      default: () => ({
        name: "",
        image: "",
        kcal: 0
      })
    },
    side: {
      type: Array,
      default: () => new Array()
    }
  },
  computed: {
    sideStr() {
      return this.side.map(s => s.name).join(" / ");
    }
  }
};
</script>
