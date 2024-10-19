# Шлях до директорії для установки Go
$installPath = "C:\Go"

# Перевіряємо, чи Go вже встановлений
if (Get-Command go -ErrorAction SilentlyContinue) {
    Write-Host "Go вже встановлений."
    exit
}

# Завантаження архіву Go
$goVersion = "1.21.1" # Заміни на потрібну версію
$goUrl = "https://golang.org/dl/go$goVersion.windows-amd64.zip"
$zipFile = "$env:TEMP\go.zip"

Invoke-WebRequest -Uri $goUrl -OutFile $zipFile

# Розпаковка архіву
Expand-Archive -Path $zipFile -DestinationPath $installPath

# Додаємо Go до PATH
$env:Path += ";$installPath\bin"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::Machine)

# Очищення
Remove-Item $zipFile

Write-Host "Go успішно встановлено. Перезавантажте PowerShell для використання Go."
