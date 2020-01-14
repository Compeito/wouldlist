<template>
  <div class="content">
    <b-button @click="login" color="skyblue">login</b-button>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

import firebase from '~/plugins/firebase'

@Component
export default class login extends Vue {
  link: string = "";

  async login() {
    const provider = new firebase.auth.TwitterAuthProvider();
    const loginResponse = await firebase.auth().signInWithPopup(provider);

    const firebaseUser = loginResponse.user;
    const firebaseCredential = loginResponse.credential as firebase.auth.OAuthCredential;
    if (firebaseUser) {
      const token = await firebaseUser.getIdToken();
      const apiResponse: { user: any, isCreated: string } = await this.$axios.post(
        '/users/join',
        {
          accessToken: firebaseCredential.accessToken,
          secret: firebaseCredential.secret
        },
        {
          headers: {'Authorization': `Bearer ${token}`}
        });
      console.log(apiResponse)
    }
  }
}
</script>
