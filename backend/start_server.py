import subprocess, sys, os, time
python = r"C:\Users\41896\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
cwd = r"C:\Users\41896\Documents\11\ai-content-studio\backend"
log = open(os.path.join(cwd, "server.log"), "w")
proc = subprocess.Popen(
    [python, '-m', 'uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8002'],
    cwd=cwd,
    stdout=log,
    stderr=subprocess.STDOUT,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
    close_fds=True
)
pid_file = os.path.join(cwd, "server.pid")
with open(pid_file, "w") as f:
    f.write(str(proc.pid))
print(f"Server started with PID {proc.pid}")
