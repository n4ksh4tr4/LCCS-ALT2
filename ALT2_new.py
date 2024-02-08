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
print('mean of daily hours:',mean_hrs_value)

df = pandas.read_csv('socialmedia.csv')
weeklyhr = df['Weeklyhr']
median_value = statistics.median(weeklyhr)
print('median of weekly hours:',median_value)

#Calculate mode of used social media application
df = pandas.read_csv('socialmedia.csv')
MainApp = df['Main_app']
mode_value = statistics.mode('MainApp')
print('mode of main app used:',mode_value)


numbers =[109, 105, 131, 64, 90, 69, 90, 60, 60, 240, 123, 120, 120, 120, 158, 158]
print("max value of daily hours:",max(numbers))
print("min value of daily hours:",min(numbers))


x = ['Erin', 'Nakshatra', 'Maheen', 'Bihone', 'Kashmala', 'Rebecca', 'Areeba', 'Aishah', 'Kieva', 'Sinead', 'Tracy', 'Shannon', 'Emma', 'Sabha', 'Emma Ivory']
y = [109, 105, 155, 240, 300, 147, 270, 172, 185, 260, 495, 420, 300, 451, 638]
'''
plt.bar(x, y)
plt.xlabel('Students')
plt.ylabel('Minutes')
plt.title('Social Media Usage of Students')

plt.show()
'''
