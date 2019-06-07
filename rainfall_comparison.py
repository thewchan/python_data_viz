import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename_d = 'data/death_valley_2018_simple.csv'
with open(filename_d) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_death_valley, prcp_death_valley = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            prcp_d = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_death_valley.append(current_date)
            prcp_death_valley.append(prcp_d)

filename_s = 'data/sitka_weather_2018_simple.csv'
with open(filename_s) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_sitka, prcp_sitka = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            prcp_s = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_sitka.append(current_date)
            prcp_sitka.append(prcp_s)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_sitka, prcp_sitka, c='red', alpha=0.5, label='Sitka')
ax.plot(
    dates_death_valley, prcp_death_valley, c='blue', alpha=0.5,
    label='Death Valley',
    )

# Format plot.
plt.title(
    "Daily Precipitation - 2018\nSitka, AK vs. Death Valley, CA",
    fontsize=20
    )
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Inch", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
ax.legend()

plt.savefig('rainfall_comparison.png', bbox_inches='tight')
plt.show()
