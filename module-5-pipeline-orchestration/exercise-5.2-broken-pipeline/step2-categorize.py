#!/usr/bin/env python3
"""Step 2: Categorize transactions.

Reads cleaned CSV from stdin, assigns categories, outputs categorized CSV.
Expects columns: date, description, amount

Usage:
    python step1-clean.py < input-data.csv | python step2-categorize.py
"""
import sys
import csv

CATEGORIES = {
    "Income": ["DEPOSIT", "PAYMENT", "TRANSFER", "PAYROLL"],
    "Dining": ["STARBUCKS", "CHIPOTLE", "PANERA", "UBER EATS", "MCDONALDS",
               "BURGER KING", "DOMINOS", "CHICK-FIL-A"],
    "Grocery": ["WHOLE FOODS", "KROGER", "TRADER JOE", "SAFEWAY", "ALDI", "PUBLIX"],
    "Utility": ["ELECTRIC", "WATER UTIL", "GAS COMPANY", "COMCAST", "ATT WIRELESS"],
    "Shopping": ["AMAZON", "TARGET", "WALMART", "HOME DEPOT", "BEST BUY", "COSTCO"],
    "Transportation": ["SHELL", "CHEVRON", "GAS STATION", "UBER TECH", "LYFT"],
    "Subscription": ["NETFLIX", "SPOTIFY", "HULU", "DISNEY"],
    "Health": ["CVS", "WALGREENS", "PHARMACY"],
}

def categorize(description):
    desc_upper = description.upper()
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in desc_upper:
                return category
    return "Other"

reader = csv.reader(sys.stdin)
header = next(reader)

writer = csv.writer(sys.stdout)
writer.writerow(["date", "description", "amount", "category"])

for row in reader:
    date = row[0]
    description = row[1]
    amount_str = row[2]

    # Parse amount -- strip leading "$" if present
    cleaned = amount_str.lstrip("$").strip()

    try:
        amount = float(cleaned)
    except ValueError:
        continue

    category = categorize(description)
    writer.writerow([date, description, f"{amount:.2f}", category])
