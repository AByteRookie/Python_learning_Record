my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for my_food in my_foods:
    print(f"{my_food.title()} are my favorite foods!")

for friend_food in friend_foods:
    print(f"My friend favorite foods are {friend_food}!")