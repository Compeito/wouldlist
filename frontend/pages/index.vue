<template>
  <div class="content">
    <pre><code>{{ message }}</code></pre>
  </div>
</template>

<script lang="ts">
import { Component } from 'nuxt-property-decorator'
import PreloadVue from '~/components/PreloadVue'

@Component
export default class index extends PreloadVue {
  message: string = 'loading...';

  async preload () {
    const response = await this.$axios.get('/users/me')
    this.message = JSON.stringify(response.data, null, 2)
  }
}
</script>
