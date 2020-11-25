<template>
     <form>
        <v-text-field
            v-model="addrObj.name"
            label="名前"
            readonly
        />
        <v-text-field
            v-model="addrObj.addr"
            label="住所"
            readonly
        />
        <v-text-field
            v-model="addrObj.ipaddr"
            label="IPアドレス"
            readonly
        />
      </form>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue';
import Addr from '~/lib/addr';

export default Vue.extend({
  props: {
    addrObj: {
      type: Object,
    } as PropOptions<Addr>,
  },
})
</script>