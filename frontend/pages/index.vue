<template>
  <div class="content">
    <p>{{ message }}</p>
    <b-button @click="increment">{{ count }}</b-button>
    <nuxt-link to="/login">login</nuxt-link>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

@Component
export default class index extends Vue {
  count: number = 0;
  message: string = "loading...";

  increment(): void {
    this.count++;
  }
}
</script>
