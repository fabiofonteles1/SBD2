#!/usr/bin/env python3
"""
Script principal para executar todo o projeto Data Lakehouse
Executa setup, validação e automação completa
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def print_banner():
    """Exibe banner do projeto"""
    print("=" * 60)
    print("🚀 DATA LAKEHOUSE SBD-2 - EXECUÇÃO COMPLETA")
    print("=" * 60)
    print()

def run_setup():
    """Executa o setup do projeto"""
    print("📋 ETAPA 1: SETUP DO PROJETO")
    print("-" * 40)
    
    if Path("setup.py").exists():
        result = subprocess.run("python setup.py", shell=True)
        if result.returncode == 0:
            print("✅ Setup concluído com sucesso")
            return True
        else:
            print("❌ Falha no setup")
            return False
    else:
        print("⚠️  Arquivo setup.py não encontrado, pulando...")
        return True

def run_validation():
    """Executa validação do setup"""
    print("\n🔍 ETAPA 2: VALIDAÇÃO DO SETUP")
    print("-" * 40)
    
    if Path("scripts/validate_setup.py").exists():
        result = subprocess.run("python scripts/validate_setup.py", shell=True)
        if result.returncode == 0:
            print("✅ Validação concluída com sucesso")
            return True
        else:
            print("❌ Falha na validação")
            return False
    else:
        print("⚠️  Arquivo validate_setup.py não encontrado, pulando...")
        return True

def run_automation():
    """Executa automação completa"""
    print("\n🤖 ETAPA 3: AUTOMAÇÃO COMPLETA")
    print("-" * 40)
    
    if Path("scripts/run_automation.py").exists():
        result = subprocess.run("python scripts/run_automation.py", shell=True)
        if result.returncode == 0:
            print("✅ Automação concluída com sucesso")
            return True
        else:
            print("❌ Falha na automação")
            return False
    else:
        print("⚠️  Arquivo run_automation.py não encontrado, pulando...")
        return True

def show_results():
    """Exibe resultados e próximos passos"""
    print("\n🎉 EXECUÇÃO CONCLUÍDA!")
    print("=" * 60)
    print()
    print("📊 RECURSOS DISPONÍVEIS:")
    print("• Jupyter Notebooks: notebooks/")
    print("• Documentação: docs/")
    print("• Scripts: scripts/")
    print("• Dados: raw/")
    print()
    print("🌐 ACESSOS:")
    print("• pgAdmin: http://localhost:8080")
    print("  - Email: admin@sbd2.com")
    print("  - Senha: admin123")
    print()
    print("• Banco de Dados: localhost:5432")
    print("  - Database: sbd2_lakehouse")
    print("  - User: sbd2_user")
    print("  - Password: sbd2_password")
    print()
    print("📋 PRÓXIMOS PASSOS:")
    print("1. Execute: jupyter notebook notebooks/")
    print("2. Analise os dados com os notebooks")
    print("3. Monitore os logs em: automation.log")
    print("4. Consulte a documentação em: docs/")
    print()
    print("🔧 COMANDOS ÚTEIS:")
    print("• Parar containers: docker-compose -f docker/docker-compose.yml down")
    print("• Reiniciar: python run_all.py")
    print("• Validar: python scripts/validate_setup.py")
    print()
    print("=" * 60)

def main():
    """Função principal"""
    print_banner()
    
    # Executa todas as etapas
    steps = [
        ("Setup", run_setup),
        ("Validação", run_validation),
        ("Automação", run_automation)
    ]
    
    success_count = 0
    total_steps = len(steps)
    
    for step_name, step_function in steps:
        try:
            if step_function():
                success_count += 1
            else:
                print(f"⚠️  {step_name} falhou, mas continuando...")
        except Exception as e:
            print(f"❌ Erro em {step_name}: {e}")
    
    # Exibe resultados
    show_results()
    
    # Status final
    if success_count == total_steps:
        print("🎉 TODAS AS ETAPAS CONCLUÍDAS COM SUCESSO!")
        sys.exit(0)
    else:
        print(f"⚠️  {success_count}/{total_steps} etapas concluídas")
        print("Verifique os logs para detalhes dos erros")
        sys.exit(1)

if __name__ == "__main__":
    main()
