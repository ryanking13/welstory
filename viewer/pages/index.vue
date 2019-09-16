<template>
  <v-app id="app">
    <github-ribbon />
    <CourseList :courses="courses" />
    <v-layout justify-center align-center pa-10>
      <v-btn large color="green white--text" @click="onSearch">Search</v-btn>
    </v-layout>
  </v-app>
</template>

<script>
import GithubRibbon from "../components/GithubRebbon";
import CourseList from "../components/CourseList";
import axios from "axios";

export default {
  data: () => ({
    courses: []
  }),
  components: {
    GithubRibbon,
    CourseList
  },
  methods: {
    onSearch: async function(params) {
      const courses = await axios.get(
        "https://welstory.azurewebsites.net/api/getcourse/",
        {
          params
        }
      );
      this.courses = JSON.parse(courses);
    }
  }
};
</script>

