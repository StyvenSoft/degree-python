
print([i -1 for i in range(5)])

# [-1, 0, 1, 2, 3]

numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    break
  print(number)

for i in range(3):
  print(5)

# 1
# 1
# 5
# 5
# 5

drink_choices = ["coffee", "tea", "water", "juice", "soda"]
for drink in drink_choices:
  print(drink)

# coffee
# tea
# water
# juice
# soda

for i in range(3):
  print(i)

# 0
# 1
# 2

practices = range(3)

for practice in practices:
    print("practice more")

# practice more
# practice more
# practice more

def odd_nums(lst):
  for item in lst:
    if item % 2 == 1:
      print(item)

odd_nums([4, 7, 9, 10, 13])

# 7
# 9
# 13