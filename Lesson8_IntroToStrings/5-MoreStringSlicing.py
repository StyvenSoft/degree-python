favorite_fruit = "blueberry"
length = len(favorite_fruit)
print(length)
# => 9

fruit_sentence = "I love blueberries"
print(len(fruit_sentence))
# => 18

# last_char = favorite_fruit[len(favorite_fruit)]
# print(last_char)
# => IndexError

last_char = favorite_fruit[len(favorite_fruit)-1]
print(last_char)
# => 'y'

length = len(favorite_fruit)
last_chars = favorite_fruit[length-4:]
print(last_chars)
# => 'erry'


first_name = "Steveen"
last_name = "Echeverri"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)

print(temp_password)

# eenrri