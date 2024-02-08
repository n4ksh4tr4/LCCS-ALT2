import csv
import pandas as pd
import statistics

# csvfile = open("myfile.csv", "x")

csv_file = 'socialmedia.csv'
open(csv_file,"r+")

print("File opened")

csvwriter = csv.writer(csv_file)
csvwriter.writerow(['Name', 'Do you use social media?', 'Most used app', 'Daily Avg', 'Weekly Avg'])
print("Columns Created")


csvwriter.writerow(['Erin', 'Yes', 'Tiktok', '109m', '205m'])
csvwriter.writerow(['Nakshatra', 'Yes', 'Tiktok', '105m', '430m'])
csvwriter.writerow(['Maheen', 'Yes', 'Tiktok', '131m', '155m'])
csvwriter.writerow(['Bihone', 'Yes', 'Whatsapp', '64m', '240m'])
csvwriter.writerow(['Kashmala', 'Yes', 'Snapchat', '90m', '300m'])
csvwriter.writerow(['Rebecca', 'Yes', 'Tiktok', '69m', '147m'])
csvwriter.writerow(['Areeba', 'Yes', 'Tiktok', '90m', '270m'])
csvwriter.writerow(['Aishah', 'Yes', 'Instagram', '60m', '172m'])
csvwriter.writerow(['Kieva', 'Yes', 'Whatsapp', '60m', '185m'])
csvwriter.writerow(['Sinead', 'Yes', 'Youtube', '240m', '260m'])
csvwriter.writerow(['Tracy', 'Yes', 'Instagram', '123m', '495m'])
csvwriter.writerow(['Shannon', 'Yes', 'Snapchat', '120m', '420m'])
csvwriter.writerow(['Emma', 'Yes', 'Snapchat', '120m', '300m'])
csvwriter.writerow(['Sabha', 'Yes', 'Tiktok', '158m', '451m'])
csvwriter.writerow(['Emma Ivory', 'Yes', 'Tiktok', '158m', '638m'])
print("Data Created")

data= [109, 105, 155, 240, 300, 147, 270, 172, 185, 260, 495, 420, 300, 451, 638]
mean_value = sum(data) / len(data)
df = pd.DataFrame({'Mean': [mean_value]})
mean = mean_value
print(df)

data = ["Tiktok", "Whatsapp", "Instagram", "Snapchat","Snapchat","Snapchat","Tiktok", "Tiktok","Tiktok","Tiktok","Tiktok", "Tiktok","Instagram","Instagram", "Youtube"]
mode_value = statistics.mode(data)
print('Mode:')
print(mode_value)

numbers=([205, 430, 155, 240, 300, 147, 270, 172, 185, 260, 495, 420, 300, 451, 638])
median_value= statistics.median(numbers)
print("Median Value:", median_value)

numbers =[109, 105, 131, 64, 90, 69, 90, 60, 60, 240, 123, 120, 120, 120, 158, 158]
print("max value:")
print(max(numbers))
print("min value:")
print(min(numbers))

csvfile.close()
print("closed")