<template>
  <v-layout
    column
    justify-center
    align-center
  >
    <v-flex
      xs12
      sm8
      md6
    >
      <v-card>
        <v-card-title class="headline">
          ユーザ一覧サンプル
        </v-card-title>
        <v-btn color="primary" to="/addrs" nuxt>住所一覧</v-btn>
        <v-btn color="primary" to="/addr_add" nuxt>住所登録</v-btn>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  components: {
  }
})

</script>
