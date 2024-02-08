import csv
import pandas as pd
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
csvfile.close()
print("closed after printing rows")
print()

df = pandas.read_csv('FIFA21-player-list.csv')
print("here")
df = pandas.read_csv('socialmedia.csv')


# Filter out the column, value_eur
daily_hours = df['Dailyhrs']

data= [109, 105, 155, 240, 300, 147, 270, 172, 185, 260, 495, 420, 300, 451, 638]
mean_value = sum(data) / len(data)
print("Mean value of daily hours:",mean_value)

data = ["Tiktok", "Whatsapp", "Instagram", "Snapchat","Snapchat","Snapchat","Tiktok", "Tiktok","Tiktok","Tiktok","Tiktok", "Tiktok","Instagram","Instagram", "Youtube"]
mode_value = statistics.mode(data)
print('Mode of most used social media app:',mode_value)

numbers=([205, 430, 155, 240, 300, 147, 270, 172, 185, 260, 495, 420, 300, 451, 638])
median_value= statistics.median(numbers)
print("Median Value of weekly hours:", median_value)

numbers =[109, 105, 131, 64, 90, 69, 90, 60, 60, 240, 123, 120, 120, 120, 158, 158]
print("max value of daily hours:",max(numbers))
print("min value of daily hours:",min(numbers))

x = ['Erin', 'Nakshatra', 'Maheen', 'Bihone', 'Kashmala', 'Rebecca', 'Areeba', 'Aishah', 'Kieva', 'Sinead', 'Tracy', 'Shannon', 'Emma', 'Sabha', 'Emma Ivory']
y = [109, 105, 155, 240, 300, 147, 270, 172, 185, 260, 495, 420, 300, 451, 638]

plt.bar(x, y)
plt.xlabel('Students')
plt.ylabel('Minutes')
plt.title('Social Media Usage of Students')

plt.show()


