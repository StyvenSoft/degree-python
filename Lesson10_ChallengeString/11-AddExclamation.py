# Write your add_exclamation function here:
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

# Uncomment these function calls to test your function:
print(add_exclamation("Internet"))
# should print Internet!!!!!!!!!!
print(add_exclamation("Internet is the best place to learn"))
# should print Internet is the best place to learn