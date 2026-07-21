@echo off
start /B "" "C:\Users\41896\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m uvicorn app.main:app --host 0.0.0.0 --port 8002 > "C:\Users\41896\Documents\11\ai-content-studio\backend\server.log" 2>&1
