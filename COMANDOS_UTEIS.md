# 🔧 Comandos Úteis

## 🧹 Limpar arquivos sensíveis do Git (EMERGÊNCIA)

Se você acidentalmente commitou o `.env` ou arquivos sensíveis:

```powershell
# 1. Remover do Git (mas manter local)
git rm --cached .env

# 2. Commit a remoção
git commit -m "Remove sensitive .env file"

# 3. Push para o GitHub
git push origin main

# 4. IMPORTANTE: Altere IMEDIATAMENTE as senhas do banco!
```

## 🔍 Verificar o que será commitado

```powershell
# Ver status dos arquivos
git status

# Ver diferenças
git diff

# Ver o que está staged
git diff --cached
```

## 🚀 Deploy Local

### Backend:

```powershell
# Ativar ambiente virtual (se usar)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar backend
python -m uvicorn app.main:app --reload

# Ou usar o script
.\start-dev.bat
```

### Frontend:

```powershell
# Instalar dependências
npm install

# Rodar em desenvolvimento
npm run dev

# Build para produção
npm run build

# Preview do build
npm run preview
```

## 🗄️ Database

### Migrations:

```powershell
# Recriar database (CUIDADO: apaga todos os dados!)
python scripts/recreate_db.py

# Adicionar colunas
python scripts/migrate_add_columns.py

# Popular dados de exemplo
python scripts/populate_planos_exemplo.py
```

### Conectar ao PostgreSQL:

```powershell
# Via psql
psql postgresql://usuario:senha@host:porta/database

# Via Python
python -c "from app.db.database import engine; print(engine.url)"
```

## 📦 Git

### Commits:

```powershell
# Add todos os arquivos
git add .

# Commit
git commit -m "Sua mensagem"

# Push
git push origin main
```

### Branches:

```powershell
# Criar nova branch
git checkout -b feature/nova-funcionalidade

# Mudar de branch
git checkout main

# Listar branches
git branch -a
```

## 🧪 Testes

### Backend:

```powershell
# Abrir documentação interativa
start http://127.0.0.1:8000/docs

# Testar endpoint específico
curl http://127.0.0.1:8000/api/v1/cotacao
```

### Frontend:

```powershell
# Build e checar erros
npm run build

# Verificar bundle size
npm run build -- --watch
```

## 🔄 Atualizar Dependências

### Python:

```powershell
# Atualizar requirements.txt
pip freeze > requirements.txt

# Instalar de requirements.txt
pip install -r requirements.txt

# Upgrade de pacote específico
pip install --upgrade nome-do-pacote
```

### Node:

```powershell
# Verificar pacotes desatualizados
npm outdated

# Atualizar todos
npm update

# Atualizar específico
npm install pacote@latest
```

## 🐛 Debug

### Backend:

```powershell
# Ver logs do uvicorn
python -m uvicorn app.main:app --reload --log-level debug

# Python interativo com contexto da app
python
>>> from app.db.database import engine
>>> from app.models import *
>>> # Seus testes aqui
```

### Frontend:

```powershell
# Limpar cache do Vite
rm -r node_modules/.vite
npm run dev

# Build com análise
npm run build -- --debug
```

## 📊 Informações do Sistema

```powershell
# Python version
python --version

# Node version
node --version

# npm version
npm --version

# Listar dependências Python instaladas
pip list

# Listar dependências Node instaladas
npm list --depth=0
```

## 🔒 Segurança

### Verificar se .env está protegido:

```powershell
# Verificar .gitignore
cat .gitignore | Select-String ".env"

# Ver histórico de um arquivo
git log --follow -- .env

# Verificar se .env está no repositório
git ls-files | Select-String ".env"
```

### Gerar nova SECRET_KEY (se necessário):

```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## 🌐 URLs Úteis

- **Backend Local:** http://127.0.0.1:8000
- **Backend Docs:** http://127.0.0.1:8000/docs
- **Frontend Local:** http://localhost:5173
- **Railway Dashboard:** https://railway.app
- **GitHub Pages:** https://seuusuario.github.io/repo

## 📝 Notas

- Sempre rode `git status` antes de commitar
- Nunca commite arquivos `.env`, `.db`, ou credentials
- Use branches para novas features
- Teste localmente antes de fazer push
- Mantenha o README atualizado
