import csv

with open('data2.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)

#  не понял нужно ли было записывать в файл если файл прикладываете )

# x = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London'],
#         ['sw2', 'Cisco', '3850', 'Liverpool'],
#         ['sw3', 'Cisco', '3650', 'Liverpool'],
#         ['sw4', 'Cisco', '3650', 'London']]
#
# with open("data2.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#
#     for row in x:
#         writer.writerow(row)
