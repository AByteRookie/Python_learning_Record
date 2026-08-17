prompt = "\nTell me some toppings you'd like to add to your pizza:"

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active =False
    else:
        print(message)
