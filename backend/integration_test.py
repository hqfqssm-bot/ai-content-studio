import subprocess, sys, time, json, urllib.request, os

python = sys.executable
cwd = r'C:\Users\41896\Documents\11\ai-content-studio\backend'
log_path = os.path.join(cwd, 'server_test.log')
log = open(log_path, 'w')

proc = subprocess.Popen(
    [python, '-m', 'uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8002'],
    cwd=cwd, stdout=log, stderr=subprocess.STDOUT,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
    close_fds=True
)
print('Server PID: ' + str(proc.pid))

for i in range(12):
    time.sleep(2)
    try:
        r = urllib.request.urlopen('http://localhost:8002/health')
        if r.status == 200:
            print('Server started!')
            break
    except:
        pass
else:
    print('STARTUP FAILED')
    with open(log_path) as f:
        print(f.read())
    sys.exit(1)

# 1. Register
req = urllib.request.Request('http://localhost:8002/api/auth/register',
    data=json.dumps({'email':'test@demo.com','password':'test123','name':'Test User'}).encode(),
    headers={'Content-Type':'application/json'})
resp = json.loads(urllib.request.urlopen(req).read())
print('1.Register: credits=' + str(resp['user']['credits']) + ', is_pro=' + str(resp['user']['is_pro']))
token = resp['access_token']

# 2. Credits
req = urllib.request.Request('http://localhost:8002/api/auth/credits',
    headers={'Authorization': 'Bearer ' + token})
cred = json.loads(urllib.request.urlopen(req).read())
print('2.Credits: ' + str(cred['credits']))

# 3. Pricing
pricing = json.loads(urllib.request.urlopen('http://localhost:8002/api/content/pricing').read())
print('3.Pricing: free=' + str(pricing['free']['credits']) + ', pro=' + str(pricing['pro']['price_monthly']))

# 4. Content types
types = json.loads(urllib.request.urlopen('http://localhost:8002/api/content/types').read())
type_names = ', '.join([t['id'] for t in types['types']])
print('4.Content types: ' + str(len(types['types'])) + ' (' + type_names + ')')

# 5. Generate content
req = urllib.request.Request('http://localhost:8002/api/content/generate',
    data=json.dumps({'content_type':'blog','prompt':'AI for business','tone':'professional','language':'en'}).encode(),
    headers={'Content-Type':'application/json','Authorization':'Bearer '+token})
gen = json.loads(urllib.request.urlopen(req).read())
print('5.Generate: type=' + gen['content_type'] + ', used=' + str(gen['credits_used']) + ', len=' + str(len(gen['content'])))

# 6. History
req = urllib.request.Request('http://localhost:8002/api/content/history',
    headers={'Authorization':'Bearer '+token})
hist = json.loads(urllib.request.urlopen(req).read())
print('6.History: ' + str(len(hist)) + ' items')

# 7. Me
req = urllib.request.Request('http://localhost:8002/api/auth/me',
    headers={'Authorization': 'Bearer '+token})
me = json.loads(urllib.request.urlopen(req).read())
print('7.Me: email=' + me['email'] + ', credits=' + str(me['credits']))

print('=== ALL PASSED ===')
proc.terminate()
