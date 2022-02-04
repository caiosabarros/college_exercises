import math

print(f'Welcome to the velocity calculator. Please enter the following:\n')

m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input(f'Drag constant (0.5 for sphere, 1.1 for cylinder): '))

velocity_at_t = math.sqrt(m * g / ( (1 / 2) * p * A * C) ) * (1 - math.exp((-1) * math.sqrt(m * g * (1 / 2) * p * A * C) * t / m))

print(f'\nThe inner value of c is: {(1 / 2) * p * A * C:.3f}')
print(f'The velocity after 10.0 seconds is: {velocity_at_t:.3f} m/s')