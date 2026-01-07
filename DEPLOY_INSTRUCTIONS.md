# Opções para Backend com GitHub Pages

## ✅ OPÇÃO 1: Usar Railway (RECOMENDADO - Já está configurado!)

Você já tem o banco PostgreSQL no Railway. Basta fazer deploy do backend Python lá também:

1. Acesse https://railway.app
2. Crie novo projeto "Deploy from GitHub"
3. Selecione seu repositório
4. Configure as variáveis de ambiente (DATABASE_URL)
5. Railway vai detectar automaticamente o Python e FastAPI
6. Anote a URL do backend (ex: https://seu-app.up.railway.app)

## ✅ OPÇÃO 2: Render.com (Gratuito)

1. Acesse https://render.com
2. Crie "New Web Service"
3. Conecte seu repositório GitHub
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
5. Adicione variável DATABASE_URL
6. Anote a URL

## ✅ OPÇÃO 3: Vercel (Serverless)

Requer adaptação para serverless functions

## ⚠️ DEPOIS: Atualizar Frontend

Após fazer deploy do backend, atualize o frontend para apontar para a URL do backend:

- Edite `src/App.jsx` ou arquivos de configuração
- Troque `http://localhost:8000` pela URL do backend hospedado
