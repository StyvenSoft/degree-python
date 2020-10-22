raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}


raffle.pop(320291, "No Prize")
# "Gift Basket"
raffle
# {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
raffle.pop(100000, "No Prize")
# "No Prize"
raffle
# {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
raffle.pop(872921, "No Prize")
# "Concert Tickets"
raffle
# {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

## Example

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

# {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25}
# 65