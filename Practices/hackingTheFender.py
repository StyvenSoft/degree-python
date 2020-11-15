import csv
import json

compromised_users = []

with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        #print(password_row)
        compromised_users.append(password_row['Username'])

print(compromised_users)

with open('compromised_users.txt', 'w') as compromised_user_file:
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)

with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {
        'recipient': 'The boss',
        'message': 'Mission Success'
    }
    json.dump(boss_message_dict, boss_message)

with open('new_passwords.csv', 'w') as new_password_obj:
    slash_null_sig = """
      ______    _                                                           
.' ____ \  / |_                                                         
| (___ \_|`| |-'.---.  _   __  .---.  .---.  _ .--.                     
 _.____`.  | | / /__\\[ \ [  ]/ /__\\/ /__\\[ `.-. |                    
| \____) | | |,| \__., \ \/ / | \__.,| \__., | | | |                    
 \______.' \__/ '.__.'  \__/   '.__.' '.__.'[___||__]                   
    ________         __                                             _   
   |_   __  |       [  |                                           (_)  
     | |_ \_| .---.  | |--.  .---.  _   __  .---.  _ .--.  _ .--.  __   
     |  _| _ / /'`\] | .-. |/ /__\\[ \ [  ]/ /__\\[ `/'`\][ `/'`\][  |  
    _| |__/ || \__.  | | | || \__., \ \/ / | \__., | |     | |     | |  
   |________|'.___.'[___]|__]'.__.'  \__/   '.__.'[___]   [___]   [___] 
"""
    new_password_obj.write(slash_null_sig)
