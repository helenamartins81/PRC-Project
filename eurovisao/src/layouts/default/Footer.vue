<template>
  <v-footer
    id="default-footer"
    color="transparent"
    absolute
    app
    inset
  >
    <div class="text-body-1 font-weight-light pt-6 pt-md-0 text-center">
      &copy; {{ (new Date()).getFullYear() }}, Made by Bernado Viseu, Helena Martins, Mariana Pereira
    </div>
  </v-footer>
</template>

<script>
  export default {
    name: 'DefaultFooter',
  }
</script>
