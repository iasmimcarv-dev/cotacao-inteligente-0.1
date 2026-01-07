# 📚 Índice de Documentação - Sistema de Cotação

## 🚀 Comece Aqui!

1. **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** - ⭐ Comece por aqui!
   - Resumo visual da solução
   - Passos numerados
   - Ordem correta de execução

## 📖 Guias Principais

2. **[CHECKLIST.md](CHECKLIST.md)** - Lista completa de tarefas

   - Segurança
   - Configuração
   - Deploy backend
   - Deploy frontend
   - Testes

3. **[GUIA_DEPLOY.md](GUIA_DEPLOY.md)** - Guia detalhado passo a passo

   - Instruções completas
   - Screenshots e comandos
   - Resolução de problemas
   - URLs importantes

4. **[DIAGRAMA_SOLUCAO.md](DIAGRAMA_SOLUCAO.md)** - Diagramas visuais
   - Arquitetura do sistema
   - Fluxos de dados
   - Comparação antes/depois
   - Stack tecnológica

## 🔧 Referências Técnicas

5. **[COMANDOS_UTEIS.md](COMANDOS_UTEIS.md)** - Comandos do dia a dia

   - Git commands
   - Deploy local
   - Database management
   - Debug e troubleshooting

6. **[DEPLOY_INSTRUCTIONS.md](DEPLOY_INSTRUCTIONS.md)** - Opções de deploy
   - Railway
   - Render
   - Vercel
   - Comparações

## ⚠️ Avisos Importantes

7. **[IMPORTANTE_VITE_CONFIG.md](IMPORTANTE_VITE_CONFIG.md)** - ⚠️ CRÍTICO!
   - Configure o `base` no vite.config.js
   - Sem isso, GitHub Pages não funciona!

## 🔒 Segurança

8. **[check-security.ps1](check-security.ps1)** - Script Windows PowerShell

   - Verifica arquivos sensíveis
   - Valida .gitignore
   - Execute antes de cada commit!

9. **[scripts/check_security.py](scripts/check_security.py)** - Script Python
   - Mesma função que o PS1
   - Cross-platform
   - Mais detalhado

## 📝 Configuração

10. **[.env.example](.env.example)** - Template de variáveis backend

    - DATABASE_URL
    - DEBUG
    - FRONTEND_URL

11. **[.env.frontend.example](.env.frontend.example)** - Template frontend

    - VITE_API_URL

12. **[.gitignore](.gitignore)** - Arquivos ignorados
    - .env protegido
    - Database files
    - node_modules
    - dist/

## 🤖 Automação

13. **[.github/workflows/deploy.yml](.github/workflows/deploy.yml)** - CI/CD
    - GitHub Actions
    - Deploy automático do frontend
    - Triggered on push

## 📂 Código

14. **[src/config/api.js](src/config/api.js)** - Config centralizada da API

    - Base URL do backend
    - Ambiente dinâmico
    - Usado por todas as páginas

15. **[app/core/config.py](app/core/config.py)** - Settings do backend

    - Configuração do CORS
    - Database URL
    - Variáveis de ambiente

16. **[vite.config.js](vite.config.js)** - Configuração do Vite

    - **base** path (IMPORTANTE!)
    - Build settings
    - Server config

17. **[README.md](README.md)** - Documentação principal do projeto
    - Overview
    - Início rápido
    - Estrutura
    - Links para outros docs

---

## 🎯 Fluxo Recomendado de Leitura

### Para Deploy Inicial:

```
1. INICIO_RAPIDO.md          (10 min)
   ↓
2. IMPORTANTE_VITE_CONFIG.md (2 min)
   ↓
3. check-security.ps1        (Execute!)
   ↓
4. CHECKLIST.md              (Siga a lista)
   ↓
5. GUIA_DEPLOY.md            (Consulte quando necessário)
```

### Para Desenvolvimento:

```
1. COMANDOS_UTEIS.md         (Referência rápida)
   ↓
2. README.md                  (Overview técnico)
   ↓
3. .env.example              (Configure localmente)
```

### Para Entender a Arquitetura:

```
1. DIAGRAMA_SOLUCAO.md       (Visualize o sistema)
   ↓
2. README.md                  (Tech stack)
   ↓
3. GUIA_DEPLOY.md            (Detalhes de infraestrutura)
```

---

## 📊 Resumo por Categoria

### 🚨 Segurança (PRIORIDADE!)

- check-security.ps1
- scripts/check_security.py
- .gitignore
- .env.example

### 📚 Documentação

- INICIO_RAPIDO.md
- README.md
- GUIA_DEPLOY.md
- DIAGRAMA_SOLUCAO.md

### ✅ Listas e Checklists

- CHECKLIST.md
- DEPLOY_INSTRUCTIONS.md

### 🔧 Referências Técnicas

- COMANDOS_UTEIS.md
- IMPORTANTE_VITE_CONFIG.md

### ⚙️ Configuração

- .env.example
- .env.frontend.example
- vite.config.js
- app/core/config.py
- src/config/api.js

### 🤖 Automação

- .github/workflows/deploy.yml

---

## 🎨 Ícones e Símbolos Usados

- ⭐ = Comece aqui / Mais importante
- ⚠️ = Atenção / Crítico
- ✅ = Checklist / Tarefa
- 🚨 = Segurança / Urgente
- 🔧 = Técnico / Comandos
- 📖 = Documentação / Leitura
- 🚀 = Deploy / Produção
- 🧪 = Testes
- 📊 = Diagrama / Visual
- 🔒 = Segurança
- 🤖 = Automação

---

## 💡 Dicas Rápidas

**Novo no projeto?**
→ Comece com [INICIO_RAPIDO.md](INICIO_RAPIDO.md)

**Pronto para fazer deploy?**
→ Siga [CHECKLIST.md](CHECKLIST.md)

**Precisa de comandos específicos?**
→ Consulte [COMANDOS_UTEIS.md](COMANDOS_UTEIS.md)

**Quer entender a arquitetura?**
→ Leia [DIAGRAMA_SOLUCAO.md](DIAGRAMA_SOLUCAO.md)

**Antes de commitar?**
→ Execute `.\check-security.ps1`

**GitHub Pages não funciona?**
→ Leia [IMPORTANTE_VITE_CONFIG.md](IMPORTANTE_VITE_CONFIG.md)

---

**Todos os arquivos estão criados e prontos para uso! 📚✨**
