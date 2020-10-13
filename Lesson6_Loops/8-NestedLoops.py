project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for team in project_teams:
  for student in team:
    print(student)

# Ava
# Samantha
# James
# Lucille
# Zed
# Edgar
# Gabriel


## Example

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
    
print(scoops_sold)

# [12, 17, 22]
# [2, 10, 3]
# [5, 12, 13]
# 96