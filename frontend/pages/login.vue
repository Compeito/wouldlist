<template>
  <div class="content">
    <b-button @click="login" color="skyblue">login</b-button>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

import firebase from '~/plugins/firebase'
import auth from "~/plugins/auth";

@Component
export default class login extends Vue {
  link: string = "";

  async login() {
    const provider = new firebase.auth.TwitterAuthProvider();
    await firebase.auth().signInWithPopup(provider);
    const user = await auth();
    console.log(user)
  }
}
</script>
