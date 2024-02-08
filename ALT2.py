import csv

# csvfile = open("myfile.csv", "x")

filename = 'socialmedia.csv'
csvfile = open(filename,"r+")

print("File opened")

csvwriter = csv.writer(csvfile)
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

csvfile.close()
print("closed")