import json


turn_to_json = {
  'eventId': 674189,
  'dateTime': '2020-11-14T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)