<template>
  <div class="content">
    <sui-button color="blue" @click="login">
      login
    </sui-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class login extends Vue {
  login () {
    const provider = new this.$firebase.auth.TwitterAuthProvider()
    this.$firebase.auth().signInWithRedirect(provider)
  }
}
</script>
