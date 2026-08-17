cities = {
    'beijing': {
        'country': 'zhongguo', 
        'renkou': 14, 
        'shishi': 'good',
        },
    
    'huashengdun':{
        'country': 'meiguo', 
        'renkou': 2, 
        'shishi': 'yiban'
        },
    'lundun': {'country': 'yingguo', 'renkou': 1.4, 'shishi': 'haixing'},
    }
for city, xinxi in cities.items():
    print(f"\nCity:{city.title()}")
    print(f"xinxi:{xinxi}")
    