Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\Users\41896\Documents\11\ai-content-studio\backend"
pythonPath = "C:\Users\41896\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
WshShell.Run pythonPath & " -m uvicorn app.main:app --host 0.0.0.0 --port 8000", 0, False
