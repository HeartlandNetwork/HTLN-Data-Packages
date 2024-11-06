
###############################################################
#
#   data_package_version.py
#   correcting lat/long dd for HOME and HOCU
#   in invasive_plants data package
#
#   Gareth Rowell - 20240927
#
###############################################################




import pandas as pd
import matplotlib.pyplot as plt

# load data

df = pd.read_csv("HTLN_InvasivePlants_Monitoring.csv")

df.dtypes


# count rows for HOSP and HOME

df_hosp = df[df['ParkCode'] == "HOSP"]
print(df_hosp)

df_home = df[df['ParkCode'] == "HOME"]
print(df_home)

df_home.hist(column='LatitudeInDecimalDegrees')
plt.xlabel('LatitudeInDecimalDegrees')
plt.ylabel('Frequency')
plt.title('Homestead Latitude')
#plt.show()

# Delete rows where latitude is < 38
df_home = df_home[df_home['LatitudeInDecimalDegrees'] > 38]

df_home.hist(column='LatitudeInDecimalDegrees')
plt.xlabel('LatitudeInDecimalDegrees')
plt.ylabel('Frequency')
plt.title('Homestead Latitude')
plt.show()


#remove HOME from df then append df_home



df = df[(df['ParkCode'] != "HOME")]

df = pd.concat([df, df_home], ignore_index=True)

# write to file

df.to_csv('HTLN_InvasivePlants_Monitoring_no_HOSP.csv', encoding='utf-8', index=False)



