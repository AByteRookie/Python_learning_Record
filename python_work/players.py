players = ['charles', 'martina', 'michael', 'florence', 'eli', 'lihua']

n =len(players)
mid = n // 2
middle_three = players[mid-2 :mid+1]
print(middle_three)

print("The first three items in the list are: ")
print(players[0:3])
print("Three items from the middle of the list are:")
print(players[1:4])
print("The last three items in the list are:")
print(players[-3:])