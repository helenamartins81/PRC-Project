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
        <v-data-table
          :headers="headers"
          :items="musicas"
          :search="search"
          item-key="name"
          :expanded.sync="expanded"
          show-expand
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title class="text-h5 mb-4 primary--text">Lista de País Participantes</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
            </v-toolbar>
          </template>
          <template v-slot:expanded-item="{ headers, item }">
            <tr>
              <th>Link</th>
              <td>{item.links}</td>
            </tr>
            <tr>
              <th>Liricístas</th>
              <td>{item.links}</td>
            </tr>
            <tr>
              <th>Compositores</th>
              <td>{item.links}</td>
            </tr>
            <tr>
              <th>Pontuação do Televoto</th>
              <td>{item.links}</td>
            </tr>
            <tr>
              <th>Pontuação do Júri</th>
              <td>{item.links}</td>
            </tr>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'MusicaView',
    data () {
      return {
        search: '',
        musicas: [],
        musicas_L_C: [],
        headers: [
          {
            text: 'Nome',
            align: 'start',
            sortable: true,
            value: 'musicas',
            class: 'primary--text',
          },
          { text: 'País', value: 'pais', class: 'primary--text' },
          { text: 'Artista', value: 'artista', class: 'primary--text' },
          { text: 'Pontuação', value: 'total', class: 'primary--text' },
          { text: 'Classificação', value: 'lugar', class: 'primary--text' },
          { text: 'Edição', value: 'ano', class: 'primary--text' },
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
    created: async function () {
      try {
        const response = await axios.get('http://localhost:3000/musicas')
        this.musicas = response.data
        const response2 = await axios.get('http://localhost:3000/musicas_L_C')
        this.musicas_L_C = response2.data
      } catch (e) {
        return e
      }
    },
  }
</script>
