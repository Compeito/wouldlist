import { Plugin, Context } from '@nuxt/types'
import { Vue } from 'nuxt-property-decorator'
import * as firebase from 'firebase/app'
import 'firebase/auth'

declare module 'vue/types/vue' {
  interface Vue {
    $firebase: typeof firebase
  }
}
declare module '@nuxt/types' {
  interface Context {
    $firebase: typeof firebase
  }
}

const firebasePlugin: Plugin = (context: Context) => {
  if (!firebase.apps.length) {
    firebase.initializeApp(
      {
        apiKey: 'AIzaSyB_ZELI1qiYaIpy7WJiY70nBq2lI1e5Hb4',
        authDomain: 'wouldlist.firebaseapp.com',
        databaseURL: 'https://wouldlist.firebaseio.com',
        projectId: 'wouldlist',
        storageBucket: 'wouldlist.appspot.com',
        messagingSenderId: '345931972879',
        appId: '1:345931972879:web:5380f8c7663c9ac9d53e7a'
      }
    )
    context.$firebase = firebase
    Vue.prototype.$firebase = firebase
  }
}

export default firebasePlugin
