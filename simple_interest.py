# simple_interest.py
# Program to calculate Simple Interest using command-line arguments

import sys

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("=== Simple Interest Calculator ===")

if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

try:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])

    interest = calculate_simple_interest(principal, rate, time)

    print("\n--- Results ---")
    print(f"Principal amount: {principal}")
    print(f"Rate of interest: {rate}")
    print(f"Time (in years): {time}")
    print(f"Simple Interest = {interest}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
