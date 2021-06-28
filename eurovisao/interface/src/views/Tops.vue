<template>
  <v-container
    id="tops-view"
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
            Top 10 País Vencedor
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
          flat
          :headers="headersA"
          :items="artista"
          :items-per-page="10"
          :search="search"
          class="elevation-1"
        >
        </v-data-table>
      </v-col>
      <v-col cols="12">
        <v-toolbar flat>
          <v-toolbar-title
            class="text-h5 primary--text"
          >
            Top 10 País Organizador
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
          flat
          :headers="headersO"
          :items="organizador"
          :items-per-page="10"
          :search="search"
          class="elevation-1"
        >
        </v-data-table>
      </v-col>
      <v-col cols="12">
        <v-toolbar flat>
          <v-toolbar-title
            class="text-h5 primary--text"
          >
            Top 10 Artísta Participaram
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
          flat
          :headers="headersArt"
          :items="art"
          :items-per-page="10"
          :search="search"
          class="elevation-1"
        >
        </v-data-table>
      </v-col>
      <v-col cols="12">
        <v-toolbar flat>
          <v-toolbar-title
            class="text-h5 primary--text"
          >
            Top 10 Liricista Participaram
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
          flat
          :headers="headersL"
          :items="lir"
          :items-per-page="10"
          :search="search"
          class="elevation-1"
        >
        </v-data-table>
      </v-col>
            <v-col cols="12">
        <v-toolbar flat>
          <v-toolbar-title
            class="text-h5 primary--text"
          >
            Top 10 Compositores Participaram
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
          flat
          :headers="headersC"
          :items="lir"
          :items-per-page="10"
          :search="search"
          class="elevation-1"
        >
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'Tops',
    data () {
      return {
        artista: [],
        organizador: [],
        art: [],
        lir: [],
        comp: [],
        search: '',
        headersA: [
          {
            text: 'País',
            align: 'start',
            sortable: true,
            value: 'pais',
            class: 'primary--text',
          },
          { text: 'Numero de Edições', value: 'numEdicoes', class: 'primary--text' },
        ],
        headersO: [
          {
            text: 'País',
            align: 'start',
            sortable: true,
            value: 'pais',
            class: 'primary--text',
          },
          { text: 'Numero de Organizações', value: 'numEdicoes', class: 'primary--text' },
        ],
        headersArt: [
          {
            text: 'Artísta',
            align: 'start',
            sortable: true,
            value: 'artista',
            class: 'primary--text',
          },
          { text: 'País', value: 'pais', class: 'primary--text' },
          { text: 'Numero de Edições', value: 'numEdicoes', class: 'primary--text' },
        ],
        headersL: [
          {
            text: 'Liricista',
            align: 'start',
            sortable: true,
            value: 'artista',
            class: 'primary--text',
          },
          { text: 'País', value: 'pais', class: 'primary--text' },
          { text: 'Numero de Edições', value: 'numEdicoes', class: 'primary--text' },
        ],
        headersC: [
          {
            text: 'Composito',
            align: 'start',
            sortable: true,
            value: 'artista',
            class: 'primary--text',
          },
          { text: 'País', value: 'pais', class: 'primary--text' },
          { text: 'Numero de Edições', value: 'numEdicoes', class: 'primary--text' },
        ],
      }
    },
    created: async function () {
      try {
        const response = await axios.get('http://localhost:3000/topArtista')
        this.artista = response.data
        const response2 = await axios.get('http://localhost:3000/topOrganizador')
        this.organizador = response2.data
        const response3 = await axios.get('http://localhost:3000/topArt')
        this.art = response3.data
        const response4 = await axios.get('http://localhost:3000/topLiricista')
        this.lir = response4.data
        const response5 = await axios.get('http://localhost:3000/topCompositor')
        this.comp = response5.data
      } catch (e) {
        return e
      }
    },
  }
</script>
