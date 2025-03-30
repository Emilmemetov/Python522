
file = "test2.txt"
f = open(file, "w")
f.write("Замена строки в текстовом файле;\n"
        "изменить строку в списке;\n"
        "записать список в файл;\n")
f.close()

f = open(file)
read_lines = f.readlines()
f.close()

pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))

if 0 <= pos1 < len(read_lines) and 0 <= pos2 < len(read_lines):
    read_lines[pos1], read_lines[pos2] = read_lines[pos2], read_lines[pos1]
else:
    print("Такого нет!")

f = open(file, "w")
f.writelines(read_lines)
f.close()


