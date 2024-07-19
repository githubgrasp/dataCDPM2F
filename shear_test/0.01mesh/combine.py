
with open("strain.dat", "r") as f1:
    file1_data = [line.strip().split() for line in f1]


with open("output.dat", "r") as f2:
    file2_data = [line.strip() for line in f2]


for i in range(len(file1_data)):
    file1_data[i].append(file2_data[i])


with open("0.01.dat", "w") as f:
    for row in file1_data:
        f.write("\t".join(row) + "\n")

