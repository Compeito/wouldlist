import { Plugin } from '@nuxt/types'
import auth from '~/plugins/auth'

const axiosPlugin: Plugin = async ({ $axios }) => {
  const user = await auth()
  if (user) {
    const token = await user.getIdToken()
    $axios.setToken(token, 'Bearer')
  }
}

export default axiosPlugin
