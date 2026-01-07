# 🚀 Guia Completo de Deploy - GitHub Pages + Backend

## ⚠️ SEGURANÇA - Primeiro Passo (CRÍTICO!)

### 1. Verificar se o .env está protegido

```bash
# NUNCA faça commit do .env!
# Verifique se está no .gitignore:
cat .gitignore | grep ".env"
```

### 2. Se você já fez commit do .env anteriormente:

```bash
# Remova o .env do histórico do Git (cuidado!)
git rm --cached .env
git commit -m "Remove .env from repository"
```

### 3. Altere IMEDIATAMENTE a senha do banco

- Acesse Railway: https://railway.app
- Vá em seu projeto PostgreSQL
- Altere a senha do banco de dados
- Atualize o arquivo `.env` local com a nova senha

---

## 📦 PASSO 1: Deploy do Backend (FastAPI + PostgreSQL)

### Opção A: Railway (RECOMENDADO)

1. **Acesse Railway:**

   - Vá em https://railway.app
   - Faça login com GitHub

2. **Crie novo projeto:**

   - Click "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha seu repositório

3. **Configure o serviço:**

   - Railway detectará automaticamente Python
   - Adicione estas variáveis de ambiente:
     ```
     DATABASE_URL=seu_url_do_postgresql
     ```

4. **Deploy automático:**
   - Railway fará deploy automaticamente
   - Anote a URL gerada (ex: `https://seu-app.up.railway.app`)

### Opção B: Render.com (Gratuito)

1. **Acesse Render:**

   - Vá em https://render.com
   - Faça login com GitHub

2. **Crie Web Service:**

   - "New" → "Web Service"
   - Conecte seu repositório

3. **Configure:**

   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 10000`
   - **Variáveis de Ambiente:**
     - `DATABASE_URL` = sua URL do PostgreSQL

4. **Deploy:**
   - Click "Create Web Service"
   - Aguarde o deploy (5-10 minutos)
   - Anote a URL gerada

---

## 🌐 PASSO 2: Deploy do Frontend (GitHub Pages)

### 1. Configurar variáveis de ambiente local

Crie o arquivo `.env.local` na raiz do projeto:

```bash
VITE_API_URL=https://sua-url-do-backend.up.railway.app/api/v1
```

### 2. Ajustar o base path no vite.config.js

Edite [vite.config.js](vite.config.js) e altere a linha:

```javascript
base: '/cotacao-assistente/', // ← ALTERE PARA O NOME DO SEU REPOSITÓRIO
```

Se seu repositório é `github.com/seuusuario/meu-projeto`, use:

```javascript
base: '/meu-projeto/',
```

### 3. Instalar dependência para deploy

```bash
npm install --save-dev gh-pages
```

### 4. Fazer commit das alterações

```bash
git add .
git commit -m "Configure for GitHub Pages deployment"
git push origin main
```

### 5. Configurar GitHub Pages

1. Vá no seu repositório no GitHub
2. **Settings** → **Pages**
3. **Source:** Selecione "GitHub Actions"
4. O deploy será automático a cada push!

### 6. Acessar o site

Após alguns minutos, acesse:

```
https://seuusuario.github.io/nome-do-repositorio/
```

---

## ✅ PASSO 3: Testar

1. **Teste o backend:**

   ```bash
   curl https://sua-url-backend.up.railway.app/docs
   ```

   Deve abrir a documentação Swagger do FastAPI

2. **Teste o frontend:**
   - Acesse a URL do GitHub Pages
   - Verifique se consegue fazer cotações
   - Abra o Console do navegador (F12) para ver se há erros

---

## 🔄 Workflow de Desenvolvimento

### Desenvolvimento Local:

```bash
# Terminal 1 - Backend
python -m uvicorn app.main:app --reload

# Terminal 2 - Frontend
npm run dev
```

### Deploy em Produção:

```bash
# Fazer alterações
git add .
git commit -m "Suas alterações"
git push origin main

# GitHub Actions fará deploy automático do frontend
# Railway/Render farão deploy automático do backend
```

---

## 🐛 Resolução de Problemas

### Erro "Failed to fetch" no frontend:

- Verifique se a variável `VITE_API_URL` está correta
- Verifique o CORS no backend
- Abra o Console do navegador (F12) e veja o erro exato

### Backend não inicia:

- Verifique os logs no Railway/Render
- Confirme que `requirements.txt` está atualizado
- Verifique se `DATABASE_URL` está configurado

### GitHub Pages mostra página em branco:

- Verifique o `base` no [vite.config.js](vite.config.js)
- Verifique os logs no GitHub Actions
- Limpe o cache do navegador (Ctrl+Shift+R)

---

## 📝 Checklist Final

- [ ] `.env` no `.gitignore` e NÃO commitado
- [ ] Senha do banco alterada se houve exposição
- [ ] Backend deployed (Railway/Render)
- [ ] Variável `VITE_API_URL` configurada
- [ ] `base` no vite.config.js correto
- [ ] GitHub Actions configurado
- [ ] GitHub Pages ativado
- [ ] Site funcionando corretamente

---

## 🆘 Precisa de Ajuda?

Se encontrar problemas:

1. Verifique os logs do GitHub Actions
2. Verifique os logs do Railway/Render
3. Abra o Console do navegador (F12)
4. Consulte a documentação oficial
