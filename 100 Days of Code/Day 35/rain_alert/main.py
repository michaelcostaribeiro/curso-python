import requests
import datetime
from twilio.rest import Client

api_key = 'eafd274d1e0396b2ad01b1ef28eed27b'
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
# https://api.openweathermap.org/data/2.5/forecast?lat=-23.092602&lon=-47.213982&appid=eafd274d1e0396b2ad01b1ef28eed27b

account_sid = 'AC0242a6f1ef20046174603d34a3d9384c'
auth_token = '7b251d9eb8a984fbccef50312b3dfbcb'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HX350d429d32e64a552466cafecbe95f3c',
  content_variables='{"1":"09/22","2":"3pm"}',
  body= 'Hi',
  to='whatsapp:+5519995762831'
)

print(message.sid)



weather_params = {
    'lat':-23.092602,
    'lon':-47.213982,
    'appid': api_key,
    'cnt':8
}

response = requests.get(OWM_Endpoint, params=weather_params)
utc_datetime = datetime.datetime.fromtimestamp(response.json()['list'][0]['dt'])

day_forecast = []

for i in range(len(response.json()['list'])):
    time = datetime.datetime.fromtimestamp(response.json()['list'][i]['dt'])
    min_temperature = response.json()['list'][i]['main']['temp_min']
    max_temperature = response.json()['list'][i]['main']['temp_max']
    weather_status = response.json()['list'][i]['weather'][0]['description']
    weather_id = response.json()['list'][i]['weather'][0]['id']
    day_forecast.append({
        'time': time,
        'min_temperature': min_temperature,
        'max_temperature':max_temperature,
        'weather_status': weather_status,
        'umbrella_status': 'Bring an umbrella' if weather_id<700 else 'Umbrella is not needed'
    })


for item in day_forecast:
    print('At day: ', item['time'].day)
    print('At hour: ',item['time'].hour)
    print('The min temperature is gonna be: ',item['min_temperature'])
    print('And the max tempeture: ',item['max_temperature'])
    print('The weather status: ',item['weather_status'])
    print(item['umbrella_status'])
    print('\n')
