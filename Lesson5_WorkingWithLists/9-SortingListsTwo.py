names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

sorted_names = sorted(names)
print(sorted_names)

# ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

print(names)
# ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print(games_sorted)


#Review

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = (len(inventory))

first = inventory[1]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()