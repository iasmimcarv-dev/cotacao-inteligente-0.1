import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/cotacao-inteligente-0.1/',
  server: {
    port: 5173
  },
  build: {
    outDir: 'dist'
  }
})
