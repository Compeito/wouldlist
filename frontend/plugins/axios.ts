import { Context, Plugin } from '@nuxt/types'
import { AxiosRequestConfig } from 'axios'

const axiosPlugin: Plugin = (context: Context) => {
  context.$axios.interceptors.request.use(async (config: AxiosRequestConfig) => {
    if (context.$user) {
      const token = await context.$user.getIdToken()
      config.headers.common.Authorization = `Bearer ${token}`
    }
    return config
  })
}

export default axiosPlugin
