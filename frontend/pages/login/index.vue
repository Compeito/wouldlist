<template>
  <div class="content">
    loading...
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

@Component
export default class index extends Vue {
  mounted() {
    this.$axios.get('/login', {withCredentials: true})
      .then((result: { data: { url: string } }) => {
        if (result.data.url) {
          location.href = result.data.url
        }
      })
  }
}
</script>
