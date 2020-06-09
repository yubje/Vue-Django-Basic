<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label for="id">ID: </label>
        <input id="id" type="text" v-model="loginData.username"><br>
      </div>
      <div>
        <label for="password">Password: </label>
        <input id="password" type="password" v-model="loginData.password"><br>
        <input type="submit">
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login() {
      this.$emit('submit-login-data', this.loginData)
    },
  },
}
</script>

<style>

</style>