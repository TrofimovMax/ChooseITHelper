# To work correctly, you need to run once:
# [Environment]::SetEnvironmentVariable("CHOOSEIT_REPORTS_PATH", "project_root_path\reports", "User") 
# [Environment]::SetEnvironmentVariable("PDFLATEX_PATH", "os_path\miktex\bin\x64\pdflatex.exe", "User")
# run it from PowerShell via
# .\compile_all_tex.ps1

$reportsPath = [Environment]::GetEnvironmentVariable("CHOOSEIT_REPORTS_PATH", "User")
$pdflatexPath = [Environment]::GetEnvironmentVariable("PDFLATEX_PATH", "User")

if (-not (Test-Path $reportsPath)) {
    Write-Error "REPORTS path не найден: $reportsPath"
    exit 1
}
if (-not (Test-Path $pdflatexPath)) {
    Write-Error "pdflatex не найден: $pdflatexPath"
    exit 1
}

Set-Location $reportsPath

$texFiles = Get-ChildItem -Filter *.tex
foreach ($file in $texFiles) {
    & $pdflatexPath $file.Name
}
