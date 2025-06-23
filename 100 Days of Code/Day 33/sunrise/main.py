import requests

parameters = {
    'lat' : -23.112449,
    'lng' : -47.216155,
    'formatted' : 0,
    'tzid' : 'UTC-3',
}

response = (requests.get('https://api.sunrise-sunset.org/json', params= parameters))
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

print(response.json())
