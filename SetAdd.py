Country_list = []
amount = int(input(""))
for i in range(amount):
    country = input("")
    Country_list.append(country)
Organized_set = set(Country_list)
New_amount = len(Organized_set)
print(New_amount)