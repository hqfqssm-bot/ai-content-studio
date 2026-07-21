@echo off
title AI Content Studio - Demo Server
echo Starting AI Content Studio server...
echo Open http://localhost:8000 in your browser
echo Press Ctrl+C to stop
echo ==========================================
cd /d "C:\Users\41896\Documents\11\ai-content-studio\backend"
"C:\Users\41896\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m uvicorn app.main:app --host 0.0.0.0 --port 8000
pause
