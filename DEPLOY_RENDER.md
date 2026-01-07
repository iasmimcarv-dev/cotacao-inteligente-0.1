# 🚀 Deploy no Render - Guia Passo a Passo

## ✅ Por que Render?

- ✅ **Gratuito** (750h/mês - suficiente para 1 serviço 24/7)
- ✅ **PostgreSQL gratuito** (90 dias, depois expira mas pode criar outro)
- ✅ **Deploy automático** do GitHub
- ✅ **HTTPS automático**
- ✅ **Muito simples** de configurar

---

## 📋 Passo a Passo

### 1️⃣ Criar Conta no Render

1. Acesse: https://render.com
2. Click em **"Get Started"**
3. **Sign up with GitHub**
4. Autorize o Render a acessar seus repositórios

---

### 2️⃣ Criar Database PostgreSQL (Primeiro!)

1. No dashboard, click **"New +"**
2. Selecione **"PostgreSQL"**
3. Configure:
   - **Name:** `cotacao-db` (ou o nome que preferir)
   - **Database:** `cotacao`
   - **User:** `cotacao_user`
   - **Region:** escolha o mais próximo (ex: Oregon USA)
   - **Plan:** **Free** (90 dias grátis)
4. Click **"Create Database"**
5. Aguarde 2-3 minutos até ficar "Available"

6. **COPIE a URL de conexão:**
   - Na página do database, procure **"Internal Database URL"**
   - Será algo como: `postgresql://cotacao_user:SENHA@dpg-xxxxx/cotacao`
   - **Copie essa URL completa!** Você vai precisar

---

### 3️⃣ Criar Web Service (Backend FastAPI)

1. No dashboard, click **"New +"** novamente
2. Selecione **"Web Service"**
3. Click **"Connect a repository"**
4. Se for a primeira vez, autorize o Render
5. Encontre e selecione seu repositório: **`cotacao-assistente`**
6. Click **"Connect"**

7. **Configure o serviço:**

   - **Name:** `cotacao-backend` (ou o que preferir)
   - **Region:** mesmo do database (ex: Oregon)
   - **Branch:** `main` (ou `master`)
   - **Root Directory:** deixe vazio
   - **Runtime:** **Python 3**
   - **Build Command:**
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```bash
     uvicorn app.main:app --host 0.0.0.0 --port 10000
     ```
   - **Plan:** **Free**

8. **Adicionar Variável de Ambiente:**

   - Scroll até **"Environment Variables"**
   - Click **"Add Environment Variable"**
   - **Key:** `DATABASE_URL`
   - **Value:** Cole a URL do database que você copiou no passo 2
   - Exemplo: `postgresql://cotacao_user:SENHA@dpg-xxxxx/cotacao`

9. Click **"Create Web Service"**

10. **Aguarde o deploy** (5-10 minutos na primeira vez)

    - Você verá os logs em tempo real
    - Quando aparecer "Your service is live", está pronto!

11. **Copie a URL do seu backend:**
    - Será algo como: `https://cotacao-backend.onrender.com`
    - **Anote essa URL!**

---

### 4️⃣ Testar o Backend

1. Acesse no navegador:

   ```
   https://cotacao-backend.onrender.com/docs
   ```

2. Você deve ver a **documentação Swagger** do FastAPI!

3. Teste o endpoint raiz:
   ```
   https://cotacao-backend.onrender.com/
   ```
   Deve retornar: `{"message": "API do Cotador online e Profissional! 🚀"}`

---

### 5️⃣ Configurar Frontend

1. Edite o arquivo `.env.local` na raiz do projeto:

   ```env
   # URL da API no Render
   VITE_API_URL=https://cotacao-backend.onrender.com/api/v1
   ```

2. **IMPORTANTE:** Substitua `cotacao-backend` pelo nome que você escolheu no passo 3

---

### 6️⃣ Deploy no GitHub Pages

1. Commit suas alterações:

   ```powershell
   git add .env.local
   git commit -m "Configure Render backend URL"
   git push origin main
   ```

2. No GitHub:

   - Vá em **Settings → Pages**
   - **Source:** "GitHub Actions"
   - Aguarde 2-3 minutos

3. Acesse seu site:
   ```
   https://seuusuario.github.io/cotacao-assistente/
   ```

---

## 🧪 Testar Tudo

### Backend:

- ✅ `https://seu-backend.onrender.com/docs` → Swagger UI
- ✅ `https://seu-backend.onrender.com/` → Mensagem de boas-vindas

### Frontend:

- ✅ Site carrega sem erros
- ✅ F12 → Console sem erros de CORS
- ✅ Consegue buscar operadoras/planos
- ✅ Consegue fazer cotação

---

## ⚠️ Limitações do Plano Gratuito

### Backend (Web Service Free):

- ✅ 750 horas/mês (suficiente para 1 app 24/7)
- ⚠️ **"Dorme" após 15 minutos sem uso** (primeira requisição demora ~30 segundos)
- ✅ 512 MB RAM
- ✅ Deploy automático do GitHub

### Database (PostgreSQL Free):

- ⚠️ **Expira após 90 dias** (você precisa criar um novo)
- ✅ 1 GB de storage
- ✅ Backup automático (7 dias)

💡 **Dica:** Se quiser evitar o "cold start", considere o plano pago ($7/mês) ou use um serviço de "keep alive"

---

## 🔄 Deploy Automático

Agora, sempre que você fizer `git push`:

1. **Backend:** Render detecta e faz redeploy automático (5-10 min)
2. **Frontend:** GitHub Actions faz deploy no Pages (2-3 min)

---

## 🔧 Configurações Avançadas (Opcional)

### Manter o serviço "acordado":

Crie um cron job gratuito (ex: cron-job.org) que acesse sua URL a cada 10 minutos:

```
https://seu-backend.onrender.com/
```

### Atualizar dependências:

Se adicionar pacotes no `requirements.txt`, o Render reinstala automaticamente no próximo deploy.

---

## 🐛 Problemas Comuns

### "Application failed to respond"

- Verifique os logs no Render Dashboard
- Confirme que o Start Command está correto
- Verifique se `DATABASE_URL` está configurado

### "Failed to fetch" no frontend

- Confirme a URL no `.env.local`
- Verifique CORS no backend (já está configurado)
- Limpe o cache do navegador (Ctrl+Shift+R)

### Database expira (90 dias)

1. Crie novo database no Render
2. Atualize `DATABASE_URL` nas variáveis de ambiente
3. O Render faz redeploy automático

---

## 💰 Custos

| Serviço     | Plano Free                 | Plano Pago              |
| ----------- | -------------------------- | ----------------------- |
| Web Service | ✅ Grátis (com cold start) | $7/mês (sem cold start) |
| PostgreSQL  | ✅ 90 dias grátis          | $7/mês (permanente)     |
| **Total**   | **Grátis**                 | **$14/mês**             |

---

## ✅ Pronto!

Agora você tem:

- ✅ Backend FastAPI no Render
- ✅ Database PostgreSQL no Render
- ✅ Frontend no GitHub Pages
- ✅ Deploy automático
- ✅ HTTPS em todo lugar
- ✅ Tudo funcionando!

---

## 📞 Próximos Passos

1. Teste tudo completamente
2. Configure um domínio customizado (opcional)
3. Monitore os logs no Render Dashboard
4. Configure alertas de uptime (opcional)

**Parabéns! Seu sistema está no ar! 🎉**
