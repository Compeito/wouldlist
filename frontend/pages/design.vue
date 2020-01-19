<template>
  <sui-container text>
    <button class="ui button" @click="store.increment()">
      {{ store.count }}
    </button>
    <nuxt-link to="/design2">
      design2
    </nuxt-link>
  </sui-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import storeInstance from '~/store/index'

@Component
export default class design extends Vue {
  store = storeInstance
}
</script>
