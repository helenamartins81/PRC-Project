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
          :items="desserts"
          :items-per-page="10"
          :search="search"
          loading-text="Loading... Please wait"
          class="elevation-1"
        >
          <template
            #item.name="{ item }"
          >
            <router-link :to="{ name: 'EdicaoX', params: { name: item.name } }">
              {{ item.name }}
            </router-link>
          </template>
          <template
            #item.musica="{ item }"
          >
            {{ item.musica }}
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'EdicaoView',
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Edição',
            align: 'start',
            sortable: true,
            value: 'name',
            class: 'primary--text',
          },
          { text: 'País realização', value: 'pr', class: 'primary--text' },
          { text: 'País Vencedor', value: 'pv', class: 'primary--text' },
          { text: 'Musica Vencedora', value: 'musica', class: 'primary--text' },
        ],
        desserts: [
          {
            name: 2017,
            pr: 159,
            pv: 'Portugal',
            musica: 'Amar pelos dois',
          },
          {
            name: 2018,
            pr: 'Portugal',
            pv: 'Israel',
            musica: 'TOy',
          },
          {
            name: 2021,
            pr: 'Holanda',
            pv: 'Italia',
            musica: 23,
          },
          {
            name: 2019,
            pr: 305,
            pv: 3.7,
            musica: 67,
          },
          {
            name: 'Gingerbread',
            pr: 356,
            pv: 16.0,
            musica: 49,
          },
          {
            name: 'Jelly bean',
            pr: 375,
            pv: 0.0,
            musica: 94,
          },
          {
            name: 'Lollipop',
            pr: 392,
            pv: 0.2,
            musica: 98,
          },
          {
            name: 'Honeycomb',
            pr: 408,
            pv: 3.2,
            musica: 87,
          },
          {
            name: 'Donut',
            pr: 452,
            pv: 25.0,
            musica: 51,
          },
          {
            name: 'KitKat',
            pr: 518,
            pv: 26.0,
            musica: 65,
          },
        ],
      }
    },
  }
</script>
