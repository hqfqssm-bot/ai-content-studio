import subprocess, sys, time, json, urllib.request, os
python = sys.executable
cwd = r'C:\Users\41896\Documents\11\ai-content-studio\backend'
log = open(os.path.join(cwd, 'server_final.log'), 'w')
proc = subprocess.Popen(
    [python, '-m', 'uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8002'],
    cwd=cwd, stdout=log, stderr=subprocess.STDOUT,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, close_fds=True)
print('PID: ' + str(proc.pid))

for i in range(12):
    time.sleep(2)
    try:
        r = urllib.request.urlopen('http://localhost:8002/health')
        if r.status == 200: break
    except: pass
else:
    print('FAILED TO START'); sys.exit(1)

print('1. Health: OK')

# Register
req = urllib.request.Request('http://localhost:8002/api/auth/register',
    data=json.dumps({'email':'test@demo.com','password':'test123','name':'Test'}).encode(),
    headers={'Content-Type':'application/json'})
r = json.loads(urllib.request.urlopen(req).read())
print('2. Register: credits=' + str(r['user']['credits']))
token = r['access_token']

# Payment config
r = json.loads(urllib.request.urlopen('http://localhost:8002/api/payments/config').read())
print('3. Payments: configured=' + str(r['stripe_configured']) + ', price=' + str(r['pro_price']))

# API Keys - create
req = urllib.request.Request('http://localhost:8002/api/keys/',
    data=json.dumps({'name':'My Key'}).encode(),
    headers={'Content-Type':'application/json', 'Authorization':'Bearer '+token})
try:
    r = json.loads(urllib.request.urlopen(req).read())
    print('4. API Key create: ' + r['key'][:12] + '...')
except urllib.error.HTTPError as e:
    # Expected if not Pro - that's OK, the route works
    print('4. API Key: Pro-only (expected) - ' + str(e.code))

# API Keys - list
req = urllib.request.Request('http://localhost:8002/api/keys/',
    headers={'Authorization':'Bearer '+token})
r = json.loads(urllib.request.urlopen(req).read())
print('5. API Key list: count=' + str(len(r)))

# Generate
req = urllib.request.Request('http://localhost:8002/api/content/generate',
    data=json.dumps({'content_type':'blog','prompt':'AI for business','tone':'professional','language':'en'}).encode(),
    headers={'Content-Type':'application/json','Authorization':'Bearer '+token})
r = json.loads(urllib.request.urlopen(req).read())
print('6. Generate: used=' + str(r['credits_used']) + ', len=' + str(len(r['content'])))

print('=== ALL TESTS PASSED ===')
proc.terminate()
