# cost_of_gum = 0.10
# cost_of_gumdrop = 0.35

# cost_of_transaction = cost_of_gum + cost_of_gumdrop
# # Returns 0.44999999999999996

from decimal import Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# 0.8899999999999999023003738329862244427204132080078125
# 0.344500000000000028421709430404007434844970703125