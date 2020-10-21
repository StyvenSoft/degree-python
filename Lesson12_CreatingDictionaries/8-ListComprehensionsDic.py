names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}


drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key: value for key, value in zipped_drinks}

# Exercise

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

list1 = {"fruit": "apple", "vegetable": 100, "spice": ["salt", "paprika", "saffron"]}

list2 = {2: ["apple", "orange"], 1: ["broccoli"], 3: ["salt", "paprika", "saffron"]}

print(list1, list2)


inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20}

inventory["invisible knife"] = 40
inventory["mithril shield"] = 25

print(inventory)
# {'iron spear': 12, 'invisible knife': 40, 'needle of ambition': 10, 'stone glove': 20, 'mithril shield': 25}

conference_rooms = ["executive", "hopper", "lovelace", "pod", "snooze booth"]
capacity = [7, 20, 6, 2, 1]
room_dict = {key:value for key, value in zip(conference_rooms, capacity)}

print(room_dict)