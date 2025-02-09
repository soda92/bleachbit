$root = Split-Path $PSScriptRoot -Parent
$python = Join-Path $root "bleachbit_venv/bin/python.exe"
# Copy-Item -Recurse -Force "$root/bleachbit" "$root/bleachbit_loader/"
$Env:PYTHONPATH += ";" + $PSScriptRoot
& $python $PSScriptRoot/impl.py
