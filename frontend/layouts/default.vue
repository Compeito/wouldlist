<template>
  <div>
    <sui-menu fixed="top" inverted>
      <sui-container>
        <sui-menu-item header>
          <nuxt-link to="/">
            WouldList
          </nuxt-link>
        </sui-menu-item>
        <sui-menu-item link href="#">
          Home
        </sui-menu-item>
        <sui-dropdown item text="Account Menu">
          <sui-dropdown-menu>
            <nuxt-link to="/login" class="item">
              login
            </nuxt-link>
            <nuxt-link to="/logout" class="item">
              logout
            </nuxt-link>
          </sui-dropdown-menu>
        </sui-dropdown>
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
  margin-top: 7em;
}
</style>
