import math


with open("ld.dat", "r") as f:
    data = [line.strip().split() for line in f]


def calculate_value(row):
    x1, y1, z1 = row 
    return float(x1)-float(y1)


new_values = [calculate_value(row) for row in data]

def calculated_value(row):
    x1, y1, z1 = row 
    return -float(z1)/0.00785
    
new_value =  [calculated_value(row) for row in data]


with open("strain.dat", "w") as f:
    for value in new_values:
        f.write(str(value) + "\n")
        
with open("output.dat", "w") as f:
    for value in new_value:
        f.write(str(value) + "\n")
