#!/usr/bin/env python3
"""
Script de validação do setup
Verifica se todos os componentes estão funcionando corretamente
"""

import os
import sys
import subprocess
import psycopg2
from pathlib import Path
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_file_structure():
    """Verifica se a estrutura de arquivos está correta"""
    logger.info("Verificando estrutura de arquivos...")
    
    required_files = [
        "docker/docker-compose.yml",
        "docker/init.sql",
        "scripts/run_etl.py",
        "scripts/run_automation.py",
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
        ".gitignore"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        logger.error(f"Arquivos ausentes: {missing_files}")
        return False
    
    logger.info("✓ Estrutura de arquivos OK")
    return True

def check_docker():
    """Verifica se Docker está funcionando"""
    logger.info("Verificando Docker...")
    
    try:
        result = subprocess.run("docker --version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            logger.info(f"✓ Docker disponível: {result.stdout.strip()}")
            return True
        else:
            logger.error("✗ Docker não está funcionando")
            return False
    except Exception as e:
        logger.error(f"✗ Erro ao verificar Docker: {e}")
        return False

def check_docker_containers():
    """Verifica se os containers estão rodando"""
    logger.info("Verificando containers Docker...")
    
    try:
        result = subprocess.run("docker ps", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            if "sbd2_postgres" in result.stdout:
                logger.info("✓ Container PostgreSQL rodando")
                return True
            else:
                logger.warning("⚠️  Container PostgreSQL não está rodando")
                return False
        else:
            logger.error("✗ Erro ao verificar containers")
            return False
    except Exception as e:
        logger.error(f"✗ Erro ao verificar containers: {e}")
        return False

def check_database_connection():
    """Verifica conexão com o banco de dados"""
    logger.info("Verificando conexão com banco de dados...")
    
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            database='sbd2_lakehouse',
            user='sbd2_user',
            password='sbd2_password'
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        if result:
            logger.info("✓ Conexão com banco de dados OK")
            return True
        else:
            logger.error("✗ Falha na consulta ao banco")
            return False
            
    except Exception as e:
        logger.error(f"✗ Erro ao conectar ao banco: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

def check_silver_tables():
    """Verifica se as tabelas Silver existem"""
    logger.info("Verificando tabelas Silver...")
    
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            database='sbd2_lakehouse',
            user='sbd2_user',
            password='sbd2_password'
        )
        
        cursor = conn.cursor()
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'silver'
        """)
        
        tables = cursor.fetchall()
        table_names = [t[0] for t in tables]
        
        expected_tables = ['train_data', 'data_metadata', 'processing_logs']
        missing_tables = [t for t in expected_tables if t not in table_names]
        
        if missing_tables:
            logger.error(f"✗ Tabelas ausentes: {missing_tables}")
            return False
        
        logger.info(f"✓ Tabelas Silver OK: {table_names}")
        return True
        
    except Exception as e:
        logger.error(f"✗ Erro ao verificar tabelas: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

def check_data_file():
    """Verifica se o arquivo de dados existe"""
    logger.info("Verificando arquivo de dados...")
    
    data_file = Path("raw/train.csv")
    if data_file.exists():
        size_gb = data_file.stat().st_size / (1024*1024*1024)
        logger.info(f"✓ Arquivo de dados OK: {size_gb:.2f} GB")
        return True
    else:
        logger.error("✗ Arquivo raw/train.csv não encontrado")
        return False

def check_python_packages():
    """Verifica se os pacotes Python estão instalados"""
    logger.info("Verificando pacotes Python...")
    
    required_packages = [
        'pandas',
        'numpy',
        'psycopg2',
        'sqlalchemy',
        'matplotlib',
        'seaborn'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        logger.error(f"✗ Pacotes ausentes: {missing_packages}")
        logger.error("Execute: pip install -r scripts/requirements.txt")
        return False
    
    logger.info("✓ Pacotes Python OK")
    return True

def generate_report():
    """Gera relatório de validação"""
    logger.info("Gerando relatório de validação...")
    
    report = {
        "timestamp": "2025-10-10",
        "checks": {
            "file_structure": check_file_structure(),
            "docker": check_docker(),
            "containers": check_docker_containers(),
            "database": check_database_connection(),
            "silver_tables": check_silver_tables(),
            "data_file": check_data_file(),
            "python_packages": check_python_packages()
        }
    }
    
    # Salva relatório
    with open("validation_report.txt", "w") as f:
        f.write("=== RELATÓRIO DE VALIDAÇÃO ===\n")
        f.write(f"Data: {report['timestamp']}\n\n")
        
        for check, status in report["checks"].items():
            status_text = "✓ OK" if status else "✗ FALHA"
            f.write(f"{check}: {status_text}\n")
        
        f.write("\n=== RESUMO ===\n")
        total_checks = len(report["checks"])
        passed_checks = sum(report["checks"].values())
        f.write(f"Checks passou: {passed_checks}/{total_checks}\n")
        f.write(f"Status: {'SUCESSO' if passed_checks == total_checks else 'FALHA'}\n")
    
    logger.info("Relatório salvo em: validation_report.txt")
    return report

def main():
    """Função principal de validação"""
    logger.info("=== INICIANDO VALIDAÇÃO DO SETUP ===")
    
    # Executa todos os checks
    report = generate_report()
    
    # Resumo final
    total_checks = len(report["checks"])
    passed_checks = sum(report["checks"].values())
    
    logger.info("=== VALIDAÇÃO CONCLUÍDA ===")
    logger.info(f"Checks passou: {passed_checks}/{total_checks}")
    
    if passed_checks == total_checks:
        logger.info("🎉 SETUP VALIDADO COM SUCESSO!")
        logger.info("O projeto está pronto para uso.")
        logger.info("Execute: python scripts/run_automation.py")
    else:
        logger.error("❌ SETUP COM PROBLEMAS")
        logger.error("Verifique os erros acima e corrija antes de continuar.")
        sys.exit(1)

if __name__ == "__main__":
    main()
