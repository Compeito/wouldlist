<template>
  <div class="content">
    <b-button @click="logout" color="skyblue">logout</b-button>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

import firebase from '~/plugins/firebase'

@Component
export default class login extends Vue {
  async logout() {
    await firebase.auth().signOut();
  }
}
</script>
