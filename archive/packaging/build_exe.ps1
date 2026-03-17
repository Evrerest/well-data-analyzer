$python = "C:\Users\ekost\AppData\Local\Programs\Python\Python312\python.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}

& $python -m PyInstaller --clean --noconfirm --distpath dist_release --workpath build_release well_data_analyzer.spec
