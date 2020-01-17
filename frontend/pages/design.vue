<template>
  <sui-container text>
    <button class="ui button">
      ボタン
    </button>
    <div class="ui button" tabindex="0">
      フォーカス可能
    </div>
  </sui-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class design extends Vue {
}
</script>
