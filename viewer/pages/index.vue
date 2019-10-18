<template>
  <v-app id="app">
    <github-ribbon />
    <v-container text-center>
      <div class="display-1 pa-10">
        <span class="maintitle">
          웰스토리
          <wbr />식단 뷰어
        </span>
      </div>
      <v-layout justify-center align-center>
        <v-flex xs8 sm6 fill-height>
          <v-select v-model="restaurant" :items="restaurantNames" label="식당" />
          <v-menu
            v-model="menu"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field v-model="date" label="날짜" readonly v-on="on"></v-text-field>
            </template>
            <v-date-picker v-model="date" @input="menu = false"></v-date-picker>
          </v-menu>
          <v-select v-model="mealType" :items="mealTypeNames" label="종류" />
          <v-layout justify-center pa-10>
            <v-btn large color="green white--text" @click="onSearch" :loading="loading">Go!</v-btn>
          </v-layout>
        </v-flex>
      </v-layout>
      <CourseList :courses="courses" />
    </v-container>
  </v-app>
</template>

<script>
import GithubRibbon from "../components/GithubRebbon";
import CourseList from "../components/CourseList";
import axios from "axios";

export default {
  data: () => ({
    menu: false,
    courses: [],
    restaurant: "전자서울대연구소",
    date: new Date().toJSON().slice(0, 10),
    mealType: "점심",
    loading: false,

    restaurants: {
      멀티캠퍼스: "REST000133",
      전자서울대연구소: "REST000176"
    },
    mealTypes: {
      아침: "1",
      점심: "2",
      저녁: "3"
    }
  }),
  components: {
    GithubRibbon,
    CourseList
  },
  computed: {
    restaurantNames() {
      return Object.keys(this.restaurants);
    },
    restaurantCode() {
      return Object.entries(this.restaurants).filter(
        r => r[0] === this.restaurant
      )[0][1];
    },
    mealTypeNames() {
      return Object.keys(this.mealTypes);
    },
    mealTypeCode() {
      return this.mealTypes[this.mealType];
    },
    dateStr() {
      return this.date.replace(/-/g, "");
    }
  },
  methods: {
    onSearch: async function() {
      const params = {
        code: this.restaurantCode,
        date: this.dateStr,
        mealType: this.mealTypeCode
      };
      this.loading = true;
      const courses = await axios.get(
        "https://welstory.azurewebsites.net/api/getcourse/",
        {
          params
        }
      );
      this.courses = courses.data.filter(d => d.type === this.mealTypeCode);
      this.loading = false;
    }
  }
};
</script>

<style>
.maintitle {
  font-family: "Do Hyeon", sans-serif;
}
</style>