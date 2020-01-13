<template>
  <div class="content">
    <pre>
      <code>{{ message }}</code>
    </pre>
    <p>
      <nuxt-link to="/login">login</nuxt-link>
    </p>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

import auth from '~/plugins/auth'

@Component
export default class index extends Vue {
  count: number = 0;
  message: string = "loading...";

  async mounted() {
    const user = await auth();
    if (user) {
      const token = await user.getIdToken();
      const me = await this.$axios.get('/users/me', {
        headers: {'Authorization': `Bearer ${token}`}
      });
      this.message = JSON.stringify(me.data)
    }
  }
}
</script>
