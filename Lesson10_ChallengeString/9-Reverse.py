# Write your reverse_string function here:
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

# Uncomment these function calls to test your  function:
print(reverse_string("Learning"))
# should print gninraeL
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print