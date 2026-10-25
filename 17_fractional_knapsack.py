# Input each parcel as: weight profit
n = int(input("Number of parcels: "))
items = []
for i in range(n):
    weight, profit = map(float, input(f"Parcel {i + 1} weight and profit: ").split())
    if weight <= 0:
        print("Weight must be positive.")
        raise SystemExit
    items.append((weight, profit, profit / weight))

capacity = float(input("Truck capacity: "))
items.sort(key=lambda x: x[2], reverse=True)
total_profit = 0.0
chosen = []

for weight, profit, ratio in items:
    if capacity <= 0:
        break
    take = min(weight, capacity)
    fraction = take / weight
    total_profit += profit * fraction
    capacity -= take
    chosen.append((weight, take, profit * fraction))

print("Selected parcels (original weight, weight loaded, profit gained):")
for original, loaded, gained in chosen:
    print(f"{original:g}, {loaded:g}, {gained:.2f}")
print(f"Maximum profit: {total_profit:.2f}")
