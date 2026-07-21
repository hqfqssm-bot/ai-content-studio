import subprocess, sys, os, time
python = sys.executable
cwd = r'C:\Users\41896\Documents\11\ai-content-studio\backend'
log = open(r'C:\Users\41896\Documents\11\ai-content-studio\backend\demo_server.log', 'w')
proc = subprocess.Popen(
    [python, '-m', 'uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8000'],
    cwd=cwd, stdout=log, stderr=subprocess.STDOUT,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
    close_fds=True)
with open(r'C:\Users\41896\Documents\11\ai-content-studio\backend\demo.pid', 'w') as f:
    f.write(str(proc.pid))
for i in range(10):
    time.sleep(2)
    try:
        r = __import__('urllib.request').request.urlopen('http://localhost:8000/health')
        if r.status == 200:
            print('SERVER STARTED - PID: ' + str(proc.pid))
            break
    except: pass
else:
    with open(r'C:\Users\41896\Documents\11\ai-content-studio\backend\demo_server.log') as f:
        print('FAILED: ' + f.read())
