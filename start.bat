@echo off
title AI Content Studio - Local Server
echo ==========================================
echo    AI Content Studio - Starting Server
echo ==========================================
echo.
echo Starting backend server on http://localhost:8000
echo.
echo Open http://localhost:8000 in your browser
echo Press Ctrl+C to stop the server
echo ==========================================
echo.
cd /d "%~dp0backend"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
pause
