import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class PreloadVue extends Vue {
  mounted () {
    this.$nextTick(async () => {
      this.$nuxt.$loading.start()
      await this.preload()
      this.$nuxt.$loading.finish()
    })
  }

  async preload () {

  }
}
