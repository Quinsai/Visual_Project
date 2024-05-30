import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const prefixUrl = "http://127.0.0.1:4523/m1/4554522-0-default"

app.use(createPinia())

app.mount('#app')

export {prefixUrl}
