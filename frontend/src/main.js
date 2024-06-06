import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import ArcoVue from '@arco-design/web-vue';
import '@arco-design/web-vue/dist/arco.css';

const app = createApp(App)
const prefixUrl = "http://127.0.0.1:8000"

app.use(createPinia())
app.use(ArcoVue)

app.mount('#app')

export {prefixUrl}
