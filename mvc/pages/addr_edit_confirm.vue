<template>
　<v-card>
    <v-subheader> 住所更新 </v-subheader>
    <v-card-text>
       <AddrIdReadOnlyForm :addrObj=addrObj />
   </v-card-text>
  <v-card-actions>
    <v-btn color="primary" :to="{ name: 'addr_edit_save', params: { addrObj: addrObj }}" nuxt>保存</v-btn>
    <v-btn color="primary" :to="{ name: 'editaddr-id', params: { addrObj: addrObj }}" nuxt> 前に戻る</v-btn>
  </v-card-actions>
  </v-card>

</template>

<script lang="ts">
import Vue from 'vue'
import AddrIdReadOnlyForm from '~/components/present/addr_id_readonly_form.vue'

export default Vue.extend({
  data () {
    var addrObj =  this.$route.params.addrObj || {};
    return {
      addrObj: addrObj
    }
  },
  components: {
    AddrIdReadOnlyForm,
  }
})
</script>