<template>
  <div class="content">
    <p>{{ message }}</p>
    <p>
      <nuxt-link to="/login">login</nuxt-link>
    </p>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'

@Component
export default class index extends Vue {
  count: number = 0;
  message: string = "loading...";

  async mounted() {
    const response = await this.$axios.get('/users');
    this.message = JSON.stringify(response.data)
  }
}
</script>
