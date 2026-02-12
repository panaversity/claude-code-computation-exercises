#!/usr/bin/env python3
"""Calculate total from transaction CSV.

Reads CSV with columns: date, description, amount
Outputs transaction count and total.

Usage:
    python broken-calc.py < test-data.csv
"""
import sys
import csv

total = 0.0
count = 0

# Read from stdin
reader = csv.reader(sys.stdin)
header = next(reader)

for row in reader:
    count += 1
    try:
        amount = float(row[2])
        if amount > 0:
            total += amount
    except (ValueError, IndexError):
        continue

# Account for the header row in the count
count = count + 1

print(f"Processed {count} transactions")
print(f"Total: ${abs(total):,.2f}")
sys.exit(0)
