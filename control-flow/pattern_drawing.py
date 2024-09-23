# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the pattern using a while loop
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after finishing a row
    row += 1
