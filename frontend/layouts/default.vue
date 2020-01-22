<template>
  <div>
    <sui-menu fixed="top" inverted>
      <sui-container>
        <nuxt-link to="/" class="item header">
          WouldList
        </nuxt-link>
        <nuxt-link to="/login" class="item">
          login
        </nuxt-link>
        <nuxt-link to="/logout" class="item">
          logout
        </nuxt-link>
        <nuxt-link to="/design" class="item">
          design
        </nuxt-link>
      </sui-container>
    </sui-menu>
    <div class="main">
      <nuxt />
    </div>
  </div>
</template>

<style>
body {
  background-color: #eeeeee;
}
.main {
  padding-top: 7em;
}
</style>
