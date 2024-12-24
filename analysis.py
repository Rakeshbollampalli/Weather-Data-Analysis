# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the weather dataset
data = pd.read_csv('weather_data.csv')  # Make sure the file is in the same directory as this script

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Print dataset overview
print(data.head())
print(data.info())

# Plot temperature trends over time
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Temperature'], label='Temperature', color='orange')
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid()
plt.show()

# Plot rainfall trends over time
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Rainfall'], label='Rainfall', color='blue')
plt.title('Rainfall Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.grid()
plt.show()

# Moving average for temperature
data['Temperature_MA'] = data['Temperature'].rolling(window=7).mean()

# Moving average for rainfall
data['Rainfall_MA'] = data['Rainfall'].rolling(window=7).mean()

# Plot moving averages
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Temperature_MA'], label='7-Day Avg Temperature', color='red')
plt.plot(data['Date'], data['Rainfall_MA'], label='7-Day Avg Rainfall', color='green')
plt.title('7-Day Moving Averages for Temperature and Rainfall')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.grid()
plt.show()
