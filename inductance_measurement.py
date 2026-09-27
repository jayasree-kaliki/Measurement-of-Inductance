# inductance_measurement.py
# Program to calculate inductance of a coil
# using voltage, current, and frequency

import math

print("=== Inductance Measurement ===")

# Input values
voltage = float(input("Enter RMS voltage (V): "))
current = float(input("Enter RMS current (A): "))
frequency = float(input("Enter frequency (Hz): "))

# Calculate inductive reactance
xl = voltage / current

# Calculate inductance
inductance = xl / (2 * math.pi * frequency)

# Display results
print("\n--- Inductance Measurement Results ---")
print(f"Voltage           = {voltage:.2f} V")
print(f"Current           = {current:.2f} A")
print(f"Frequency         = {frequency:.2f} Hz")
print(f"Inductive Reactance = {xl:.2f} Ohm")
print(f"Inductance        = {inductance:.6f} H")
print(f"Inductance        = {inductance * 1000:.3f} mH")
