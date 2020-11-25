<template>
　<v-card>
    <v-subheader> 住所登録 </v-subheader>
    <v-card-text>
      <validation-observer ref="validationObserver" tag="div">
        <AddrForm :addrObj=addrObj />
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
</template>

<script lang="ts">
import Vue from 'vue'
import Addr from '~/lib/addr'
import AddrForm from '~/components/present/addr_form.vue'

function params_get(params: any): any {
  return params;
}

export default Vue.extend({
  data () {
    var addrObj = new Addr();
    // 戻った時にデータを戻す。
    if (this.$route.params.addrObj !== undefined) {
      addrObj = params_get(this.$route.params.addrObj);
    }
    return {
      addrObj: addrObj
    }
  },
  computed: {
  },
  methods: {
    async submit(addrObj) {
      const isValid = await this.$refs.validationObserver.validate();
      if (!isValid) return false;
      this.$router.push({ name: 'addr_confirm', params: { addrObj: addrObj }});
    }
  },
  components: {
    AddrForm,
  },
})
</script>

<style>

</style>