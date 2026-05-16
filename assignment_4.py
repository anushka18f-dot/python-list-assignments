#Assignment 4

prices = [250, 310, 1450, 1200, 180, 420]
total_price = sum(prices)
aver_price = total_price / len(prices)
highest = max(prices)
lowest = min(prices)

expensive_prices_list = []

for price in prices:
    if price > 1000:
        expensive_prices_list.append(price)

print(expensive_prices_list)
