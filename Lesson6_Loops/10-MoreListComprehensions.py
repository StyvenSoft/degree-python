usernames = ["@coolguy35", "@kewldawg54", "@matchamom"]

print(usernames)

messages = [user + " please follow me!" for user in usernames]

# ['@coolguy35', '@kewldawg54', '@matchamom']

my_upvotes = [192, 34, 22, 175, 75, 101, 97]

updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]

# Example

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp*(9/5) + 32 for temp in celsius]

print(fahrenheit)

## Review

single_digits = range(10)
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)
  
cubes = [item**3 for item in single_digits]
print(cubes)