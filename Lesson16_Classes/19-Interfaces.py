class Chess:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_chess_pieces()
 
  def play(self):
    print("Playing chess!")
 
class Checkers:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_checkers_pieces()
 
  def play(self):
    print("Playing checkers!")

#  defined an InsurancePolicy class

class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005