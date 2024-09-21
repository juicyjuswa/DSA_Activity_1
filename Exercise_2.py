# Subject: Data Structure and Algorithm
# Lab Activity: Python review 
# Student: Braganza, Joshua S.
# Course and Section: BS CpE 2-3
# Deadline: September 22, 2024 11:59pm


# Exercise 2: Ohm’s Law Calculator
# Instructions:
# 1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
# 2.	Based on their choice, prompt the user to input the appropriate values.
# 3.	Use Ohm's Law to calculate the missing variable and display the result.
# 4.	Handle cases where division by zero might occur.

def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    if resistance == 0:
        return print("Resistance cannot be zero when calculating current.")
    return voltage / resistance

def calculate_resistance(voltage, current):
    if current == 0:
        return print("Current cannot be zero when calculating resistance.")
    return voltage / current

while True:
    print("\nWhat do you want to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    print("4. Exit")
    
    input_choice = input("\nEnter your choice (1, 2, 3, or 4): ")

    if input_choice == "1":
        current = float(input("\nEnter the current (I) in amperes: "))
        resistance = float(input("Enter the resistance (R) in ohms: "))
        voltage = calculate_voltage(current, resistance)
        print(f"\nThe calculated voltage is {voltage:.2f} volts.")

    elif input_choice == "2":
        voltage = float(input("\nEnter the voltage (V) in volts: "))
        resistance = float(input("Enter the resistance (R) in ohms: "))
        current = calculate_current(voltage, resistance)
        if isinstance(current, str):  
            print(current)
        else:
            print(f"\nThe calculated voltage is {current:.2f} amperes.")

    elif input_choice == "3":
        voltage = float(input("\nEnter the voltage (V) in volts: "))
        current = float(input("Enter the current (I) in amperes: "))
        resistance = calculate_resistance(voltage, current)
        if isinstance(resistance, str):  
            print(resistance)
        else:
            print(f"\nThe calculated voltage is {resistance:.2f} ohms.")
    
    elif input_choice == "4":
        print("\nExiting program. Babush")
        break

    else:
        print("\nInvalid Choice, Please Select 1, 2, 3 or 4")