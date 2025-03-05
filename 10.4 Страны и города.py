country: dict = {}
for _ in range(int(input())):
    list_city = input().split()
    country[list_city[0]] = list_city[1:]
for _ in range(int(input())):
    city:str = input()
    for key in country.keys():
        if city in country[key]:
            print(key)