import pandas as pd
import matplotlib.pyplot as plt
df_weather = pd.read_csv("weather-data.csv")
df_squirel = pd.read_csv("Squirrel-Data.csv")

x_cordinate = df_squirel["X"].to_list()

#print(x_cordinate)

df_weather_dict = df_weather.to_dict()

'''waar = weather[weather["temp"] > 14]
print(waar)'''

'''weather.plot()
plt.show()'''

#creatimg dataframe
data_dict = {
    "name" : ['awa','roger','pablo'],
    "age" : [12,34,45]
}

data = pd.DataFrame(data_dict)
print(data)

data.to_csv("new_file.csv")