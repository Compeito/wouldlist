import { User } from 'firebase/app'
import firebase from '~/plugins/firebase'

function auth () {
  return new Promise<User>((resolve, reject) => {
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        resolve(user)
      } else {
        reject(user)
      }
    })
  })
}

export default auth
