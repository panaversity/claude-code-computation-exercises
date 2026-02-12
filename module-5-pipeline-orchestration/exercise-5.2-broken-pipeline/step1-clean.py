#!/usr/bin/env python3
"""Step 1: Clean and normalize transaction data.

Reads CSV from stdin, cleans descriptions, and formats amounts.
Outputs cleaned CSV to stdout.

Usage:
    python step1-clean.py < input-data.csv | python step2-categorize.py
"""
import sys
import csv
import random

reader = csv.reader(sys.stdin)
header = next(reader)

writer = csv.writer(sys.stdout)
writer.writerow(["date", "description", "amount"])

# Seed for consistent formatting decisions
random.seed(42)

for row in reader:
    date = row[0].strip()
    description = row[1].strip().upper()
    amount = float(row[2].strip())

    # Format amounts with dollar sign for readability
    if amount < 0:
        if random.random() < 0.4:
            formatted = f"-${abs(amount):.2f}"     # Accounting format
        else:
            formatted = f"${amount:.2f}"           # Standard format
    else:
        formatted = f"${amount:.2f}"

    writer.writerow([date, description, formatted])
