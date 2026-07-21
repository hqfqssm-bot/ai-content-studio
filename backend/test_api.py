import urllib.request, json, time

# Register user
req = urllib.request.Request('http://localhost:8002/api/auth/register', 
    data=json.dumps({"email":"test@demo.com","password":"test123","name":"Test User"}).encode(),
    headers={'Content-Type':'application/json'})
resp = json.loads(urllib.request.urlopen(req).read())
print('Register: credits=' + str(resp["user"]["credits"]) + ', is_pro=' + str(resp["user"]["is_pro"]))
token = resp['access_token']

# Credits
req = urllib.request.Request('http://localhost:8002/api/auth/credits',
    headers={'Authorization': 'Bearer ' + token})
cred = json.loads(urllib.request.urlopen(req).read())
print('Credits: ' + str(cred["credits"]))

# Pricing
pricing = json.loads(urllib.request.urlopen('http://localhost:8002/api/content/pricing').read())
print('Pricing: free=' + str(pricing["free"]["credits"]) + ', pro_monthly=$' + str(pricing["pro"]["price_monthly"]))

# Generate content  
gen_req = urllib.request.Request('http://localhost:8002/api/content/generate',
    data=json.dumps({"content_type":"blog","prompt":"AI for business","tone":"professional","language":"en"}).encode(),
    headers={'Content-Type':'application/json', 'Authorization': 'Bearer ' + token})
gen = json.loads(urllib.request.urlopen(gen_req).read())
print('Generate: type=' + gen["content_type"] + ', credits_used=' + str(gen["credits_used"]) + ', length=' + str(len(gen["content"])))

# History
hist_req = urllib.request.Request('http://localhost:8002/api/content/history',
    headers={'Authorization': 'Bearer ' + token})
hist = json.loads(urllib.request.urlopen(hist_req).read())
print('History: ' + str(len(hist)) + ' items')
print('ALL TESTS PASSED')
