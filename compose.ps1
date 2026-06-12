param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ComposeArgs
)

$ErrorActionPreference = 'Stop'

$composeFile = Join-Path $PSScriptRoot 'docker-compose.yml'
$envFile = Join-Path $PSScriptRoot '_env'

if (-not (Test-Path -Path $envFile)) {
    Write-Error "Missing _env file at $envFile"
    exit 1
}

if (-not (Test-Path -Path $composeFile)) {
    Write-Error "Missing docker-compose.yml at $composeFile"
    exit 1
}

if (-not $ComposeArgs -or $ComposeArgs.Count -eq 0) {
    Write-Host 'Usage: .\compose.ps1 <docker compose args>'
    Write-Host 'Example: .\compose.ps1 up -d'
    exit 0
}

$composeArgsList = [System.Collections.Generic.List[string]]::new()
$composeArgsList.AddRange($ComposeArgs)

if ($composeArgsList.Count -gt 0 -and $composeArgsList[0] -eq 'up' -and ($composeArgsList -notcontains '-d')) {
    $composeArgsList.Insert(1, '-d')
}

$composeArguments = @('--env-file', $envFile, '-f', $composeFile) + $composeArgsList.ToArray()

& docker compose @composeArguments
$composeExitCode = $LASTEXITCODE

exit $composeExitCode
