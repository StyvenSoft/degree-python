import os

# Function definition with two required parameters
def create_user(username, is_admin):
  print("Create user: " + username)
  print("Set permissions: " + str(is_admin))
 
# Function call with all two required arguments
create_user('johnny_thunder', True)
 
# Raises a "TypeError: Missing 1 required positional argument"
# create_user('djohansen')

# Function defined with one required and one optional parameter
def create_user_Two(username, is_admin=False):
  print("Create user: " + username)
  print("Set permissions: " + str(is_admin))
 
# Calling with two arguments uses the default value for is_admin
create_user_Two('djohansen')


def make_folders(folders_list, nest=False):
  if nest:
    """
    Nest all the folders, like
    ./Music/fun/parliament
    """
    path_to_new_folder = "."
    for folder in folders_list:
      path_to_new_folder += "/{}".format(folder)
      try:
        print(path_to_new_folder)
        os.makedirs("./" + path_to_new_folder)
      except FileExistsError:
        continue
  else:
    """
    Makes all different folders, like
    ./Music/ ./fun/ and ./parliament/
    """
    for folder in folders_list:
      try:
        os.makedirs(folder)

      except FileExistsError:
        continue

make_folders(['Music', 'fun', 'parliament'])
