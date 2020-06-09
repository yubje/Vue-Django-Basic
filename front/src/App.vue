<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> | 
      <router-link v-if="!isLoggedin" :to="{ name: 'LoginView' }">Login</router-link> | 
      <router-link v-if="isLoggedin" to="/accounts/logout" @click.native="logout">Logout</router-link>

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
      // 3. 쿠키 설정
      this.$cookies.set('auth-token', key)
      // 4. 로그인 완료 표시 
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
    logout() {
      // 1. 로그아웃 하기 위한 header 정보 만들기 
      const requestHeader = {
        headers: {
          // 2. get을 통해 'auth-token'이라는 이름으로 저장된 토큰 값 가져오기
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      // 3. post 요청은 두 번째 위치 인자로 data가 들어가기 때문에 비워둔다. 
      axios.post(`${SERVER_URL}/rest-auth/logout/`, null, requestHeader)
        .then(() => {
          // 4. 브라우저 쿠키 값 지우기 
          this.$cookies.remove('auth-token')
          // 5. 로그인 여부 상태 변경 & Home으로 라우팅 
          this.isLoggedin = false
          this.$router.push('/')
        })
        .catch(error => console.log(error.response.data))
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
