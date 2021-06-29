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
          item-key="musicas"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title
                c
                lass="text-h5 mb-4 primary--text"
              >
                Lista de País Participantes
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

        headers2: [
          {
            text: 'Nome',
            align: 'start',
            sortable: true,
            value: 'musicas',
            class: 'primary--text',
          },
          { text: 'Link', value: 'links', class: 'primary--text' },
          { text: 'Liricístas', value: 'liricista', class: 'primary--text' },
          { text: 'Pontuação', value: 'total', class: 'primary--text' },
          { text: 'Classificação', value: 'lugar', class: 'primary--text' },
          { text: 'Edição', value: 'ano', class: 'primary--text' },
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
