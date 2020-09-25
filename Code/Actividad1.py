import csv

with open("TextFiles/populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
         print(row[-1])

    #reader = csv.DictReader(csvFile)

    #print(reader.fieldnames)