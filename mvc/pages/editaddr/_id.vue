<template>
  <v-layout
    column
  >
  　<v-card>
    <v-subheader> 住所更新 </v-subheader>
    <v-card-text>
      <validation-observer ref="validationObserver" tag="div">
        <AddrIdform :addrObj=addrObj />
      </validation-observer>
    </v-card-text>
    <v-card-actions>
  <v-btn color="primary" @click="submit(addrObj)" >確認</v-btn>
  <v-btn
    color=""
    class="mr-4"
    to="/addrs" nuxt
  >
      一覧に戻る
      </v-btn>
    </v-card-actions>
  　</v-card>
   </v-layout>

</template>

<script lang="ts">
import Vue from 'vue'
import AddrIdform from '~/components/present/addr_id_form.vue'

function params_get(params: any): any {
  return params;
}

export default Vue.extend({
  data () {
    // getterから取得したデータは修正できないので一度コピーする。
    var addrObj =  Object.assign({}, this.$store.getters['getAddr'](this.$route.params.id));
    // 戻った時にデータを戻す。
    if (this.$route.params.addrObj !== undefined) {
      addrObj = params_get(this.$route.params.addrObj);
    }
    return {
      addrObj: addrObj
    }
  },
  components: {
    AddrIdform,
  },
  methods: {
    async submit(addrObj) {
      const isValid = await this.$refs.validationObserver.validate();
      if (!isValid) return false;
      this.$router.push({ name: 'addr_edit_confirm', params: { addrObj: addrObj }});
    }
  }
})
</script>
