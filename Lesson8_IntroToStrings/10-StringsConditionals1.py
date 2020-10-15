favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

#2

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False