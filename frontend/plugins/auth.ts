import firebase from '~/plugins/firebase'

function auth() {
  return new Promise<firebase.User | null>((resolve, reject) => {
    firebase.auth().onAuthStateChanged((user) => {
      resolve(user)
    })
  })
}

export default auth
