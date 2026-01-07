import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/cotacao-assistente/', // Altere para o nome do seu repositório
  server: {
    port: 5173
  },
  build: {
    outDir: 'dist'
  }
})
