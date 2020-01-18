<template>
  <div class="content">
    <pre><code>{{ message }}</code></pre>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class index extends Vue {
  message: string = 'loading...';

  mounted () {
    this.$axios.get('/users/me')
      .then((response) => {
        this.message = JSON.stringify(response.data, null, 2)
      }).catch((error) => {
        this.message = error
      })
  }
}
</script>
