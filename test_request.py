import requests

with open('../request.json', 'r') as f:
    data = f.read()


request = requests.post('https://localhost:9001/722520790:AAEM0nUuaAD9BWFp0jv58VkeX3m-85DQOq0', data=data)
