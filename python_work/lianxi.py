jiabinnames = ['Jiabaoyu', 'Lindaiyu', 'Sunwukong']
jiabinnames.insert(0,'Likui')
jiabinnames.insert(2,'Bailongma')
jiabinnames.append('Zhubajie')
zhengshirenyuan = f"{jiabinnames}"
print(len(jiabinnames))
print(f"Now we have more guests to join the party,{zhengshirenyuan.title()}!")
print(f"Unfortunately,only two guests {jiabinnames[0].title()} and {jiabinnames[1].title()} can be invited to the party.")
baoqian1 = f"{jiabinnames.pop()}"
print(f"Sorry,{baoqian1.title()}!We can't invite you to the party.")
baoqian2 = f"{jiabinnames.pop()}"
print(f"Sorry,{baoqian2.title()}!We can't invite you to the party.")
baoqian3 = f"{jiabinnames.pop()}"
print(f"Sorry,{baoqian3.title()}!We can't invite you to the party.")
baoqian4 = f"{jiabinnames.pop()}"
print(f"Sorry,{baoqian4.title()}!We can't invite you to the party.")
print(f"{jiabinnames[0].title()} and {jiabinnames[1].title()},you are still invited to the party!")
del jiabinnames[0]
print(jiabinnames)
del jiabinnames[0]
print(jiabinnames)