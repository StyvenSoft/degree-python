words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)

print(usernames)
# ["@coolguy35", "@kewldawg54", "@matchamom"]

usernames = [word for word in words if word[0] == '@']

# ["@coolguy35", "@kewldawg54", "@matchamom"]

# Example

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

# [164, 170, 163, 163]