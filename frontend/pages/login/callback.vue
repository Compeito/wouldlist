<template>
  <div class="content">
    <b-button>logged in</b-button>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

@Component
export default class callback extends Vue {
  mounted() {
    this.$axios.post('/login/callback' + location.search, null, {withCredentials: true})
      .then((result) => {
        console.log(result)
      })
  }
}
</script>
