file1 = open("global_dataset.csv", "a")
file2 = open("dataset3.csv", "r")

for line in file2:
   file1.write(line)

file1.close()
file2.close()
