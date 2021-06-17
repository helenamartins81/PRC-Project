<template>
  <v-carousel
    hide-delimiters
    cycle
    height="750px"
  >
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
  // Utilities
  export default {
    name: 'DashboardView',

    data () {
      return {
        items: [
          {
            src: 'https://www.ukrainetogo.com/wp-content/uploads/2017/09/sobral-3.jpg',
          },
          {
            src: 'https://www.middleeasteye.net/sites/default/files/styles/article_page/public/images-story/israelieurovision.afp_.jpg?itok=9uv2a_Au',
          },
          {
            src: 'https://www.eurovision.de/niederlande1166_v-contentxl.jpg',
          },
          {
            src: 'https://i1.wp.com/escxtra.com/wp-content/uploads/Maneskin-2021-e1621794952242.jpg?fit=1254%2C680&ssl=1',
          },
        ],
      }
    },
  }
</script>
