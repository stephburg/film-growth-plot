import matplotlib.pyplot as plt
import numpy as np

# Define the time range and the growth rate
time = np.linspace(0, 10, 100)  # Time from 0 to 10 units
growth_rate = 5  # Film thickness growth rate in nm/unit time

# Calculate the film thickness
film_thickness = growth_rate * time

# Plot the diagram
plt.figure(figsize=(8, 6))
plt.plot(time, film_thickness, label='Linear Growth', color='blue')
plt.xlabel('Time (units)')
plt.ylabel('Film Thickness (nm)')
plt.title('Linear Growth of Film Thickness Over Time')
plt.legend()
plt.grid(True)
plt.show()