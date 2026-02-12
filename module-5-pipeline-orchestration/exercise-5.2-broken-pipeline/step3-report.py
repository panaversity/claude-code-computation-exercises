#!/usr/bin/env python3
"""Step 3: Generate summary report from categorized transactions.

Reads categorized CSV from stdin, produces a summary report on stdout.
Expects columns: date, description, amount, category

Usage:
    ... | python step3-report.py
"""
import sys
import csv
from collections import defaultdict

reader = csv.reader(sys.stdin)
header = next(reader)

totals = defaultdict(float)
counts = defaultdict(int)

for row in reader:
    try:
        amount = float(row[2])
        category = row[3]
        totals[category] += amount
        counts[category] += 1
    except (ValueError, IndexError):
        continue

print("QUARTERLY FINANCIAL REPORT")
print("=" * 50)
print()
print(f"Total transactions processed: {sum(counts.values())}")
print()
print(f"{'Category':<20} {'Count':>6} {'Total':>12}")
print("-" * 40)

for cat in sorted(totals.keys()):
    print(f"{cat:<20} {counts[cat]:>6} ${totals[cat]:>10,.2f}")

print("-" * 40)
grand = sum(totals.values())
total_count = sum(counts.values())
print(f"{'TOTAL':<20} {total_count:>6} ${grand:>10,.2f}")
