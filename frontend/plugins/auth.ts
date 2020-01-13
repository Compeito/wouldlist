import {User} from 'firebase/app'
import firebase from '~/plugins/firebase'

function auth() {
  return new Promise<User | null>((resolve, reject) => {
    firebase.auth().onAuthStateChanged((user) => {
      resolve(user)
    })
  })
}

export default auth
