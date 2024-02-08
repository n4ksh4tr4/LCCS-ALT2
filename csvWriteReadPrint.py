import csv
import pandas
import statistics 

csvfile = open("myfile3.csv", "w", newline = '')
print("File created")
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Noise', 'Temp'])
print("Columns Created")
csvwriter.writerow([25, 10])
csvwriter.writerow([24, 12])
csvwriter.writerow([12, 9])
csvwriter.writerow([33, 77])
csvfile.close() 
print("Data Created")
print("closed after created rows")

csvfile = open("myfile3.csv","r")
line = csvfile.readline()
print(line, "readline1")
line = csvfile.readline()
print(line, "readline2")
line = csvfile.readline()
print(line, "readline3")
line = csvfile.readline()
print(line, "readline4")
line = csvfile.readline()
print(line, "readline5")
line = csvfile.readline()
csvfile.close()
print("closed after printing rows")

csvfile = open('myfile3.csv',"a")
print("closed append")                             