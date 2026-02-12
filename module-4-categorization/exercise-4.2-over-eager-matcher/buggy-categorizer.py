#!/usr/bin/env python3
"""Categorize transactions from a CSV file.

Reads CSV with columns: date, merchant, amount
Outputs categorized transactions with category totals.

Usage:
    python buggy-categorizer.py < transactions.csv
"""
import sys
import csv
import re

# Category patterns
categories = {
    "Medical": [
        r"DR\s",
        r"PHARMACY",
        r"MEDICAL",
        r"HEALTH",
        r"HOSPITAL",
    ],
    "Charitable": [
        r"RED",
        r"UNITED WAY",
        r"DONATION",
        r"CHARITY",
    ],
    "Transit": [
        r"SUBWAY",
        r"MTA",
        r"UBER",
        r"LYFT",
        r"METRO",
    ],
    "Electronics": [
        r"APPLE",
        r"SAMSUNG",
        r"SONY",
    ],
    "Tech": [
        r"SHELL",
        r"GITHUB",
        r"DIGITAL",
    ],
    "Grocery": [
        r"WHOLE FOODS",
        r"TRADER JOE",
        r"KROGER",
        r"SAFEWAY",
        r"ALDI",
        r"FRESH",
    ],
    "Shopping": [
        r"AMAZON",
        r"WALMART",
        r"NORDSTROM",
        r"TJMAXX",
        r"TARGET",
    ],
    "Food": [
        r"CHIPOTLE",
        r"OLIVE GARDEN",
        r"PANERA",
        r"STARBUCKS",
        r"MCDONALDS",
        r"BURGER KING",
        r"CHICK-FIL-A",
        r"BEST",
    ],
    "Utility": [
        r"ELECTRIC",
        r"WATER UTIL",
        r"GAS COMPANY",
        r"COMCAST",
    ],
}

reader = csv.reader(sys.stdin)
header = next(reader)

categorized = {}
totals = {}
counts = {}

for row in reader:
    date, merchant, amount_str = row[0], row[1], row[2]
    amount = float(amount_str)

    assigned = []
    for category, patterns in categories.items():
        for pattern in patterns:
            if re.search(pattern, merchant, re.IGNORECASE):
                assigned.append(category)
                break

    if not assigned:
        assigned = ["Uncategorized"]

    for cat in assigned:
        totals[cat] = totals.get(cat, 0.0) + amount
        counts[cat] = counts.get(cat, 0) + 1

# Print summary
print("=" * 50)
print("TRANSACTION CATEGORY SUMMARY")
print("=" * 50)
for cat in sorted(totals.keys()):
    print(f"  {cat:20s}: {counts[cat]:4d} transactions  ${totals[cat]:>10,.2f}")
print("=" * 50)
print(f"  {'TOTAL':20s}: {sum(counts.values()):4d} transactions  ${sum(totals.values()):>10,.2f}")
