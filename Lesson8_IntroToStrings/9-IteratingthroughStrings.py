def print_each_letter(word):
  for letter in word:
    print(letter)

favorite_color = "blue"
print_each_letter(favorite_color)
# => 'b'
# => 'l'
# => 'u'
# => 'e'

def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter