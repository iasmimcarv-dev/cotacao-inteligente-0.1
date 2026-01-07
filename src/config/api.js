// Configuração da API
// Para desenvolvimento local, use a URL local
// Para produção (GitHub Pages), use a URL do backend hospedado

const API_BASE_URL =
  import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/v1'

export default API_BASE_URL
