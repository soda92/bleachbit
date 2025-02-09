$root = Split-Path $PSScriptRoot -Parent
$python = Join-Path $root "bleachbit_venv/bin/python.exe"
$Env:PYTHONPATH += ";$root"
& $python $PSScriptRoot/impl.py
