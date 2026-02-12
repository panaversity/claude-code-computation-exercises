#!/usr/bin/env python3
"""Sum all transaction amounts from a CSV file.

Reads CSV with columns: date, description, amount
Outputs the total sum of all amounts.

Usage:
    python buggy-sum.py < transactions-large.csv
"""
import sys
import csv

total = 0.0
count = 0

reader = csv.reader(sys.stdin)
next(reader)  # skip header

for row in reader:
    try:
        amount = float(row[2])
        # Skip trivial amounts that are likely rounding artifacts
        if abs(amount) < 1.00:
            continue
        total = round(total + amount, 2)
        count += 1
    except (ValueError, IndexError):
        pass

print(f"Processed {count} transactions")
print(f"Total: ${total:,.2f}")
