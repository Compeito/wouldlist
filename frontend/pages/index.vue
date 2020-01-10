<template>
  <div class="content">
    <p>{{ message }}</p>
    <b-button @click="increment">{{ count }}</b-button>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'nuxt-property-decorator'


@Component
export default class index extends Vue {
  count: number = 0;
  message: string = "loading...";

  mounted() {
    interface YesNoResponse {
      answer: string,
      forced: boolean,
      image: string,
    }

    this.$axios.get('https://yesno.wtf/api')
      .then((result: { data: YesNoResponse }) => {
        this.message = result.data.answer;
      })
  }

  increment(): void {
    this.count++;
  }
}
</script>
