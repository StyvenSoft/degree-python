# key_to_check = "Landmark 81"
# try:
#   print(building_heights[key_to_check])
# except KeyError:
#   print("That key doesn't exist!")


caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30

try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")

#30