pizzas = ['big', 'small', 'mid', 'gagic']

friend_pizzas = pizzas[:]
friend_pizzas.append('mm')
pizzas.append('ml')

for pizza in pizzas:
    print(f"My favorite pizzas are:{pizza.title()}!")
for friend_pizza in friend_pizzas:
    print(f"My friend favorite pizzas are:{friend_pizza.title()}!")