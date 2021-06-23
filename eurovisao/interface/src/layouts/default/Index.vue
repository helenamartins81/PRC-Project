<template>
  <v-app>
    <default-drawer />

    <default-view />

    <default-footer />

    <default-settings />
  </v-app>
</template>

<script>
  export default {
    name: 'DefaultLayout',

    components: {
      DefaultDrawer: () => import(
        /* webpackChunkName: "default-drawer" */
        './Drawer'
      ),
      DefaultFooter: () => import(
        /* webpackChunkName: "default-footer" */
        './Footer'
      ),
      DefaultSettings: () => import(
        /* webpackChunkName: "default-settings" */
        './Settings'
      ),
      DefaultView: () => import(
        /* webpackChunkName: "default-view" */
        './View'
      ),
    },
  }
</script>
