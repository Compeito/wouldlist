import Item from '~/schemes/Item'

export default interface User {
  name: string
  photoUrl: string
  screenName: string
  item: Item[]
}
