import csv

data = []
with open("../inventory-list.csv", 'r') as file:
    for line in file:
        temp = []
        for i in line.split(','):
            temp.append(i)
        data.append(temp)

for i in range(len(data)):
    data[i] = [x.replace('\n', '') for x in data[i]]

data = data[1:]

counts = {}

plant_count = {}

for i in data:
    if i[4] in plant_count:
        if i[3] in plant_count[i[4]]:
            if i[0] in plant_count[i[4]][i[3]]:
                plant_count[i[4]][i[3]][i[0]] += 1
            else:
                plant_count[i[4]][i[3]][i[0]] = 1
        else:
            plant_count[i[4]][i[3]] = {i[0]: 1}
    else:
        plant_count[i[4]] = {i[3]: {i[0]: 1}}

print(plant_count)

master = [["Plant", "Own/Rent", "Equipment", "Count"]]

for i in plant_count:
    for j in plant_count[i]:
        for k in plant_count[i][j]:
            temp1 = [i, j, k, plant_count[i][j][k]]
            master.append(temp1)

file = open("equip_count.csv", "w+", newline= '')
with file:
    write = csv.writer(file)
    write.writerows(master)
