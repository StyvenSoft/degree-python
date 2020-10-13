toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizza = len(toppings)

print("We sell " + str(num_pizza) + " different kings of pizza!")

pizzas = list(zip(toppings, prices))

pizzas.sort()


cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(three_cheapest)

num_two_dolar_slices = prices.count(2)

print(num_two_dolar_slices)