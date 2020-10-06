#¿Cuáles fueron los 5 países más productores de gases de invernadero en 2010?
#¿Cuáles fueron los 5 países más poblados en 2010? 
#¿Tienen alguna relación estos datos?
filepath_1 = "./TextFiles/greenhouse_gas_inventory_data_data.csv"
filepath_2 = "./TextFiles/populationbycountry19802010millions.csv"

with open(filepath_1,'r') as fp1:
    data1 = fp1.read().split('\n')

data1 = [f.split(',') for f in data1]
datos1_2010 = []


for i in range(len(data1)):
    if data1[i][1] == "2010":
        datos1_2010.append([data1[i][0], float(data1[i][2])])

print(datos1_2010)


with open(filepath_2,'r') as fp2:
    data2 = fp2.read().split('\n')
    
data2 = [f.split(',') for f in data2]

mayor2 = 0
indice = 0
paises_pob = []
for i in range(5):
    for j in range(len(data2)-1):
        if data2[j][-1] != "2010" and data2[j][-1] != "NA" and data2[j][-1] != "--" and (data2[j][0] not in paises_pob):
            if float(data2[j][-1]) > mayor2:
                mayor2 = float(data2[j][-1])
                indice = j
    paises_pob.append(data2[indice][0])

print (paises_pob)