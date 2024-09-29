# Global Conversion Factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function for user interaction
def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
        elif unit == 'F':
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
