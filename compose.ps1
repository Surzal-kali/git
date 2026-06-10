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

$shouldPrintTailscaleUrl = $composeArgsList.Count -gt 0 -and $composeArgsList[0] -eq 'up'
$composeArguments = @('--env-file', $envFile, '-f', $composeFile) + $composeArgsList.ToArray()

& docker compose @composeArguments
$composeExitCode = $LASTEXITCODE

if ($composeExitCode -ne 0) {
    exit $composeExitCode
}

if ($shouldPrintTailscaleUrl) {
    Write-Host ''
    $tailscaleLoginOutput = & docker exec tailscale-sidecar tailscale --socket=/tmp/tailscaled.sock up --qr --timeout=10s --accept-dns=false --accept-routes --advertise-routes=172.31.250.0/24 2>&1
    $tailscaleUpExitCode = $LASTEXITCODE
    $loginMatches = $tailscaleLoginOutput |
        Select-String -Pattern 'https://login\.tailscale\.com/\S+' -AllMatches |
        ForEach-Object { $_.Matches.Value } |
        Sort-Object -Unique

    if ($loginMatches) {
        Write-Host 'Tailscale login URL:'
        $loginMatches | ForEach-Object { Write-Host $_ }
    }
    elseif ($tailscaleUpExitCode -eq 0) {
        Write-Host 'Tailscale is already authenticated; no login URL required.'
    }
    else {
        Write-Host 'Failed to request Tailscale login URL:'
        $tailscaleLoginOutput | ForEach-Object { Write-Host $_ }
    }

    if ($tailscaleUpExitCode -eq 0) {
        $tailscaleIpOutput = & docker exec tailscale-sidecar tailscale --socket=/tmp/tailscaled.sock ip -4 2>&1
        $tailscaleIpExitCode = $LASTEXITCODE

        if ($tailscaleIpExitCode -eq 0) {
            $tailscaleIp = $tailscaleIpOutput |
                Select-String -Pattern '^(?:\d{1,3}\.){3}\d{1,3}$' |
                ForEach-Object { $_.Line.Trim() } |
                Select-Object -First 1

            if ($tailscaleIp) {
                Write-Host "Tailscale IPv4: $tailscaleIp"
            }
            else {
                Write-Host 'Tailscale IPv4: unavailable'
            }
        }
        else {
            Write-Host 'Tailscale IPv4: unavailable'
            $tailscaleIpOutput | ForEach-Object { Write-Host $_ }
        }
    }
}

exit 0
