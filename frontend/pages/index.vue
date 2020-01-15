<template>
  <div class="content">
    <pre><code>{{ message }}</code></pre>
    <p>
      <nuxt-link to="/login">login</nuxt-link>
    </p>
    <p>
      <nuxt-link to="/logout">logout</nuxt-link>
    </p>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "nuxt-property-decorator";

@Component
export default class index extends Vue {
  count: number = 0;
  message: string = "loading...";

  async mounted() {
    const me = await this.$axios.get("/users/me");
    this.message = JSON.stringify(me.data, null, 2);
  }
}
</script>
