#!/usr/bin/env python3
"""
Script principal de automação
Orquestra a criação do banco, execução do DDL e processamento ETL
"""

import os
import sys
import subprocess
import time
import logging
from pathlib import Path

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_command(command, description):
    """Executa um comando e registra o resultado"""
    logger.info(f"Iniciando: {description}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            logger.info(f"✓ {description} - Sucesso")
            if result.stdout:
                logger.info(f"Output: {result.stdout}")
        else:
            logger.error(f"✗ {description} - Erro")
            logger.error(f"Error: {result.stderr}")
            return False
    except Exception as e:
        logger.error(f"✗ {description} - Exceção: {e}")
        return False
    return True

def check_docker():
    """Verifica se o Docker está rodando"""
    logger.info("Verificando Docker...")
    result = subprocess.run("docker --version", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        logger.info("✓ Docker está disponível")
        return True
    else:
        logger.error("✗ Docker não está disponível")
        return False

def start_docker_services():
    """Inicia os serviços Docker"""
    logger.info("Iniciando serviços Docker...")
    
    # Navega para o diretório docker
    docker_dir = Path("docker")
    if not docker_dir.exists():
        logger.error("Diretório docker não encontrado")
        return False
    
    # Para containers existentes
    run_command("docker-compose -f docker/docker-compose.yml down", "Parando containers existentes")
    
    # Inicia os serviços
    if not run_command("docker-compose -f docker/docker-compose.yml up -d", "Iniciando containers"):
        return False
    
    # Aguarda os serviços ficarem prontos
    logger.info("Aguardando serviços ficarem prontos...")
    time.sleep(30)
    
    return True

def wait_for_database():
    """Aguarda o banco de dados ficar disponível"""
    logger.info("Aguardando banco de dados...")
    
    import psycopg2
    max_attempts = 30
    attempt = 0
    
    while attempt < max_attempts:
        try:
            conn = psycopg2.connect(
                host='localhost',
                port=5432,
                database='sbd2_lakehouse',
                user='sbd2_user',
                password='sbd2_password'
            )
            conn.close()
            logger.info("✓ Banco de dados disponível")
            return True
        except Exception as e:
            attempt += 1
            logger.info(f"Tentativa {attempt}/{max_attempts} - Aguardando banco...")
            time.sleep(10)
    
    logger.error("✗ Banco de dados não ficou disponível")
    return False

def run_etl():
    """Executa o processo ETL"""
    logger.info("Executando ETL...")
    
    # Verifica se o arquivo de dados existe
    data_file = Path("raw/train.csv")
    if not data_file.exists():
        logger.error("Arquivo raw/train.csv não encontrado")
        return False
    
    # Executa o script ETL
    if not run_command("python scripts/run_etl.py", "Executando ETL"):
        return False
    
    return True

def validate_lakehouse():
    """Valida se o lakehouse foi populado corretamente"""
    logger.info("Validando lakehouse...")
    
    try:
        import psycopg2
        
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            database='sbd2_lakehouse',
            user='sbd2_user',
            password='sbd2_password'
        )
        cursor = conn.cursor()
        
        # Verifica se as tabelas existem
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'silver'
        """)
        
        tables = cursor.fetchall()
        logger.info(f"Tabelas encontradas no schema silver: {[t[0] for t in tables]}")
        
        # Verifica logs de processamento
        cursor.execute("""
            SELECT process_name, status, records_processed, completed_at
            FROM silver.processing_logs
            ORDER BY completed_at DESC
            LIMIT 5
        """)
        
        logs = cursor.fetchall()
        logger.info("Últimos logs de processamento:")
        for log in logs:
            logger.info(f"  {log[0]} - {log[1]} - {log[2]} registros - {log[3]}")
        
        conn.close()
        logger.info("✓ Lakehouse validado com sucesso")
        return True
        
    except Exception as e:
        logger.error(f"✗ Erro ao validar lakehouse: {e}")
        return False

def main():
    """Função principal de automação"""
    logger.info("=== INICIANDO AUTOMAÇÃO COMPLETA ===")
    
    # 1. Verificar Docker
    if not check_docker():
        logger.error("Docker não está disponível. Encerrando.")
        sys.exit(1)
    
    # 2. Iniciar serviços Docker
    if not start_docker_services():
        logger.error("Falha ao iniciar serviços Docker. Encerrando.")
        sys.exit(1)
    
    # 3. Aguardar banco de dados
    if not wait_for_database():
        logger.error("Banco de dados não ficou disponível. Encerrando.")
        sys.exit(1)
    
    # 4. Executar ETL
    if not run_etl():
        logger.error("Falha no ETL. Encerrando.")
        sys.exit(1)
    
    # 5. Validar lakehouse
    if not validate_lakehouse():
        logger.error("Falha na validação do lakehouse. Encerrando.")
        sys.exit(1)
    
    logger.info("=== AUTOMAÇÃO CONCLUÍDA COM SUCESSO ===")
    logger.info("Acesse o pgAdmin em: http://localhost:8080")
    logger.info("Usuário: admin@sbd2.com | Senha: admin123")
    logger.info("Banco: sbd2_lakehouse | Usuário: sbd2_user | Senha: sbd2_password")

if __name__ == "__main__":
    main()
