import json
import matplotlib.pyplot as plt
import os

delay_datas = []
file = '/Users/tjfournier19/Documents/GitHub/TjFournier.github.io/AirlineDelays.json'
with open(file, encoding='ascii') as f:
    text = f.read()
    delay_datas += json.loads(text)

# Finds location (SEA) for every month and gives delay % of flights
accumilator_delay_percent = []
accumilator_time = []

for given_year in range(2010,2017,1):
    for delay_data in delay_datas:
        location = delay_data["Airport"]["Code"]
        month = delay_data["Time"]["Month"]
        year = delay_data["Time"]["Year"]
        if location == "SEA" and year == given_year and month == 1 or location == "SEA" and year == given_year and month == 11 or location == "SEA" and year == given_year and month == 12:
            accumilator_delay_percent.append(100*(delay_data["Statistics"]["Flights"]["Delayed"]/delay_data["Statistics"]["Flights"]["Total"]))
            accumilator_time.append(str(year)+'-'+str(month))


# Creates bar graph
x = accumilator_time
y = accumilator_delay_percent

fig, ax = plt.subplots()
plt.bar(x, y)
plt.title('% of Flights delayed During the Holiday Months in Seattle')
plt.xlabel('Year and Month')
plt.ylabel('Flight Delay %')
plt.xticks(rotation=30, ha='right')
plt.savefig('SEA_flight_delay.png')
plt.show()



# Find GDP of US through the years
gdps_US = []
file1 = '/Users/tjfournier19/Documents/GitHub/TjFournier.github.io/US_GDP.json'
with open(file1, encoding='ascii') as f:
    text1 = f.read()
    gdps_US += json.loads(text1)

y_US=[]
for dict in gdps_US[1]:
    y_US.append(dict['value'])

x_US=[]
for year_US in range(2020, 1959, -1):
    x_US.append(year_US)

#GDP of China through the years
gdps_CHN = []
file2 = '/Users/tjfournier19/Documents/GitHub/TjFournier.github.io/China_GDP.json'
with open(file2, encoding='ascii') as f:
    text2 = f.read()
    gdps_CHN += json.loads(text2)

y_china=[]
for dict in gdps_CHN[1]:
    y_china.append(dict['value'])

x_china=[]
for year_china in range(2020, 1959, -1):
    x_china.append(year_china)

# Creates line graph with two data points
plt.xlabel('Years')
plt.ylabel('Gross Domestic Product (units in ten trillions)')
plt.title('GDP of United States vs China Over Time')
plt.plot(x_US, y_US, label = 'US\'s GDP')
plt.plot(x_china, y_china, label = 'China\'s GDP')
plt.legend()
plt.savefig('China_US_gdp_comparison.png')
plt.show() 