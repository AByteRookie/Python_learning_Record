rivers = {'yangtze river': 'china',
          'nile':'Egypt',
          'amazon':'brazil',
          }
for key, value in rivers.items():   # 加上“.items()”
    print(f"The {key.title()} runs through {value.title()}.")
    print(key.title())
    print(value.title())