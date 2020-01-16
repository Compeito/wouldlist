<template>
  <div class="content">
    <b-button color="skyblue" @click="logout">
      logout
    </b-button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

import firebase from '~/plugins/firebase'

@Component
export default class login extends Vue {
  async logout () {
    await firebase.auth().signOut()
  }
}
</script>
