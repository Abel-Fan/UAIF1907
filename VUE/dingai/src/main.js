import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'  // 饿了么组件的一个插件

Vue.config.productionTip = false

Vue.use(ElementUI)   // 加载插件

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
