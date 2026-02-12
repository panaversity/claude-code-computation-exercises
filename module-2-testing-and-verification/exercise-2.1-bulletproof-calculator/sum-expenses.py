#!/usr/bin/env python3
"""Sum expenses from a CSV file.

Reads CSV with columns: date, description, amount
Outputs transaction count and total.

Usage:
    python sum-expenses.py < data.csv
"""
import sys
import csv

total = 0.0
count = 0

reader = csv.reader(sys.stdin)
header = next(reader)

for row in reader:
    try:
        amount = float(row[2])
        total += amount
        count += 1
    except (ValueError, IndexError):
        pass  # skip bad rows

print(f"Processed {count} transactions")
print(f"Total: ${total:,.2f}")
