import csv
import pandas
import statistics

csvfile = open("myfile4.csv", "w",newline='')
print("File Created")
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['App used', 'Daily screentime', 'Weekly screentime']) 
print("Columns Created")