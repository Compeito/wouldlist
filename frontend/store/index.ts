import { VuexModule, Module, Mutation, Action } from 'vuex-module-decorators'

@Module
export default class Posts extends VuexModule {
  count: number = 0

  @Mutation
  increment (x: number) {
    this.count = x
  }

  @Action({ commit: 'increment' })
  addOne () {
    return 1
  }
}
