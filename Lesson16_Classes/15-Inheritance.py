class User:
  is_admin = False
  def __init__(self, username)
    self.username = username
 
class Admin(User):
  is_admin = True

class Bin:
  pass

class RecyclingBin(Bin):
  pass