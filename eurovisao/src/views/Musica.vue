<template>
  <v-container
    id="musica-view"
    fluid
    tag="section"
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col cols="12">
        <v-toolbar flat>
          <v-toolbar-title
            class="text-h5 primary--text"
          >
            Lista de Edições
          </v-toolbar-title>
          <v-spacer />
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          />
        </v-toolbar>
        <v-data-table
          :headers="headers"
          :items="desserts"
          :items-per-page="10"
          :search="search"
          loading-text="Loading... Please wait"
          class="elevation-1"
        >
          <template #item.edicao="{ item }">
            <router-link :to="{ name: 'EdicaoX', params: { name: item.edicao } }">
              {{ item.edicao }}
            </router-link>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'MusicaView',
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Nome',
            align: 'start',
            sortable: true,
            value: 'name',
            class: 'primary--text',
          },
          { text: 'País', value: 'calories', class: 'primary--text' },
          { text: 'Artista', value: 'fat', class: 'primary--text' },
          { text: 'Pontuação', value: 'carbs', class: 'primary--text' },
          { text: 'Edição', value: 'edicao', class: 'primary--text' },
        ],
        desserts: [
          {
            name: 1,
            calories: 159,
            fat: 6.0,
            carbs: 24,
            edicao: 2017,
          },
          {
            name: 2,
            calories: 237,
            fat: 9.0,
            carbs: 37,
          },
          {
            name: 3,
            calories: 262,
            fat: 16.0,
            carbs: 23,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
          },
        ],
      }
    },
  }
</script>
