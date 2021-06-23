<template>
  <v-container
    id="edicao-view"
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
          flat
          :headers="headers"
          :items="edicao"
          :items-per-page="10"
          :search="search"
          class="elevation-1"
        >
          <template
            #item.ano="{ item }"
          >
            <router-link :to="{ name: 'EdicaoX', params: { name: item.ano } }">
              {{ item.ano }}
            </router-link>
          </template>
          <template
            #item.musicaVencedor="{ item }"
          >
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'EdicaoView',
    data () {
      return {
        edicao: [],
        search: '',
        headers: [
          {
            text: 'Edição',
            align: 'start',
            sortable: true,
            value: 'ano',
            class: 'primary--text',
          },
          { text: 'País Organizador', value: 'organizador', class: 'primary--text' },
          { text: 'País Vencedor', value: 'vencedor', class: 'primary--text' },
          { text: 'Musica Vencedora', value: 'musicaVencedora', class: 'primary--text' },
        ],
      }
    },
    created: async function () {
      try {
        const response = await axios.get('http://localhost:3000/edicoes')
        this.edicao = response.data
      } catch (e) {
        return e
      }
    },
  }
</script>
