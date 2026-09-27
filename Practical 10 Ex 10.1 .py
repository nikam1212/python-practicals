prices = [100.5, 250.75, 50.25, 500.0, 300.5]

prices.sort(reverse=True)

print("Top 3 highest prices:")
for price in prices[:3]:
    print(price)
