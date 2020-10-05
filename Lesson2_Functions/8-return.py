def divide_by_four(input_number):
  return input_number/4
  
result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")


def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
  
my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)


print("I am "+str(my_age)+" years old and my dad is "+str(dads_age)+" years old")