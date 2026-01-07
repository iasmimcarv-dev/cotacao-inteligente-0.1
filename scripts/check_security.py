#!/usr/bin/env python3
"""
Script de verificação de segurança antes de commit
Execute antes de fazer git push para verificar se não há credenciais expostas
"""
import os
import sys
import re
from pathlib import Path

# Cores para output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_error(msg):
    print(f"{RED}{BOLD}❌ ERRO: {msg}{RESET}")

def print_warning(msg):
    print(f"{YELLOW}⚠️  AVISO: {msg}{RESET}")

def print_success(msg):
    print(f"{GREEN}✅ {msg}{RESET}")

def check_file_exists(filepath, should_exist=True):
    """Verifica se um arquivo existe ou não existe"""
    exists = os.path.exists(filepath)
    if should_exist and not exists:
        print_error(f"Arquivo {filepath} não encontrado!")
        return False
    elif not should_exist and exists:
        print_error(f"Arquivo {filepath} NÃO deveria existir no projeto!")
        return False
    return True

def check_gitignore():
    """Verifica se .gitignore tem as entradas necessárias"""
    print(f"\n{BOLD}Verificando .gitignore...{RESET}")
    
    required_entries = ['.env', '*.db', '*.sqlite', 'node_modules/', 'dist/']
    
    if not os.path.exists('.gitignore'):
        print_error(".gitignore não encontrado!")
        return False
    
    with open('.gitignore', 'r', encoding='utf-8') as f:
        content = f.read()
    
    all_ok = True
    for entry in required_entries:
        if entry not in content:
            print_error(f"Entrada '{entry}' não encontrada no .gitignore")
            all_ok = False
        else:
            print_success(f"'{entry}' protegido no .gitignore")
    
    return all_ok

def check_env_file():
    """Verifica se .env existe e se não está versionado"""
    print(f"\n{BOLD}Verificando arquivo .env...{RESET}")
    
    if not os.path.exists('.env'):
        print_warning(".env não encontrado (você precisa criar um baseado no .env.example)")
        return True  # Não é erro crítico
    
    # Verifica se .env está no git
    result = os.popen('git ls-files .env 2>&1').read()
    
    if '.env' in result:
        print_error(".env está versionado no Git! Execute: git rm --cached .env")
        return False
    
    print_success(".env existe e NÃO está versionado")
    return True

def check_sensitive_patterns():
    """Procura por padrões sensíveis em arquivos Python e JavaScript"""
    print(f"\n{BOLD}Procurando por credenciais hardcoded...{RESET}")
    
    sensitive_patterns = [
        (r'password\s*=\s*["\'][^"\']+["\']', 'senha hardcoded'),
        (r'api_key\s*=\s*["\'][^"\']+["\']', 'API key hardcoded'),
        (r'secret\s*=\s*["\'][^"\']{20,}["\']', 'secret hardcoded'),
        (r'postgres://[^:]+:[^@]+@', 'DATABASE_URL hardcoded'),
    ]
    
    files_to_check = []
    for ext in ['*.py', '*.js', '*.jsx', '*.ts', '*.tsx']:
        files_to_check.extend(Path('.').rglob(ext))
    
    issues_found = False
    excluded_dirs = {'node_modules', 'venv', '.git', 'dist', '__pycache__', 'build'}
    
    for filepath in files_to_check:
        # Pular diretórios excluídos
        if any(excluded in filepath.parts for excluded in excluded_dirs):
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for pattern, description in sensitive_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    # Ignorar comentários e exemplos
                    if 'example' not in str(filepath) and 'test' not in str(filepath):
                        print_warning(f"{description} encontrado em {filepath}")
                        issues_found = True
        except Exception:
            continue
    
    if not issues_found:
        print_success("Nenhuma credencial hardcoded encontrada")
    
    return not issues_found

def check_database_files():
    """Verifica se há arquivos de database no projeto"""
    print(f"\n{BOLD}Verificando arquivos de database...{RESET}")
    
    db_extensions = ['.db', '.sqlite', '.sqlite3']
    db_files = []
    
    for ext in db_extensions:
        db_files.extend(Path('.').rglob(f'*{ext}'))
    
    # Filtrar arquivos que estão versionados
    versionados = []
    for db_file in db_files:
        result = os.popen(f'git ls-files {db_file} 2>&1').read()
        if str(db_file) in result:
            versionados.append(db_file)
    
    if versionados:
        print_error(f"Arquivos de database versionados encontrados:")
        for f in versionados:
            print(f"  - {f}")
        print_error("Execute: git rm --cached <arquivo>")
        return False
    
    print_success("Nenhum arquivo de database versionado")
    return True

def main():
    print(f"{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}🔒 Verificação de Segurança Pré-Commit{RESET}")
    print(f"{BOLD}{'='*60}{RESET}")
    
    checks = [
        check_gitignore(),
        check_env_file(),
        check_database_files(),
        check_sensitive_patterns(),
    ]
    
    print(f"\n{BOLD}{'='*60}{RESET}")
    
    if all(checks):
        print_success(f"{BOLD}✅ Todas as verificações passaram!{RESET}")
        print(f"{GREEN}É seguro fazer commit.{RESET}")
        sys.exit(0)
    else:
        print_error(f"{BOLD}❌ Algumas verificações falharam!{RESET}")
        print(f"{RED}Corrija os problemas antes de fazer commit.{RESET}")
        sys.exit(1)

if __name__ == '__main__':
    main()
