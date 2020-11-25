<template>
　<v-card>
    <v-subheader> 住所登録 </v-subheader>
    <v-card-text>
       <AddrConfirmForm :addrObj=addrObj />
   </v-card-text>
  <v-card-actions>
    <v-btn color="primary" :to="{ name: 'addr_save', params: { addrObj: addrObj }}" nuxt>保存</v-btn>
    <v-btn color="primary" :to="{ name: 'addr_add', params: { addrObj: addrObj }}" nuxt> 前に戻る</v-btn>
  </v-card-actions>
  </v-card>

</template>

<script lang="ts">
import Vue from 'vue'
import AddrConfirmForm from '~/components/present/addr_form_readonly.vue'

export default Vue.extend({
  data () {
    var addrObj =  this.$route.params.addrObj || {};
    return {
      addrObj: addrObj
    }
  },
  components: {
    AddrConfirmForm,
  }
})
</script>