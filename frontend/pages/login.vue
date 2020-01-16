<template>
  <div class="content">
    <b-button color="skyblue" @click="login">
      login
    </b-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

import firebase from '~/plugins/firebase'

@Component
export default class login extends Vue {
  async login () {
    const provider = new firebase.auth.TwitterAuthProvider()
    await firebase.auth().signInWithPopup(provider)
  }
}
</script>
