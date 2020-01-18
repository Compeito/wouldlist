<template>
  <sui-dimmer ref="dimmer" :active="loading">
    <sui-loader size="big">
      読み込み中...
    </sui-loader>
  </sui-dimmer>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class Loading extends Vue {
  loading:boolean =false

  start () {
    this.loading = true
  }

  finish () {
    const $dimmer = this.$refs.dimmer as Vue
    $dimmer.$el.classList.add('preload-finished')
    setTimeout(() => {
      this.loading = false
    }, 500)
  }
}
</script>

<style>
.preload-finished {
  animation: 0.5s finished;
}

@keyframes finished {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>
