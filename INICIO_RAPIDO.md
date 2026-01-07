# 🎯 Resumo Rápido: Como Usar no GitHub Pages

## O Problema que Você Tinha:

1. ❌ **GitHub Pages não executa Python/FastAPI** (só serve HTML/CSS/JS estáticos)
2. ❌ **Database com credenciais não pode ser commitado** (risco de segurança)

## A Solução Implementada:

```
┌─────────────────────────────────────────────────────────────┐
│                    ARQUITETURA FINAL                        │
└─────────────────────────────────────────────────────────────┘

    USUÁRIO
       ↓
   ┌────────────────────┐
   │  GitHub Pages      │ ← Frontend React (HTML/CSS/JS)
   │  (Estático)        │   https://seuusuario.github.io/repo
   └────────────────────┘
            ↓ API Requests
   ┌────────────────────┐
   │  Railway/Render    │ ← Backend FastAPI (Python)
   │  (Servidor)        │   https://seu-app.up.railway.app
   └────────────────────┘
            ↓ SQL Queries
   ┌────────────────────┐
   │  PostgreSQL        │ ← Database
   │  (Railway)         │   Suas tabelas e dados
   └────────────────────┘
```

## 📋 Próximos Passos (Ordem):

### 1️⃣ **SEGURANÇA PRIMEIRO** (5 minutos)

```powershell
# Execute o script de verificação
.\check-security.ps1

# Se encontrar problemas, corrija antes de continuar!
```

**Checklist:**

- [ ] `.env` NÃO está commitado
- [ ] `.gitignore` tem `.env`, `*.db`, `node_modules/`, `dist/`
- [ ] Nenhuma senha hardcoded no código

---

### 2️⃣ **Deploy do Backend** (10-15 minutos)

**Opção A: Railway (Recomendado)**

1. Acesse https://railway.app
2. Login com GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecione seu repositório
5. Adicione variável: `DATABASE_URL` (copie do seu `.env`)
6. Aguarde deploy
7. **Anote a URL:** `https://________.up.railway.app`

**Opção B: Render**

1. Acesse https://render.com
2. "New" → "Web Service"
3. Conecte repositório
4. Build: `pip install -r requirements.txt`
5. Start: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
6. Adicione `DATABASE_URL`
7. **Anote a URL:** `https://________.onrender.com`

✅ **Teste:** Acesse `https://sua-url/docs` - deve abrir o Swagger

---

### 3️⃣ **Configurar Frontend** (5 minutos)

```powershell
# 1. Criar arquivo .env.local na raiz do projeto
New-Item -Path ".env.local" -ItemType File

# 2. Adicionar a URL do backend
# Edite .env.local e adicione:
VITE_API_URL=https://sua-url-do-backend.up.railway.app/api/v1
```

```javascript
// 3. Editar vite.config.js
// Altere 'cotacao-assistente' para o nome do SEU repositório
base: '/SEU-NOME-DO-REPO/',
```

---

### 4️⃣ **Deploy no GitHub Pages** (5 minutos)

```powershell
# 1. Commit todas as alterações
git add .
git commit -m "Configure for production deployment"
git push origin main
```

```
2. No GitHub:
   - Vá em Settings → Pages
   - Source: "GitHub Actions"
   - Aguarde 2-3 minutos
```

✅ **Acesse:** `https://seuusuario.github.io/seu-repo/`

---

## 🧪 Testar Tudo

### Backend:

```powershell
# Teste o endpoint de docs
start https://sua-url-backend.up.railway.app/docs
```

### Frontend:

```powershell
# Acesse o site
start https://seuusuario.github.io/seu-repo/

# Pressione F12 no navegador
# - Aba Network: veja as requisições para o backend
# - Aba Console: não deve ter erros de CORS
```

### Integração:

- [ ] Página carrega sem erros
- [ ] Consegue buscar operadoras/planos
- [ ] Consegue fazer cotação
- [ ] Resultados aparecem corretamente

---

## 🔄 Workflow de Agora em Diante

### Desenvolvimento Local:

```powershell
# Terminal 1 - Backend
python -m uvicorn app.main:app --reload

# Terminal 2 - Frontend
npm run dev

# Acesse: http://localhost:5173
```

### Deploy para Produção:

```powershell
# 1. Verificar segurança
.\check-security.ps1

# 2. Commit e Push
git add .
git commit -m "Suas alterações"
git push origin main

# 3. Deploy é AUTOMÁTICO!
# - GitHub Actions → Frontend
# - Railway/Render → Backend
```

---

## 📁 Arquivos Importantes Criados

| Arquivo                                                      | Descrição                          |
| ------------------------------------------------------------ | ---------------------------------- |
| [CHECKLIST.md](CHECKLIST.md)                                 | Lista completa de tarefas          |
| [GUIA_DEPLOY.md](GUIA_DEPLOY.md)                             | Guia detalhado passo a passo       |
| [COMANDOS_UTEIS.md](COMANDOS_UTEIS.md)                       | Comandos úteis do dia a dia        |
| [check-security.ps1](check-security.ps1)                     | Script de verificação de segurança |
| [.github/workflows/deploy.yml](.github/workflows/deploy.yml) | GitHub Actions para deploy         |
| [src/config/api.js](src/config/api.js)                       | Configuração centralizada da API   |

---

## 🆘 Problemas Comuns

### "Failed to fetch" no frontend:

```powershell
# 1. Verifique se VITE_API_URL está correto no .env.local
cat .env.local

# 2. Verifique CORS no backend
# Abra: https://seu-backend.up.railway.app/docs
# Teste um endpoint manualmente
```

### Backend não inicia:

```powershell
# Ver logs no Railway:
# Dashboard → Seu projeto → Deployments → View Logs

# Verificar variáveis de ambiente:
# Settings → Variables → Confirme DATABASE_URL
```

### GitHub Pages em branco:

```powershell
# 1. Verifique o base no vite.config.js
# 2. Ver logs do GitHub Actions
#    GitHub → Actions → Último workflow
# 3. Limpar cache do navegador
#    Ctrl + Shift + R
```

---

## ✅ Resultado Final

Quando tudo estiver funcionando:

✅ Frontend hospedado no **GitHub Pages** (grátis, rápido, HTTPS)  
✅ Backend hospedado no **Railway/Render** (banco de dados seguro)  
✅ Deploy automático a cada `git push`  
✅ HTTPS em todo lugar  
✅ Sem credenciais expostas  
✅ Escalável e profissional

---

## 📞 Precisa de Ajuda?

1. Veja o [CHECKLIST.md](CHECKLIST.md) completo
2. Consulte o [GUIA_DEPLOY.md](GUIA_DEPLOY.md) detalhado
3. Execute `.\check-security.ps1` antes de cada commit
4. Use os [COMANDOS_UTEIS.md](COMANDOS_UTEIS.md) para operações do dia a dia

**Boa sorte! 🚀**
