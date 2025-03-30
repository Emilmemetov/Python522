a = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}
for name, regions in a.items():
    print(name)
    for region_1, value in regions.items():
        print(region_1, ":", value)

name = input("Введите имя:")
region = input("Введите регион:")
if name in a and region in a[name]:
    print("Продажи", name, "В регионе", region, ":", a[name][region])
else:
    print("Ввели неверные данные")
name_edit = input("Введите новое значение")
a[name][region] = name_edit
print("Обновленные продажи для:", name, a[name])

