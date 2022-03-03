<template>
  <v-container>
    <v-row >
      <v-col align="center">
        <v-img class="mb-4 mt-4"
          :src="require('../assets/logo.png')"
          contain
          height="150"
        />
      
        <h1 class="font-weight-bold mb-6">
          Send a Message
        </h1>
        <v-text-field
            class="sh rink"
            v-model="message"
            :append-outer-icon="'mdi-send'"
            :prepend-inner-icon="icon"
            dense
            outlined
            rounded
            solo
            clearable
            label="Message"
            type="text"
            color="black"
            @click:append-outer="sendMessage"
            @click:prepend-inner="changeIcon"
            @click:clear="clearMessage"
        ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>
<style scoped>

.v-text-field{
      width: 600px;
}
</style>
<script>
  var baseUrl = window.location.origin
  export default {
    data: () => ({
      password: 'Password',
      show: false,
      message: 'Café?',
      marker: true,
      iconIndex: 0,
      icons: [
        'mdi-emoticon',
        'mdi-emoticon-cool',
        'mdi-emoticon-dead',
        'mdi-emoticon-excited',
        'mdi-emoticon-happy',
        'mdi-emoticon-neutral',
        'mdi-emoticon-sad',
        'mdi-emoticon-tongue',
      ],
    }),

    computed: {
      icon () {
        return this.icons[this.iconIndex]
      },
    },

    methods: {
      toggleMarker () {
        this.marker = !this.marker
      },
      sendMessage () {
        fetch(baseUrl + '/api/send-message', {
        method: 'POST',
        body: JSON.stringify({
          message: this.message
        }),
        headers: {'Content-type': 'application/json; charset=UTF-8'}
        })
        .then(() => {
          this.resetIcon()
          this.clearMessage()
        })
      },
      clearMessage () {
        this.message = ''
      },
      resetIcon () {
        this.iconIndex = 0
      },
      changeIcon () {
        this.iconIndex === this.icons.length - 1
          ? this.iconIndex = 0
          : this.iconIndex++
      },
    },
  }
</script>