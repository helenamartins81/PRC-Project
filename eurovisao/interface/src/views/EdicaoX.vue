<template>
  <v-container
    id="edicao-x-view"
    fluid
    tag="section"
  >
    <v-row
      align="center"
      justify="start"
    >
      <v-col cols="12">
        <app-card class="mt-4">
          <v-card-text class="">
            <h3 class="text-h3 mb-2 primary--text">
              Eurovisão Edição {{this.id}}
            </h3>
            <p class="text-h5 mb-2">País da realização : {{this.organizador}}</p>
            <p class="text-h5 mb-2">País Vencedor: {{this.vencedor}}</p>
            <p class="text-h5 mb-2">Música Vencedora: {{this.musica}}</p>
            <v-spacer />
             <v-data-table
              :headers="headers"
              :items="this.pais"
              :search="search"
              item-key="name"
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
            </v-data-table>
          </v-card-text>
        </app-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'EdicaoXView',
    data () {
      return {
        pais: [],
        vencedor: '',
        organizador: '',
        musica: '',
        search: '',
        id: this.$route.params.name,
        headers: [
          {
            text: 'País',
            align: 'start',
            sortable: true,
            value: 'p',
          },
          { text: 'Artista(s)', value: 'artista' },
          { text: 'Musica', value: 'musica' },
          { text: 'Classificação', value: 'lugar' },
          { text: 'Juri', value: 'juri' },
          { text: 'Televoto', value: 'televoto' },
          { text: 'Total', value: 'total' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
          },
        ],
      }
    },
    created: async function () {
      try {
        const response = await axios.get('http://localhost:3000/edicao/ed' + this.id)
        this.lista = response.data
        this.musica = this.lista[0].musicaVencedora
        this.vencedor = this.lista[0].paisVencedor
        this.organizador = this.lista[0].organizador
        const response2 = await axios.get('http://localhost:3000/edicao/' + this.id+'/pais')
        this.pais = response2.data

      } catch (e) {
        return e
      }
    },
  }
</script>
