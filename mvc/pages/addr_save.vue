<template>
　<v-card>
    <v-subheader> 住所登録(完了) </v-subheader>
    <v-card-text>
       <AddrIdReadOnlyForm :addrObj=addrObj />
   </v-card-text>
  <v-card-actions>
    <v-btn color="primary" to="/addrs" nuxt>一覧に戻る</v-btn>
  </v-card-actions>
  </v-card>

</template>

<script lang="ts">
import Vue from 'vue'

import AddrIdReadOnlyForm from '~/components/present/addr_id_readonly_form.vue'
import Addr,{AddrView} from '~/lib/addr'
import ApiClient from '~/lib/api'

export default Vue.extend({
  data () {
  },
  async asyncData({ params, $axios }) {
    let api = new ApiClient();
    var addrObj =  params.addrObj || {};
    const response = await api.post($axios, 'create', addrObj);
    addrObj = response.Result;
    return {
      addrObj: addrObj
    }
  },
  components: {
    AddrIdReadOnlyForm,
  }
})
</script>