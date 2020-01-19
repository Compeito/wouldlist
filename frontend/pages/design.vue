<template>
  <sui-container>
    <sui-card-group :items-per-row="3" stackable>
      <template v-for="(item, i) in items">
        <nuxt-link :key="i" :to="`/todo?id=${item.title}`" class="ui card raised link">
          <sui-card-content>
            <sui-card-header>{{ item.title }}</sui-card-header>
            <sui-card-description>{{ item.text }}</sui-card-description>
          </sui-card-content>
        </nuxt-link>
      </template>
    </sui-card-group>
  </sui-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

interface TodoItem {
  title: string,
  text: string
}

@Component
export default class design extends Vue {
  items: TodoItem[] = [
    {
      title: 'hoge1',
      text: 'ほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふが'
    },
    {
      title: 'hoge2',
      text: 'ほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふが'
    },
    {
      title: 'hoge3',
      text: 'ほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふが'
    },
    {
      title: 'hoge4',
      text: 'ほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふが'
    },
    {
      title: 'hoge5',
      text: 'ほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふがほげほげふがふが'
    }
  ]
}
</script>
