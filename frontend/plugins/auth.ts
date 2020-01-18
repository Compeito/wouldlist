import { User } from 'firebase/app'
import firebase from '~/plugins/firebase'

function auth () {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  return new Promise<User | null>((resolve, reject) => {
    firebase.auth().onAuthStateChanged((user) => {
      resolve(user)
    })
  })
}

export default auth
