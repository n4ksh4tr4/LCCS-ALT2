import statistics
import pandas

#Read the entire CSV File into a pandas DataFrame
df= pandas.read_csv('yesyestest.csv')

#Filter out the column, years,time,age
years_worked=df['years']
print(years_worked)

hours_worked=df['time']
print(hours_worked)

ages_working=df['age']
print(ages_working)



