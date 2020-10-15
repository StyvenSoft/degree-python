fruit_prefix = "blue"
fruit_suffix = "berries"

favorite_fruit = fruit_prefix + fruit_suffix
print(favorite_fruit)
# => 'blueberries


fruit_sentence = "My favorite fruit is" + favorite_fruit
print(fruit_sentence)
# => "My favorite fruit isblueberries"

fruit_sentence = "My favorite fruit is " + favorite_fruit
print(fruit_sentence)
# => "My favorite fruit is blueberries"


first_name = "Steven"
last_name = "Echeverri"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)