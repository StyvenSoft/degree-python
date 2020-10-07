print((1 + 1 == 2) and (2 + 2 == 4)) #True
print((1 + 1 == 2) and (2 < 1)) #False
print((1 > 9) and (5 != 6)) #False
print((0 == 10) and (1 + 1 == 1) ) #False

statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"