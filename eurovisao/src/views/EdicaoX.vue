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
            <p class="text-h5 mb-2">País da realização : {{this.pr}}</p>
            <p class="text-h5 mb-2">País Vencedor: {{this.vencedor}}</p>
            <p class="text-h5 mb-2">Música Vencedora: {{this.vencedor}}</p>
            <v-spacer />
             <v-data-table
              :headers="dessertHeaders"
              :items="desserts"
              :expanded.sync="expanded"
              :search="search"
              item-key="name"
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
                <td :colspan="headers.length">
                  <v-data-table
                    :headers="headers"
                    :items="desserts"
                    :items-per-page="10"
                    loading-text="Loading... Please wait"
                    class="elevation-1"
                  />
                </td>
              </template>
            </v-data-table>
          </v-card-text>
        </app-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'EdicaoXView',
    data () {
      return {
        search: '',
        id: this.$route.params.name,
        expanded: [],
        dessertHeaders: [
          {
            text: 'País',
            align: 'start',
            sortable: true,
            value: 'name',
          },
          { text: 'Artista(s)', value: 'calories' },
          { text: 'Musica', value: 'fat' },
          { text: 'Juri', value: 'carbs' },
          { text: 'Publico', value: 'protein' },
          { text: '', value: 'data-table-expand' },
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
  }
</script>
