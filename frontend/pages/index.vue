<template>
  <div class="content">
    <pre><code>{{ message }}</code></pre>
  </div>
</template>

<script lang="ts">
import { Context } from '@nuxt/types'
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class index extends Vue {
  message: string = 'loading...'

  async asyncData (context: Context) {
    const response = await context.$axios.get('/users/me')
    const message = JSON.stringify(response.data, null, 2)
    return { message }
  }
}
</script>
