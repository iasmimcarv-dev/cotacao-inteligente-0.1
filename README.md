# 🏥 Sistema de Cotação de Planos de Saúde

Sistema completo para cotação de planos de saúde com backend FastAPI + PostgreSQL e frontend React.

## 🚀 Links Rápidos

- ⭐ **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** - Comece por aqui!
- 📚 **[INDICE.md](INDICE.md)** - Índice completo de toda documentação
- ✅ [Checklist de Deploy](CHECKLIST.md)
- 📖 [Guia Completo de Deploy](GUIA_DEPLOY.md)
- 🔧 [Comandos Úteis](COMANDOS_UTEIS.md)
- 📊 [Diagramas da Solução](DIAGRAMA_SOLUCAO.md)
- ⚠️ [IMPORTANTE: Configurar Vite](IMPORTANTE_VITE_CONFIG.md)

## 🏗️ Arquitetura

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  GitHub Pages   │────────▶│  Backend API     │────────▶│  PostgreSQL     │
│  (Frontend)     │         │  (Railway/Render)│         │  (Railway)      │
└─────────────────┘         └──────────────────┘         └─────────────────┘
```

## 🛠️ Tecnologias

**Frontend:**

- React + Vite
- TailwindCSS
- Axios
- React Router

**Backend:**

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL

## ⚡ Início Rápido (Desenvolvimento Local)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/cotacao-assistente.git
cd cotacao-assistente
```

### 2. Configure o Backend

```bash
# Crie o arquivo .env com suas credenciais
cp .env.example .env

# Edite o .env e adicione sua DATABASE_URL
notepad .env

# Instale as dependências Python
pip install -r requirements.txt

# Execute o backend
python -m uvicorn app.main:app --reload
```

Backend estará em: `http://127.0.0.1:8000`

### 3. Configure o Frontend

```bash
# Instale as dependências Node
npm install

# Execute o frontend
npm run dev
```

Frontend estará em: `http://localhost:5173`

## 📦 Deploy em Produção

**IMPORTANTE:** Siga o [Guia Completo de Deploy](GUIA_DEPLOY.md) para instruções detalhadas.

### Resumo:

1. **Backend (Railway/Render):**

   - Deploy do FastAPI
   - Configure DATABASE_URL
   - Anote a URL do backend

2. **Frontend (GitHub Pages):**
   - Configure `VITE_API_URL` no `.env.local`
   - Ajuste `base` no `vite.config.js`
   - Push para GitHub
   - GitHub Actions fará deploy automático

## 🔒 Segurança

⚠️ **CRÍTICO:** Nunca commite arquivos sensíveis!

### Verificação Automática de Segurança

Antes de fazer commit, execute o script de verificação:

```powershell
# Windows PowerShell
.\check-security.ps1

# Ou Python (cross-platform)
python scripts/check_security.py
```

Este script verifica:

- ✅ Se `.env` está protegido no `.gitignore`
- ✅ Se arquivos de database não estão versionados
- ✅ Se não há credenciais hardcoded no código
- ✅ Se configurações sensíveis estão seguras

### Arquivos que NUNCA devem ser commitados:

```bash
# Verifique se estes arquivos NÃO estão commitados:
- .env
- .env.local
- *.db
- *.sqlite
```

### Se você acidentalmente commitou o `.env`:

```bash
# 1. Remover do Git
git rm --cached .env
git commit -m "Remove sensitive .env file"
git push origin main

# 2. ALTERAR IMEDIATAMENTE a senha do banco de dados!
```

## 📂 Estrutura do Projeto

```
cotacao-assistente/
├── app/                    # Backend Python
│   ├── core/              # Configurações
│   ├── db/                # Database
│   ├── models/            # Modelos SQLAlchemy
│   ├── routers/           # Endpoints API
│   ├── schemas/           # Schemas Pydantic
│   └── services/          # Lógica de negócio
├── src/                   # Frontend React
│   ├── components/        # Componentes
│   ├── config/            # Configurações
│   ├── pages/             # Páginas
│   └── theme/             # Tema
├── scripts/               # Scripts de utilidade
├── .env.example           # Exemplo de variáveis de ambiente
└── GUIA_DEPLOY.md        # Guia de deploy
```

## 🧪 Testando

### Backend:

```bash
# Docs automáticas do FastAPI
http://127.0.0.1:8000/docs
```

### Frontend:

```bash
npm run dev
```

## 📝 Variáveis de Ambiente

### Backend (.env):

```env
DATABASE_URL=postgresql://user:pass@host:port/db
DEBUG=false
FRONTEND_URL=https://seuusuario.github.io/repo
```

### Frontend (.env.local):

```env
VITE_API_URL=https://seu-backend.up.railway.app/api/v1
```

## 🐛 Resolução de Problemas

### Erro "Failed to fetch":

- Verifique CORS no backend
- Confirme `VITE_API_URL` no `.env.local`
- Abra Console do navegador (F12)

### Backend não inicia:

- Verifique `DATABASE_URL` no `.env`
- Instale dependências: `pip install -r requirements.txt`
- Verifique logs

### GitHub Pages em branco:

- Verifique `base` no `vite.config.js`
- Limpe cache (Ctrl+Shift+R)
- Verifique logs do GitHub Actions

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Add nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é privado e proprietário.

## 📞 Suporte

- 📖 [Guia de Deploy](GUIA_DEPLOY.md)
- 🐛 Issues: Abra uma issue no GitHub
- 📧 Email: seu-email@exemplo.com

---

⚡ Feito com FastAPI + React
