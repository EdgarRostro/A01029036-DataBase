import pandas as pd
filepath = "./TextFiles/populationbycountry19802010millions.csv"
with open(filepath,'r') as fp:
    data = fp.read().split('\n')
    
data = [f.split(',') for f in data]
print (data[0][0])git 