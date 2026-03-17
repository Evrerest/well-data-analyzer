$python = "C:\Users\ekost\AppData\Local\Programs\Python\Python312\python.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}

& $python -m streamlit run app.py
