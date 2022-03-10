<template>
  <v-app :style="{background: 'linear-gradient(to top, #2980b9, #6dd5fa, #ffffff)'}">
    <v-main>
      <SendAMessage/>
    </v-main>
  </v-app>
</template>

<script>
import SendAMessage from './components/SendAMessage';

export default {
  name: 'App',

  components: {
    SendAMessage,
  },

  data: () => ({
    //
  }),
};
</script>
