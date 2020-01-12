<template>
  <div class="content">
    <template v-if="link">
      <a :href="link">login</a>
    </template>
    <template v-else>
      loading...
    </template>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

@Component
export default class index extends Vue {
  link: string = "";

  mounted() {
    this.$axios.get('/login', {withCredentials: true})
      .then((result: { data: { url: string } }) => {
        if (result.data.url) {
          this.link = result.data.url
        }
      })
  }
}
</script>
