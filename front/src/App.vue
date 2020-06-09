<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link v-if="!isLoggedin" :to="{ name: 'LoginView' }">Login</router-link>

    </div>
    <router-view
      @submit-login-data="login"
    />
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8080'

export default {
  name: 'App',
  data() {
    return {
      isLoggedin: false
    }
  },
  methods: {
    setCookie(key) {
      this.$cookies.set('auth-token', key)
      this.isLoggedin = true
    },
    login(loginData) {
      axios.post(`${SERVER_URL}/rest-auth/login/`, loginData)
        .then(response =>{
          console.log(response)
          // 1. 토큰을 설정하기 위한 메서드 호출 (키 값 넘겨줌)
          this.setCookie(response.data.key)
          // 2. 로그인이 끝나면 메인 페이지로 이동 
          this.$router.push('/')
        })
        .catch(error => console.log(error.response))
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
