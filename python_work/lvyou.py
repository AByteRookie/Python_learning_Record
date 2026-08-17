responses = {} # 创建一个空字典来存储调查结果
response_active = True # 设置一个标志来控制循环的继续

while response_active: # 循环开始，直到用户选择结束循环
    name = input("\nWhat is your name? ") # 提示用户输入他们的名字
    response = input("If you could visit one place in the world, where would you go? ") # 提示用户输入想去的地方
    
    responses[name] = response # 将用户的名字他们的回答存储在字典中
    
    repeat = input("Would you like to let another person respond? (yes/no) ") # 提示用户是否继续调查
    if repeat == 'no': # 如果用户选择’no‘，则结束循环
        response_active = False # 结束循环
        
print("\n---Results---") # 打印结果
for name, response in responses.items():# 遍历字典中的键值对
    print(f"{name} would like to visit {response}.") # 打印每个人的名字和他们想去的地方