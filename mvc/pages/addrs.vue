<template>
  <v-layout
    column
    justify-center
    align-center
  >
    <v-card v-if="addrs">
      <v-card-title>
        住所一覧
        <v-spacer />
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="検索"
          sigle-line
        />
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="addrs"
        :items-per-page="10"
        :search="search"
        class="elevation-1"
      >
        <template v-slot:[`item.actions`]="{ item }">
          <v-icon
            small
            @click="$router.push({path: `editaddr/${item.id}`})"
          >
            mdi-pencil
          </v-icon>
          <v-icon
            small
            @click="remove_dialog_open(item)"
          >
            mdi-delete
          </v-icon>
        </template>
      </v-data-table>
    </v-card>
    <div v-else>
      Now you don't
    </div>

  <ConfirmDialog
    ref="confirm"
    title="住所削除"
    :message="deleteMessage"
    buttonMessage="削除"
    @confirm="confirmDeletion"
  >
  </ConfirmDialog>

  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'
import Addr from '~/lib/addr'
import ConfirmDialog from '~/components/present/confirm_dialog.vue'

export default Vue.extend({
  data () {
    let addrs  = this.$store.getters['getAddrs']
    return {
      search: '',
      headers: [
        { text: 'ID', value: 'id' },
        { text: '名前', value: 'name' },
        { text: '住所', value: 'addr' },
        { text: 'IPアドレス', value: 'ipaddr' },
        { text: '操作', value: 'actions' }
      ],
      addrs: addrs,
      deletedItem: {
        name: '',
      },
    }
  },
  computed: {
    deleteMessage() {
      return `${this.deletedItem.name} を削除します。よろしいですか。`
    },
  },
  async asyncData({ params, store, error }) {
    await store.dispatch('fetchNewAddrs');
  },
  methods: {
    remove_dialog_open(addr) {
      this.deletedItem = addr
      this.$refs.confirm.open()
    },
    confirmDeletion () {
      let addr = this.deletedItem;
      const payload = { addr: addr };
      this.$store.dispatch('removeAddrApi', payload);
    },
  }
})
</script>