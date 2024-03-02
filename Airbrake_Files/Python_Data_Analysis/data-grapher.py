import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

actual_apogee = 0; # replace with actual apogee of flight in m

# filename = '/home/gavin/Documents/Airbrake_Files/Flight_Data/Clean_Data/test2.csv'
filename = '/home/gavin/Documents/test_data.TXT'
# graph_filename = '/home/gavin/Documents/Airbrake_Files/Flight_Data/Graphs/test2.png'
graph_filename = '/home/gavin/Documents/test.png'

df = pd.read_csv(filename, names=['Time', 'Altitude', 'Velocity', 'isDeployed', 'isBurning', 'Projected Apogee'])

df.loc[df['Time'] <= 1.5, 'Projected Apogee'] = np.nan
df['Error'] = abs(actual_apogee - df['Projected Apogee'])
altitude_color = np.where(df['isDeployed'] == 1, 'green', 'red')

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Altitude'], color=altitude_color, label='Altitude')
plt.plot(df['Time'], df['Velocity'], label='Velocity')
plt.plot(df['Time'], df['Projected Apogee'], label='Projected Apogee')
plt.plot(df['Time'], df['Error'], label='Error', color='green')
plt.axhline(y=actual_apogee, color='r', linestyle='-', label='Actual Apogee')
plt.axhline(y=1500, color='r', linestyle='-', label='Motor Cutoff (1.5s)')

deploy_changes = df[df['isDeployed'].diff() != 0]
for time in deploy_changes['Time']:
    plt.axvline(x=time, color='k', linestyle='--', alpha=0.5)

plt.ylim(0, 400)
plt.xlim(0, 10)

plt.xlabel('Time (Seconds)')
plt.ylabel('Altitude (Meters)')
plt.title('Flight Data Graph')
plt.legend()

# Save the plot to a file
plt.savefig(graph_filename)

print(f"Graph saved as {graph_filename}")