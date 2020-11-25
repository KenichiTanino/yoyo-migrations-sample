<template>
     <form>
        <v-text-field
            v-model="addrObj.id"
            label="ID"
            readonly
        />
        <validation-provider v-slot="{ errors }" rules="required" name="名前" >
        <v-text-field
            v-model="addrObj.name"
            label="名前"
            :error-messages="errors"
        />
        </validation-provider>
        <v-text-field
            v-model="addrObj.addr"
            label="住所"
        />
        <validation-provider v-slot="{ errors }" rules="required|ipaddr" name="IPアドレス" >
        <v-text-field
            v-model="addrObj.ipaddr"
            label="IPアドレス"
            :error-messages="errors"
        />
        </validation-provider>
      </form>
</template>
<script lang="ts">
import Vue, { PropOptions } from 'vue';
import {AddrView} from '~/lib/addr';

export default Vue.extend({
  props: {
    addrObj: {
      type: Object,
    } as PropOptions<AddrView>,
  },
})
</script>
