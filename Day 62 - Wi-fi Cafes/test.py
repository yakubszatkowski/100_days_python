import csv

with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)

print(list_of_rows)

# some_list = []
# something = 'qwerty'
# something2 = 'okas'
#
# some_list.extend([something, something2])
# print(some_list)