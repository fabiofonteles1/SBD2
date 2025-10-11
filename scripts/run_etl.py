#!/usr/bin/env python3
"""
Script de automação para execução do ETL
Executa a criação do banco/tabelas e o processamento dos dados
"""

import os
import sys
import psycopg2
import pandas as pd
from pathlib import Path
import logging
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configurações do banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'sbd2_lakehouse',
    'user': 'sbd2_user',
    'password': 'sbd2_password'
}

def connect_to_db():
    """Conecta ao banco de dados PostgreSQL"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        logger.info("Conexão com banco de dados estabelecida")
        return conn
    except Exception as e:
        logger.error(f"Erro ao conectar ao banco: {e}")
        sys.exit(1)

def execute_ddl():
    """Executa os scripts DDL para criar as tabelas"""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        
        # Lê o script DDL
        ddl_path = Path('docker/init.sql')
        if ddl_path.exists():
            with open(ddl_path, 'r', encoding='utf-8') as f:
                ddl_script = f.read()
            
            # Executa o script
            cursor.execute(ddl_script)
            conn.commit()
            logger.info("Script DDL executado com sucesso")
        else:
            logger.error("Arquivo DDL não encontrado")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Erro ao executar DDL: {e}")
        sys.exit(1)
    finally:
        if 'conn' in locals():
            conn.close()

def log_processing_start(process_name):
    """Registra o início de um processo"""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO silver.processing_logs (process_name, status, started_at)
            VALUES (%s, %s, %s)
        """, (process_name, 'STARTED', datetime.now()))
        
        conn.commit()
        logger.info(f"Processo {process_name} iniciado")
        
    except Exception as e:
        logger.error(f"Erro ao registrar início do processo: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

def log_processing_end(process_name, status, records_processed=None, error_message=None):
    """Registra o fim de um processo"""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE silver.processing_logs 
            SET status = %s, records_processed = %s, error_message = %s, completed_at = %s
            WHERE process_name = %s AND status = 'STARTED'
            ORDER BY started_at DESC LIMIT 1
        """, (status, records_processed, error_message, datetime.now(), process_name))
        
        conn.commit()
        logger.info(f"Processo {process_name} finalizado com status: {status}")
        
    except Exception as e:
        logger.error(f"Erro ao registrar fim do processo: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

def run_etl():
    """Executa o processo ETL principal"""
    process_name = "ETL_RAW_TO_SILVER"
    
    try:
        # Log início do processo
        log_processing_start(process_name)
        
        # Verifica se o arquivo de dados existe
        data_path = Path('raw/train.csv')
        if not data_path.exists():
            raise FileNotFoundError("Arquivo train.csv não encontrado em raw/")
        
        logger.info(f"Processando arquivo: {data_path}")
        logger.info(f"Tamanho do arquivo: {data_path.stat().st_size / (1024*1024*1024):.2f} GB")
        
        # Leitura em chunks para arquivos grandes
        chunk_size = 10000
        total_records = 0
        
        conn = connect_to_db()
        cursor = conn.cursor()
        
        # Processa o arquivo em chunks
        for chunk in pd.read_csv(data_path, chunksize=chunk_size):
            # Aqui seria implementada a lógica de transformação
            # Por enquanto, apenas conta os registros
            total_records += len(chunk)
            
            if total_records % 100000 == 0:
                logger.info(f"Processados {total_records:,} registros")
        
        # Log sucesso
        log_processing_end(process_name, 'SUCCESS', total_records)
        logger.info(f"ETL concluído com sucesso. Total de registros: {total_records:,}")
        
    except Exception as e:
        # Log erro
        log_processing_end(process_name, 'ERROR', error_message=str(e))
        logger.error(f"Erro no ETL: {e}")
        sys.exit(1)
    finally:
        if 'conn' in locals():
            conn.close()

def main():
    """Função principal"""
    logger.info("=== INICIANDO AUTOMAÇÃO ETL ===")
    
    # 1. Executa DDL
    logger.info("1. Executando DDL...")
    execute_ddl()
    
    # 2. Executa ETL
    logger.info("2. Executando ETL...")
    run_etl()
    
    logger.info("=== AUTOMAÇÃO CONCLUÍDA ===")

if __name__ == "__main__":
    main()
