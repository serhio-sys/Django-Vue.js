import { createApp } from 'vue'
import App from './App.vue'
import './scss/index.scss'
import Router from './router/index.js'
import Store from './store/store.js'

const app = createApp(App)
app.use(Store)
app.use(Router)
app.mount('#app')
