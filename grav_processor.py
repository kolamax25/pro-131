import csv
import pandas as pd

rows = []

with open("final_data.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]

df = pd.read_csv("final_data.csv")
solar_mass_list = df["Mass"].tolist()
solar_radius_list = df["Radius"].tolist()

solar_mass_list.pop(0)
solar_radius_list.pop(0)

star_masses = []
star_radiuses = []
star_names = []
for data in star_data:
  star_masses.append(data[3])
  star_radiuses.append(data[4])
  star_names.append(data[1])

print((star_radiuses))

star_gravities = []

for index,data in enumerate(star_names):
    gravity = (float(star_masses[index])*5.972e+24) / (float(star_radiuses[index])*float(star_radiuses[index])*6371000*6371000) * 6.674e-11
    star_gravities.append(gravity)

df.to_csv("star_with_gravity.csv")