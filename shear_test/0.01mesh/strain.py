import math


with open("ld.dat", "r") as f:
    data = [line.strip().split() for line in f]


def calculate_value(row):
    x201, y201, x203, y203, x212, y212, x210, y210, x204, y204, x207, y207, x206, y206, x209, y209, z = row
    e1 = (float(y206) - float(y204))/0.114
    e2 = (float(x210) - float(x204))/0.114
    e3 = math.sqrt( (float(x212) - float(x204))**2 + (float(y212)-float(y204))**2)/0.161220
    f1 =  (float(y203) - float(y201))/0.114
    f2 =  (float(x207) - float(x201))/0.114
    f3 =  math.sqrt( (float(x209) - float(x201))**2 + (float(y209)-float(y201))**2)/0.161220

    return ((2.*f3 - f1 - f2)+(2. * e3 -e1 - e2))/2.


new_values = [calculate_value(row) for row in data]

def calculated_value(row):
    x201, y201, x203, y203, x212, y212, x210, y210, x204, y204, x207, y207, x206, y206, x209, y209, z = row
    return float(z)/0.0105
    
new_value =  [calculated_value(row) for row in data]


with open("strain.dat", "w") as f:
    for value in new_values:
        f.write(str(value) + "\n")
        
with open("output.dat", "w") as f:
    for value in new_value:
        f.write(str(value) + "\n")
