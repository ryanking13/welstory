<template>
  <div class="text-center">
    <v-dialog v-model="on" width="500">
      <v-card>
        <v-card-title class="headline lighten-2" primary-title>Error</v-card-title>

        <v-card-text>문제가 발생했습니다.</v-card-text>
        <v-card-text>개발자(def6488@gmail.com)에게 알려주세요</v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green" text @click="onClose">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  props: {
    onClose: {
      type: Function,
      default: () => {}
    },
    on: {
      type: Boolean,
      default: true
    }
  }
};
</script>