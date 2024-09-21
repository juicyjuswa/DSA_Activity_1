# Subject: Data Structure and Algorithm
# Lab Activity: Python review 
# Student: Braganza, Joshua S.
# Course and Section: BS CpE 2-3
# Deadline: September 22, 2024 11:59pm


# Exercise 1: Temperature Converter
# Create a program that converts temperatures between Celsius and Fahrenheit.
# Instructions:
# 1.	Ask the user to input a temperature.
# 2.	Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
# 3.	Perform the appropriate conversion and print the result.

while True:
    print("\nSelect Conversion Type:")
    print("1.) Celsius to Fahrenheit")
    print("2.) Fahrenheit to Celsius")
    print("3.) Exit the Program")

    input_choice = input("\nEnter your Choice (1, 2 or 3): ")

    if input_choice == "1":
        user_input = float(input("\nInput Temperature: "))
        celsius =(user_input * (9/5)) + 32
        print(f"\n{user_input}°C is equal to {celsius:.2f}°F")

    elif input_choice == "2":
        user_input = float(input("\nInput Temperature: "))
        fahrenheit = (user_input - 32) * 5/9
        print(f"\n{user_input}°F is equal to {fahrenheit:.2f}°C")

    elif input_choice == "3":
        print("\nExiting Program, Babush")
        break

    else:
        print("\nInvalid Choice, Please Select 1, 2 or 3")