<template>
  <section class="section">
    <div class="columns is-mobile">
      <b-button @click="increment">{{ count }}</b-button>
    </div>
  </section>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'

@Component
export default class index extends Vue {
  count: number = 0;

  increment(): void {
    this.count++;
  }
}
</script>
