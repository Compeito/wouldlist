<template>
  <div class="content">
    <sui-button @click="logout">
      logout
    </sui-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class login extends Vue {
  async logout () {
    await this.$firebase.auth().signOut()
  }
}
</script>
