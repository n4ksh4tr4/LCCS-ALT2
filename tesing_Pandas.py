# Event: Phase 3 NW3 (Jan. 2022)
# Author: PDST 
# Using pandas - recommended for larger files
import statistics
import pandas

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('socialmedia.csv')

# Filter out the column, value_eur
daily_hrs = df['Dailyhrs']
mean_hrs_value = round(statistics.mean(daily_hrs), 2)
print(daily_hrs, mean_hrs_value)
"""
# Compute and display the mean
mean_value = round(statistics.mean(player_values), 2)
print("Mean Value:", type(mean_value),mean_value)

# Compute and display the median
median_value = statistics.median(player_values)
print("Median Value:", median_value)

# Compute and display the min and max values
print("Min: €%f, Max: €%f" %(min(player_values),max(player_values)))

# Second smallest unique value
s1 = list(set(sorted(player_values)))
s2 = sorted(s1)
print("Min:", s2[1])
print("Max:", s2[len(s2)-1])
"""
import csv
import pandas 
import statistics
import matplotlib.pyplot as plt

# Open and Create the file 
csvfile = open("socialmedia.csv", "r")
print("File Created")

# Open the file read it and print the first 2 rows
csvfile = open("socialmedia.csv","r")
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
print(line, "readline6")
line = csvfile.readline()
print(line, "readline7")
line = csvfile.readline()
print(line, "readline8")
line = csvfile.readline()
print(line, "readline9")
line = csvfile.readline()
print(line, "readline10")
line = csvfile.readline()
print(line, "readline11")
line = csvfile.readline()
print(line, "readline12")
line = csvfile.readline()
print(line, "readline13")
line = csvfile.readline()
print(line, "readline14")
line = csvfile.readline()
print(line, "readline15")
print()

df = pandas.read_csv('socialmedia.csv')
# Filter out the column, value_eur
daily_hrs = df['Dailyhrs']
mean_hrs_value = round(statistics.mean(daily_hrs), 2)
print(mean_hrs_value)

df = pandas.read_csv('socialmedia.csv')
weeklyhr = df['Weeklyhr']
median_value = statistics.median(Weeklyhr)




print(median_value)



x = ['Erin', 'Nakshatra', 'Maheen', 'Bihone', 'Kashmala', 'Rebecca', 'Areeba', 'Aishah', 'Kieva', 'Sinead', 'Tracy', 'Shannon', 'Emma', 'Sabha', 'Emma Ivory']
y = [109, 105, 155, 240, 300, 147, 270, 172, 185, 260, 495, 420, 300, 451, 638]

plt.bar(x, y)
plt.xlabel('Students')
plt.ylabel('Minutes')
plt.title('Social Media Usage of Students')

plt.show()