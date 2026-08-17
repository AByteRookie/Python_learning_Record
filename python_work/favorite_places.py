favorite_places= {
    'lihua': ['beijing' ,'shanghai' ,'tianjin'],
    'liudehua': ['xianggang', 'beijing', 'wuhan'],
    'zhaowu': ['zhangjiakou' ,'tianjin' ,'shenyang']
    }
for name, places in favorite_places.items():
    for place in places:
        print(f"{name.title()} says {place.title()} is very good!")