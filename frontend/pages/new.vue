<template>
  <sui-container text>
    <sui-form>
      <sui-form-field>
        <label>
          内容
          <textarea v-model="text" maxlength="200" :style="textareaStyle" />
          <span>{{ text.length }}/200</span>
        </label>
      </sui-form-field>
      <sui-button :loading="isLoading" type="button" @click="submit">
        作成！
      </sui-button>
    </sui-form>
  </sui-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import Item from '~/schemes/Item'

@Component
export default class New extends Vue {
  text: string = ''
  isLoading: boolean = false

  get textareaStyle () {
    return '' +
      'resize: none;' +
      `height: ${this.text.split('\n').length * 20}px;`
  }

  async submit () {
    if (this.isLoading) {
      return
    }
    this.isLoading = true
    const response: { data: { item: Item } } = await this.$axios.post(`/items/create?text=${this.text}`)
    this.$router.push(`/view?uid=${response.data.item.uid}`)
  }
}
</script>
