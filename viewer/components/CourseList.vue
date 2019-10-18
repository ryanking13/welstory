<template>
  <v-container class="pa-2 col-xs-10 col-sm-10 col-md-6" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="course in courses" :key="course.course" pa-5>
        <CourseCard
          :name="course.course"
          :kcal="course.kcal"
          :main="course.main"
          :side="course.side"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import CourseCard from "./CourseCard";
export default {
  components: {
    CourseCard
  },
  props: {
    courses: {
      type: Array,
      default: () => new Array()
    }
  }
};
</script>
