
import csv

# csvfile = open("myfile.csv", "x")

filename = 'socialmedia.csv'
csvfile = open(filename,"r+")

print("File opened")

csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Name', 'Do you use social media?', 'Most used app', 'Daily Avg', 'Weekly Avg'])
print("Columns Created")


csvwriter.writerow(['Erin', 'Yes', 'Tiktok', '1 hr 49m', '3hrs 25m'])
csvwriter.writerow(['Nakshatra', 'Yes', 'Tiktok', '1 hr 45m', '7hrs 10m'])
csvwriter.writerow(['Maheen', 'Yes', 'Tiktok', '2 hrs 11m', '2hrs 35m'])
csvwriter.writerow(['Bihone', 'Yes', 'Whatsapp', '1 hr 4m', '4hrs'])
csvwriter.writerow(['Kashmala', 'Yes', 'Snapchat', '1 hr 30m', '5hrs'])
print("Data Created")

csvfile.close()
print("closed")