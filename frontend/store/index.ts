import Vue from 'vue'

class Counter {
  private _count: number = 0

  get count () {
    return this._count
  }

  public increment (): void {
    this._count++
  }
}

export default Vue.observable(new Counter())
