print("The deli has run out of pastrami!") # 打印告知顾客熟食店的五香烟熏牛肉卖完了

sandwich_orders = ['bigbig', 'small', 'medium', 'pastrami', 'pastrami', 'pastrami', 'gagic'] # 订单列表
while 'pastrami' in sandwich_orders: # 当订单列表中存在五香烟熏牛肉的时候
    sandwich_orders.remove('pastrami') # 从订单列表中去除五香烟熏牛肉的订单
    print(sandwich_orders) # 打印剩余的订单列表

finished_sandwiches = [] # 完成列表

while sandwich_orders: # 当订单列表不为空时循环
    current_sandwich = sandwich_orders.pop() # 从订单列表中去除最后一个订单并存储在current_sandwich中
    print(f"I made your {current_sandwich} sandwich.") # 打印制作完成的三明治
    finished_sandwiches.append(current_sandwich) # 将制作完成的三明治添加到完成列表中
    
print("\nThe following sandwiches have been made:") # 打印已经完成的三明治列表
for sandwich in finished_sandwiches: # 遍历完成列表中的每个三明治
    print(f"- {sandwich}") # 打印每个完成的三明治