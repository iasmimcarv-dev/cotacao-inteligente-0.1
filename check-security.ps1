# Script de verificação de segurança para Windows
# Execute antes de fazer git push

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Verificacao de Seguranca Pre-Commit" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

$errors = 0
$warnings = 0

# Verificar .gitignore
Write-Host "Verificando .gitignore..." -ForegroundColor Yellow
if (Test-Path .gitignore) {
    $gitignore = Get-Content .gitignore -Raw
    
    $required = @('.env', '*.db', '*.sqlite', 'node_modules/', 'dist/')
    foreach ($entry in $required) {
        if ($gitignore -match [regex]::Escape($entry)) {
            Write-Host "OK '$entry' protegido no .gitignore" -ForegroundColor Green
        } else {
            Write-Host "ERRO '$entry' NAO encontrado no .gitignore" -ForegroundColor Red
            $errors++
        }
    }
} else {
    Write-Host "ERRO .gitignore nao encontrado!" -ForegroundColor Red
    $errors++
}

Write-Host ""

# Verificar .env
Write-Host "Verificando arquivo .env..." -ForegroundColor Yellow
if (Test-Path .env) {
    $gitFiles = git ls-files .env 2>&1
    if ($gitFiles -match ".env") {
        Write-Host "ERRO .env esta versionado no Git! Execute: git rm --cached .env" -ForegroundColor Red
        $errors++
    } else {
        Write-Host "OK .env existe e NAO esta versionado" -ForegroundColor Green
    }
} else {
    Write-Host "AVISO .env nao encontrado (crie um baseado no .env.example)" -ForegroundColor Yellow
    $warnings++
}

Write-Host ""

# Verificar arquivos de database
Write-Host "Verificando arquivos de database..." -ForegroundColor Yellow
$dbFiles = Get-ChildItem -Recurse -Include *.db,*.sqlite,*.sqlite3 -File -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch "node_modules|venv|\.git"
}

$dbVersioned = $false
foreach ($dbFile in $dbFiles) {
    $gitCheck = git ls-files $dbFile.Name 2>&1
    if ($gitCheck -match $dbFile.Name) {
        Write-Host "ERRO Arquivo de database versionado: $($dbFile.Name)" -ForegroundColor Red
        $errors++
        $dbVersioned = $true
    }
}

if (-not $dbVersioned -and $dbFiles.Count -eq 0) {
    Write-Host "OK Nenhum arquivo de database versionado" -ForegroundColor Green
}

Write-Host ""

# Verificar padrões sensíveis
Write-Host "Procurando por credenciais hardcoded..." -ForegroundColor Yellow
$foundIssues = $false
$files = Get-ChildItem -Recurse -Include *.py,*.js,*.jsx -File -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch "node_modules|venv|\.git|dist|__pycache__|example|test"
}

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
    if ($content) {
        if ($content -match 'password\s*=\s*["''][^"'']+["'']') {
            Write-Host "AVISO Possivel credencial hardcoded em: $($file.Name)" -ForegroundColor Yellow
            $warnings++
            $foundIssues = $true
        }
        if ($content -match 'postgres://[^:]+:[^@]+@') {
            Write-Host "AVISO Possivel DATABASE_URL hardcoded em: $($file.Name)" -ForegroundColor Yellow
            $warnings++
            $foundIssues = $true
        }
    }
}

if (-not $foundIssues) {
    Write-Host "OK Nenhuma credencial hardcoded encontrada" -ForegroundColor Green
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan

# Resumo
if ($errors -eq 0 -and $warnings -eq 0) {
    Write-Host "SUCESSO Todas as verificacoes passaram!" -ForegroundColor Green
    Write-Host "E seguro fazer commit." -ForegroundColor Green
    exit 0
} elseif ($errors -eq 0) {
    Write-Host "AVISO $warnings aviso(s) encontrado(s)" -ForegroundColor Yellow
    Write-Host "Voce pode fazer commit, mas revise os avisos." -ForegroundColor Yellow
    exit 0
} else {
    Write-Host "ERRO $errors erro(s) encontrado(s)!" -ForegroundColor Red
    Write-Host "Corrija os problemas antes de fazer commit." -ForegroundColor Red
    exit 1
}

