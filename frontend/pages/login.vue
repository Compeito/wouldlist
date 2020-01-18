<template>
  <div class="content">
    <sui-button color="blue" @click="login">
      login
    </sui-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

import firebase from '~/plugins/firebase'

@Component
export default class login extends Vue {
  login () {
    const provider = new firebase.auth.TwitterAuthProvider()
    firebase.auth().signInWithRedirect(provider)
  }
}
</script>
