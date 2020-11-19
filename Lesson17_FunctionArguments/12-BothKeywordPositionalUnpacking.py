def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()
  for arg in args:
    text = text.replace(arg, "")
  for kwarg, replacement in kwargs.items():
    text = text.replace(kwarg, replacement)
  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))

## King Richard often thought upon what he had seen of Mr. Robin Hood and his fellows. 
# He was very amused by of archery; he had heard of many  actions that were told about them, and he admired their  spirit and manners. 
# Thought he, If I could but make these men my faithful subjects, what a pride they would be to my court! The king at last fixed upon a plan by which he might see Mr. Robin Hood once more.