import Vue from 'vue'
import App from './App.vue'
import router from './router'

// vue-cookies es2015 module
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
