import { Context, Plugin } from '@nuxt/types'
import { Vue } from 'nuxt-property-decorator'
import { User } from 'firebase/app'

declare module 'vue/types/vue' {
  interface Vue {
    $user: User | null
  }
}

declare module '@nuxt/types' {
  interface Context {
    $user: User | null
  }
}

const authPlugin: Plugin = (context: Context) => {
  return new Promise<void>((resolve, reject) => {
    try {
      context.$firebase.auth().onAuthStateChanged((user) => {
        Vue.prototype.$user = user
        context.$user = user
        resolve()
      })
    } catch (e) {
      reject(e)
    }
  })
}

export default authPlugin
