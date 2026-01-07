# ⚠️ IMPORTANTE: Configure o nome do repositório

Antes de fazer deploy para GitHub Pages, você DEVE alterar a linha `base` no arquivo `vite.config.js`.

## Como descobrir o nome correto:

1. **Vá no seu repositório no GitHub**

   - URL será algo como: `https://github.com/seuusuario/nome-do-repo`

2. **O nome do repo é a última parte da URL**

   - Exemplo: se a URL é `https://github.com/joao/cotacao-saude`
   - O nome do repo é: `cotacao-saude`

3. **Edite o vite.config.js**

```javascript
export default defineConfig({
  plugins: [react()],
  base: '/nome-do-repo/', // ← ALTERE AQUI!
  server: {
    port: 5173
  },
  build: {
    outDir: 'dist'
  }
})
```

## Exemplos:

### Se seu repositório é: `github.com/maria/sistema-cotacao`

```javascript
base: '/sistema-cotacao/',
```

### Se seu repositório é: `github.com/empresa/app-saude`

```javascript
base: '/app-saude/',
```

### Se seu repositório é: `github.com/dev/health-quotes`

```javascript
base: '/health-quotes/',
```

## ⚠️ O que acontece se NÃO alterar:

- GitHub Pages mostrará uma página em branco
- Console do navegador mostrará erro 404 nos arquivos JS/CSS
- Nada funcionará!

## ✅ Como testar se está correto:

```powershell
# 1. Build local
npm run build

# 2. Preview
npm run preview

# 3. Acesse: http://localhost:4173/nome-do-repo/
# Deve funcionar!
```

## 🔧 Se já fez deploy e não funciona:

```powershell
# 1. Altere o vite.config.js
# 2. Commit e push
git add vite.config.js
git commit -m "Fix base path for GitHub Pages"
git push origin main

# 3. Aguarde 2-3 minutos para o deploy automático
# 4. Limpe o cache do navegador (Ctrl+Shift+R)
```

---

**Não esqueça este passo! É essencial para o GitHub Pages funcionar! 🚨**
