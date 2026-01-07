# ✅ Checklist de Segurança e Deploy

## 🚨 SEGURANÇA (FAÇA PRIMEIRO!)

### 1. Proteção de Credenciais

- [ ] Verificar que `.env` está no `.gitignore`
- [ ] Verificar que `.env` NÃO foi commitado anteriormente
  ```powershell
  git log --all --full-history -- .env
  ```
- [ ] Se foi commitado, remover do histórico:
  ```powershell
  git rm --cached .env
  git commit -m "Remove .env from repository"
  ```
- [ ] **ALTERAR senha do banco de dados imediatamente**
- [ ] Criar `.env.example` sem credenciais reais ✓

### 2. Verificar .gitignore

- [ ] `.env` ✓
- [ ] `.env.local` ✓
- [ ] `*.db` ✓
- [ ] `*.sqlite` ✓
- [ ] `node_modules/` ✓
- [ ] `dist/` ✓
- [ ] `__pycache__/` ✓

---

## 🔧 CONFIGURAÇÃO DO PROJETO

### Backend

- [ ] Arquivo `.env` criado com `DATABASE_URL` correto
- [ ] Dependencies instaladas: `pip install -r requirements.txt`
- [ ] Backend roda localmente: `python -m uvicorn app.main:app --reload`
- [ ] Docs acessíveis: http://127.0.0.1:8000/docs
- [ ] CORS configurado em [app/main.py](app/main.py) ✓
- [ ] Settings criadas em [app/core/config.py](app/core/config.py) ✓

### Frontend

- [ ] Dependencies instaladas: `npm install`
- [ ] Frontend roda localmente: `npm run dev`
- [ ] Configuração de API criada em [src/config/api.js](src/config/api.js) ✓
- [ ] Páginas atualizadas para usar config centralizada ✓
- [ ] `vite.config.js` com `base` correto para GitHub Pages ✓

---

## 🚀 DEPLOY BACKEND (Railway/Render)

### Opção: Railway

- [ ] Conta criada em https://railway.app
- [ ] Projeto criado: "Deploy from GitHub repo"
- [ ] Repositório conectado
- [ ] Variável `DATABASE_URL` configurada
- [ ] Deploy concluído com sucesso
- [ ] URL anotada: `https://________.up.railway.app`
- [ ] Testado: `https://________.up.railway.app/docs`

### Opção: Render

- [ ] Conta criada em https://render.com
- [ ] Web Service criado
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
- [ ] Variável `DATABASE_URL` configurada
- [ ] Deploy concluído
- [ ] URL anotada: `https://________.onrender.com`

---

## 🌐 DEPLOY FRONTEND (GitHub Pages)

### 1. Configuração Local

- [ ] Arquivo `.env.local` criado na raiz
- [ ] `VITE_API_URL` configurado no `.env.local`:
  ```
  VITE_API_URL=https://seu-backend.up.railway.app/api/v1
  ```
- [ ] `base` no `vite.config.js` ajustado para nome do repo
- [ ] GitHub Actions workflow criado: `.github/workflows/deploy.yml` ✓

### 2. Git & GitHub

- [ ] Todas as alterações commitadas:
  ```powershell
  git add .
  git commit -m "Configure for production deployment"
  git push origin main
  ```
- [ ] Repositório está público ou privado conforme desejado
- [ ] GitHub Pages habilitado em Settings → Pages
- [ ] Source configurado para "GitHub Actions"

### 3. Verificação

- [ ] GitHub Actions executou com sucesso (aba Actions)
- [ ] Site acessível: `https://seuusuario.github.io/repo-name/`
- [ ] Console do navegador (F12) sem erros de CORS
- [ ] Requisições para backend funcionando

---

## 🧪 TESTES FINAIS

### Backend em Produção

- [ ] `GET /` retorna mensagem de boas-vindas
- [ ] `GET /docs` mostra Swagger UI
- [ ] `POST /api/v1/cotacao` funciona
- [ ] Database conecta corretamente

### Frontend em Produção

- [ ] Página carrega sem erros
- [ ] Formulário de cotação visível
- [ ] Consegue buscar operadoras
- [ ] Consegue calcular cotação
- [ ] Resultados são exibidos corretamente
- [ ] Página admin acessível (se aplicável)

### Integração Frontend + Backend

- [ ] F12 → Network mostra requisições para backend
- [ ] Sem erros de CORS
- [ ] Dados carregam corretamente
- [ ] Formulários enviam dados com sucesso

---

## 📝 DOCUMENTAÇÃO

- [ ] README.md atualizado ✓
- [ ] GUIA_DEPLOY.md criado ✓
- [ ] COMANDOS_UTEIS.md criado ✓
- [ ] `.env.example` atualizado ✓
- [ ] URLs de produção anotadas

---

## 🔄 PÓS-DEPLOY

### Monitoramento

- [ ] Verificar logs do backend (Railway/Render)
- [ ] Verificar GitHub Actions para deploys futuros
- [ ] Configurar alertas de uptime (opcional)

### Manutenção

- [ ] Backup do banco de dados configurado
- [ ] Documentação de como reverter deploy
- [ ] Plano de recuperação de desastres

---

## 📞 SUPORTE

Se algo não funcionar:

1. **Erro de CORS:**

   - Verifique [app/core/config.py](app/core/config.py)
   - Adicione a URL do frontend em `CORS_ORIGINS`

2. **API não responde:**

   - Verifique logs no Railway/Render
   - Confirme `DATABASE_URL` está correto
   - Teste o endpoint `/docs`

3. **GitHub Pages em branco:**

   - Verifique `base` no `vite.config.js`
   - Limpe cache (Ctrl+Shift+R)
   - Verifique logs do GitHub Actions

4. **Database não conecta:**
   - Verifique `DATABASE_URL` no Railway/Render
   - Teste conexão local com psql
   - Verifique firewall/IP whitelist

---

## ✅ TUDO PRONTO!

Quando todos os itens estiverem marcados, seu sistema estará:

- ✅ Seguro (sem credenciais expostas)
- ✅ Funcionando em produção
- ✅ Acessível via GitHub Pages
- ✅ Backend hospedado e escalável
- ✅ Documentado para futuras manutenções

**Parabéns! 🎉**
