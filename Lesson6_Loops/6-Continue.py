big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
  if i < 0:
    continue
  print(i)

# 1
# 2
# 4
# 5
# 2

## Example

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for i in ages:
  if i < 21:
    continue
  print(i)

# 38
# 34
# 26
# 21
# 67
# 41