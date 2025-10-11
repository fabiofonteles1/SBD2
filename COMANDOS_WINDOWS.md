# 💻 COMANDOS ESPECÍFICOS PARA WINDOWS

## 🖥️ COMANDOS POWERSHELL

### Navegação e Verificação
```powershell
# Navegar para o diretório do projeto
cd "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2"

# Verificar diretório atual
Get-Location

# Listar arquivos e pastas
Get-ChildItem

# Verificar se arquivo de dados existe
Test-Path "raw\train.csv"

# Verificar tamanho do arquivo
(Get-Item "raw\train.csv").Length / 1GB
```

### Verificação de Pré-requisitos
```powershell
# Verificar Python
python --version

# Verificar Docker
docker --version

# Verificar Git
git --version

# Verificar se Docker está rodando
docker info
```

### Execução do Projeto
```powershell
# Execução completa (recomendado)
python run_all.py

# Setup manual
python setup.py

# Validação
python scripts\validate_setup.py

# Automação
python scripts\run_automation.py
```

### Gerenciamento de Containers Docker
```powershell
# Verificar containers rodando
docker ps

# Parar containers
docker-compose -f docker\docker-compose.yml down

# Iniciar containers
docker-compose -f docker\docker-compose.yml up -d

# Ver logs
docker-compose -f docker\docker-compose.yml logs

# Ver logs em tempo real
docker-compose -f docker\docker-compose.yml logs -f
```

### Verificação de Portas
```powershell
# Verificar se porta 5432 está em uso
netstat -an | findstr :5432

# Verificar se porta 8080 está em uso
netstat -an | findstr :8080

# Verificar todas as portas em uso
netstat -an | findstr LISTENING
```

### Gerenciamento de Processos
```powershell
# Ver processos Python
Get-Process python

# Ver processos Docker
Get-Process docker

# Matar processo específico
Stop-Process -Name "python" -Force
```

### Verificação de Logs
```powershell
# Ver conteúdo dos logs
Get-Content automation.log
Get-Content etl.log
Get-Content validation_report.txt

# Ver últimas 10 linhas
Get-Content automation.log -Tail 10

# Ver logs em tempo real
Get-Content automation.log -Wait
```

### Limpeza do Sistema
```powershell
# Parar todos os containers
docker-compose -f docker\docker-compose.yml down -v

# Remover volumes Docker
docker volume prune -f

# Limpar logs
Remove-Item automation.log, etl.log, validation_report.txt -ErrorAction SilentlyContinue

# Limpar cache Python
python -m pip cache purge
```

### Backup e Restauração
```powershell
# Backup do banco de dados
docker exec sbd2_postgres pg_dump -U sbd2_user sbd2_lakehouse > backup.sql

# Restaurar banco de dados
Get-Content backup.sql | docker exec -i sbd2_postgres psql -U sbd2_user sbd2_lakehouse

# Backup de arquivos
Copy-Item "raw\train.csv" "backup\train_backup.csv"
```

### Verificação de Recursos do Sistema
```powershell
# Ver uso de memória
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5

# Ver uso de CPU
Get-Counter "\Processor(_Total)\% Processor Time"

# Ver espaço em disco
Get-WmiObject -Class Win32_LogicalDisk | Select-Object DeviceID, @{Name="Size(GB)";Expression={[math]::Round($_.Size/1GB,2)}}, @{Name="FreeSpace(GB)";Expression={[math]::Round($_.FreeSpace/1GB,2)}}
```

### Troubleshooting Específico para Windows
```powershell
# Verificar se Docker Desktop está rodando
Get-Service | Where-Object {$_.Name -like "*docker*"}

# Reiniciar Docker Desktop
Restart-Service docker

# Verificar firewall
Get-NetFirewallRule | Where-Object {$_.DisplayName -like "*docker*"}

# Verificar antivírus (pode bloquear Docker)
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```

### Comandos de Rede
```powershell
# Testar conectividade com banco
Test-NetConnection -ComputerName localhost -Port 5432

# Testar conectividade com pgAdmin
Test-NetConnection -ComputerName localhost -Port 8080

# Ver configurações de rede
ipconfig /all
```

### Verificação de Permissões
```powershell
# Verificar permissões do diretório
Get-Acl "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2" | Format-List

# Verificar se pode escrever no diretório
Test-Path "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2" -PathType Container
```

### Monitoramento em Tempo Real
```powershell
# Monitorar uso de CPU e memória
while ($true) {
    Clear-Host
    Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, CPU, WorkingSet
    Start-Sleep -Seconds 2
}

# Monitorar logs em tempo real
Get-Content automation.log -Wait -Tail 5
```

### Comandos de Desenvolvimento
```powershell
# Instalar dependências
pip install -r scripts\requirements.txt

# Atualizar dependências
pip install --upgrade -r scripts\requirements.txt

# Verificar dependências instaladas
pip list

# Criar ambiente virtual (opcional)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Comandos Git
```powershell
# Inicializar repositório
git init

# Adicionar arquivos
git add .

# Commit
git commit -m "Initial commit"

# Ver status
git status

# Ver histórico
git log --oneline
```

### Comandos de Limpeza Avançada
```powershell
# Limpar cache Docker
docker system prune -a

# Limpar imagens não utilizadas
docker image prune -a

# Limpar containers parados
docker container prune

# Limpar redes não utilizadas
docker network prune

# Limpeza completa do Docker
docker system prune -a --volumes
```

### Verificação de Integridade
```powershell
# Verificar integridade do arquivo de dados
Get-FileHash "raw\train.csv" -Algorithm SHA256

# Verificar se arquivo não está corrompido
Get-Content "raw\train.csv" -Head 1
Get-Content "raw\train.csv" -Tail 1

# Verificar permissões de leitura
Get-Acl "raw\train.csv" | Format-List
```

### Comandos de Diagnóstico
```powershell
# Verificar eventos do sistema
Get-EventLog -LogName Application -Source "Docker Desktop" -Newest 10

# Verificar processos que usam porta 5432
Get-NetTCPConnection -LocalPort 5432

# Verificar processos que usam porta 8080
Get-NetTCPConnection -LocalPort 8080
```

---

## 🚨 SOLUÇÕES PARA PROBLEMAS COMUNS NO WINDOWS

### Problema: "Execution Policy" do PowerShell
```powershell
# Verificar política atual
Get-ExecutionPolicy

# Alterar política (como administrador)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: Docker Desktop não inicia
```powershell
# Verificar se Hyper-V está habilitado
Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V

# Reiniciar serviço Docker
Restart-Service docker
```

### Problema: Porta já em uso
```powershell
# Encontrar processo usando porta 5432
Get-NetTCPConnection -LocalPort 5432 | Select-Object OwningProcess

# Matar processo específico
Stop-Process -Id <PID> -Force
```

### Problema: Permissões de arquivo
```powershell
# Dar permissão total ao usuário
icacls "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2" /grant "fabio:F" /T
```

---

## 📝 NOTAS IMPORTANTES

1. **Sempre execute como Administrador** quando necessário
2. **Verifique o antivírus** - pode bloquear Docker
3. **Mantenha Docker Desktop rodando** durante todo o processo
4. **Use PowerShell** em vez do CMD para melhor compatibilidade
5. **Monitore os logs** para identificar problemas rapidamente

---

*Comandos específicos para Windows PowerShell - Data Lakehouse SBD-2* 💻
