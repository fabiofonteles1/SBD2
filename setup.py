#!/usr/bin/env python3
"""
Script de setup do projeto Data Lakehouse
Configura o ambiente e instala dependências
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(command, description):
    """Executa um comando e registra o resultado"""
    print(f"Executando: {description}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {description} - Sucesso")
            return True
        else:
            print(f"✗ {description} - Erro: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ {description} - Exceção: {e}")
        return False

def check_python():
    """Verifica se Python está instalado"""
    print("Verificando Python...")
    try:
        version = sys.version_info
        print(f"Python {version.major}.{version.minor}.{version.micro} encontrado")
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print("⚠️  Versão do Python muito antiga. Recomendado Python 3.8+")
        return True
    except Exception as e:
        print(f"✗ Erro ao verificar Python: {e}")
        return False

def check_docker():
    """Verifica se Docker está instalado"""
    print("Verificando Docker...")
    result = subprocess.run("docker --version", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✓ {result.stdout.strip()}")
        return True
    else:
        print("✗ Docker não encontrado")
        print("Instale Docker: https://docs.docker.com/get-docker/")
        return False

def install_requirements():
    """Instala as dependências Python"""
    print("Instalando dependências Python...")
    
    requirements_file = Path("scripts/requirements.txt")
    if requirements_file.exists():
        return run_command(f"pip install -r {requirements_file}", "Instalação de dependências")
    else:
        print("⚠️  Arquivo requirements.txt não encontrado")
        return False

def create_directories():
    """Cria diretórios necessários"""
    print("Criando estrutura de diretórios...")
    
    directories = [
        "silver",
        "gold",
        "logs",
        "output"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ Diretório {directory} criado/verificado")
    
    return True

def setup_git():
    """Configura o repositório Git"""
    print("Configurando Git...")
    
    # Inicializa repositório se não existir
    if not Path(".git").exists():
        run_command("git init", "Inicializando repositório Git")
    
    # Adiciona arquivos
    run_command("git add .", "Adicionando arquivos ao Git")
    
    # Commit inicial
    run_command('git commit -m "Initial commit: Data Lakehouse setup"', "Commit inicial")
    
    return True

def main():
    """Função principal de setup"""
    print("=== SETUP DO PROJETO DATA LAKEHOUSE ===")
    print()
    
    # 1. Verificar Python
    if not check_python():
        print("❌ Python não encontrado. Instale Python 3.8+ e tente novamente.")
        sys.exit(1)
    
    # 2. Verificar Docker
    if not check_docker():
        print("❌ Docker não encontrado. Instale Docker e tente novamente.")
        sys.exit(1)
    
    # 3. Instalar dependências
    if not install_requirements():
        print("⚠️  Falha na instalação de dependências. Continue manualmente.")
    
    # 4. Criar diretórios
    if not create_directories():
        print("❌ Falha ao criar diretórios.")
        sys.exit(1)
    
    # 5. Configurar Git
    if not setup_git():
        print("⚠️  Falha na configuração do Git. Continue manualmente.")
    
    print()
    print("=== SETUP CONCLUÍDO ===")
    print()
    print("Próximos passos:")
    print("1. Execute: python scripts/run_automation.py")
    print("2. Acesse os notebooks em: notebooks/")
    print("3. Monitore os logs em: automation.log")
    print()
    print("Acesso ao banco de dados:")
    print("- Host: localhost:5432")
    print("- Database: sbd2_lakehouse")
    print("- User: sbd2_user")
    print("- Password: sbd2_password")
    print()
    print("Acesso ao pgAdmin:")
    print("- URL: http://localhost:8080")
    print("- Email: admin@sbd2.com")
    print("- Password: admin123")

if __name__ == "__main__":
    main()
