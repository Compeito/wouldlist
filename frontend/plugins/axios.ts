import { Context, Plugin } from '@nuxt/types'
import { AxiosRequestConfig } from 'axios'

import auth from '~/plugins/auth'

const axiosPlugin: Plugin = (context: Context) => {
  context.$axios.interceptors.request.use(async (config: AxiosRequestConfig) => {
    const user = await auth()
    if (user) {
      const token = await user.getIdToken()
      config.headers.common.Authorization = `Bearer ${token}`
    }
    return config
  })
}

export default axiosPlugin
