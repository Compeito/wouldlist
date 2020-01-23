<template>
  <sui-container text>
    <sui-card class="fluid">
      <sui-card-content>
        <sui-card-header>hogehoge</sui-card-header>
        <sui-card-description>{{ item.text }}</sui-card-description>
      </sui-card-content>
    </sui-card>
  </sui-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import { Context } from '@nuxt/types'
import Item from '~/schemes/Item'

@Component
export default class item extends Vue {
  item?: Item

  async asyncData (context: Context) {
    const uid = context.query.uid
    const response: { data: { item: Item } } = await context.$axios.get(`/items?uid=${uid}`)
    return response.data
  }
}
</script>
