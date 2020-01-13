import * as firebase from 'firebase/app'
import 'firebase/auth'

if (!firebase.apps.length) {
  firebase.initializeApp(
    {
      apiKey: "AIzaSyB_ZELI1qiYaIpy7WJiY70nBq2lI1e5Hb4",
      authDomain: "wouldlist.firebaseapp.com",
      databaseURL: "https://wouldlist.firebaseio.com",
      projectId: "wouldlist",
      storageBucket: "wouldlist.appspot.com",
      messagingSenderId: "345931972879",
      appId: "1:345931972879:web:5380f8c7663c9ac9d53e7a",
    }
  )
}

export default firebase
