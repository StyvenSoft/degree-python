print(True or (3 + 4 == 7)) #True
print((1 - 1 == 0) or False) #True
print((2 < 0) or True) #True
print((3 == 8) or (3 > 4)) #False 


statement_one = True

statement_two = True

def graduation_mailer(gpa, credits):
  if (gpa >= 2.0) or (credits >= 120):
    return True