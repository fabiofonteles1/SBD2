#!/usr/bin/env python3
"""
Teste simples para verificar se o projeto está funcionando
"""

import os
import sys
from pathlib import Path

def test_file_structure():
    """Testa se a estrutura de arquivos está correta"""
    print("=== TESTE DE ESTRUTURA DE ARQUIVOS ===")
    
    required_files = [
        "docker/docker-compose.yml",
        "docker/init.sql", 
        "scripts/run_etl.py",
        "scripts/run_automation.py",
        "scripts/validate_setup.py",
        "scripts/requirements.txt",
        "docs/README.md",
        "docs/modelagem_silver.md",
        "docs/dicionario_dados_bronze.md",
        "notebooks/01_data_exploration.ipynb",
        "notebooks/02_etl_raw_to_silver.ipynb", 
        "notebooks/03_lakehouse_validation.ipynb",
        "raw/train.csv",
        "README.md",
        "setup.py",
        "run_all.py",
        ".gitignore"
    ]
    
    missing_files = []
    existing_files = []
    
    for file_path in required_files:
        if Path(file_path).exists():
            existing_files.append(file_path)
            print(f"✅ {file_path}")
        else:
            missing_files.append(file_path)
            print(f"❌ {file_path}")
    
    print(f"\n=== RESUMO ===")
    print(f"Arquivos encontrados: {len(existing_files)}/{len(required_files)}")
    print(f"Arquivos ausentes: {len(missing_files)}")
    
    if missing_files:
        print(f"\n❌ Arquivos ausentes:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    else:
        print(f"\n🎉 TODOS OS ARQUIVOS ENCONTRADOS!")
        return True

def test_data_file():
    """Testa se o arquivo de dados existe e tem tamanho correto"""
    print("\n=== TESTE DO ARQUIVO DE DADOS ===")
    
    data_file = Path("raw/train.csv")
    if data_file.exists():
        size_gb = data_file.stat().st_size / (1024*1024*1024)
        print(f"✅ Arquivo encontrado: {data_file}")
        print(f"✅ Tamanho: {size_gb:.2f} GB")
        
        if size_gb > 1.0:  # Pelo menos 1GB
            print("✅ Tamanho adequado para processamento")
            return True
        else:
            print("⚠️  Arquivo muito pequeno")
            return False
    else:
        print("❌ Arquivo raw/train.csv não encontrado")
        return False

def test_python_imports():
    """Testa se as dependências Python estão disponíveis"""
    print("\n=== TESTE DE DEPENDÊNCIAS PYTHON ===")
    
    required_packages = [
        'pandas',
        'numpy', 
        'psycopg2',
        'sqlalchemy',
        'matplotlib',
        'seaborn'
    ]
    
    missing_packages = []
    available_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            available_packages.append(package)
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package}")
    
    print(f"\n=== RESUMO ===")
    print(f"Pacotes disponíveis: {len(available_packages)}/{len(required_packages)}")
    print(f"Pacotes ausentes: {len(missing_packages)}")
    
    if missing_packages:
        print(f"\n❌ Pacotes ausentes:")
        for package in missing_packages:
            print(f"  - {package}")
        print("\n💡 Execute: pip install -r scripts/requirements.txt")
        return False
    else:
        print(f"\n🎉 TODAS AS DEPENDÊNCIAS DISPONÍVEIS!")
        return True

def test_docker():
    """Testa se Docker está disponível"""
    print("\n=== TESTE DO DOCKER ===")
    
    try:
        import subprocess
        result = subprocess.run("docker --version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Docker disponível: {result.stdout.strip()}")
            return True
        else:
            print("❌ Docker não está funcionando")
            return False
    except Exception as e:
        print(f"❌ Erro ao verificar Docker: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🚀 TESTE DO PROJETO DATA LAKEHOUSE SBD-2")
    print("=" * 50)
    
    # Executa todos os testes
    tests = [
        ("Estrutura de Arquivos", test_file_structure),
        ("Arquivo de Dados", test_data_file),
        ("Dependências Python", test_python_imports),
        ("Docker", test_docker)
    ]
    
    results = []
    for test_name, test_function in tests:
        try:
            result = test_function()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Erro no teste {test_name}: {e}")
            results.append((test_name, False))
    
    # Resumo final
    print("\n" + "=" * 50)
    print("📊 RESUMO DOS TESTES")
    print("=" * 50)
    
    passed_tests = 0
    total_tests = len(results)
    
    for test_name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name}: {status}")
        if result:
            passed_tests += 1
    
    print(f"\n🎯 RESULTADO FINAL: {passed_tests}/{total_tests} testes passaram")
    
    if passed_tests == total_tests:
        print("🎉 PROJETO PRONTO PARA USO!")
        print("\n💡 Próximos passos:")
        print("1. Execute: python run_all.py")
        print("2. Acesse: http://localhost:8080 (pgAdmin)")
        print("3. Execute os notebooks em: notebooks/")
    else:
        print("⚠️  ALGUNS TESTES FALHARAM")
        print("Verifique os erros acima e corrija antes de continuar")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
