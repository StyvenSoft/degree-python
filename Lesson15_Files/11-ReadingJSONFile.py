import json
 
with open('message.json') as purchase_json:
  purchase_data = json.load(purchase_json)
 
print(purchase_data['user'])
# Prints 'ellen_greg'

with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])
  print(message['secret text'])

# Now that's JSON!
# Now that's some _serious_ JSON!