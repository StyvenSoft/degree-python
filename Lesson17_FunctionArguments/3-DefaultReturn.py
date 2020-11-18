def no_return():
  print("You've hit the point of no return")
  # notice no return statement
 
here_it_is = no_return()
 
print(here_it_is)
# Prints out "None"

def fifty_percent_off(item):
  # Check if item.cost exists
  if hasattr(item, 'cost'):
    return item.cost / 2
 
  # If not, return None 
  return
 
sale_price = fifty_percent_off(200)
 
if sale_price is None:
  print("This product is not for sale!")


# store the result of this print() statement in the variable prints_return
prints_return = print("What does this print function return?")

# print out the value of prints_return
print(prints_return)

# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]
list_sort_return = sort_this_list.sort()

# print out the value of list_sort_return
print(list_sort_return)

# What does this print function return?
# None
# None
