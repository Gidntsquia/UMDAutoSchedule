import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.planetterp.com/v1/professor', params={
  'name': 'Larry Herman'
}, headers = headers)

print(r.json())


import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.planetterp.com/v1/grades', headers = headers, params={
      'course': 'ENGL101',
      'professor': 'William Pittman'
})

print(r.json())

