# Exercise 4.1 -- The Expense Report Builder

**Build** -- Categorize 156 corporate expenses with regex precision and false-positive guards

## Goal

Build a categorization script that assigns each transaction in `corporate-expenses.csv` to one of five categories: Travel, Meals, Software, Office Supplies, or Uncategorized. The data includes merchants designed to trick naive pattern matchers -- "DELTA FAUCETS" is a plumbing company (Office Supplies), not Delta Airlines (Travel). Your categorizer must handle these correctly.

## What You Have

- `corporate-expenses.csv` -- 156 corporate card transactions with columns: date, merchant, amount, card_holder, description

### Category Definitions

| Category | Includes | Example Merchants |
|----------|----------|-------------------|
| Travel | Airlines, hotels, rental cars, rideshares | DELTA AIR LINES, HILTON HOTELS, HERTZ, UBER |
| Meals | Restaurants, coffee shops, fast food | CHIPOTLE, STARBUCKS, PANERA, OLIVE GARDEN |
| Software | SaaS subscriptions, licenses, cloud services | JETBRAINS, GITHUB, SLACK, ZOOM, AWS |
| Office Supplies | Paper, equipment, repairs, shipping | STAPLES, OFFICE DEPOT, HP INC, ULINE |
| Uncategorized | Everything that does not clearly fit | Review manually |

### Known False-Positive Traps

These merchants LOOK like they belong in one category but actually belong in another:
- **DELTA FAUCETS** -- Plumbing company, NOT Delta Airlines. Category: Office Supplies
- **JAVA CITY COFFEE** -- Coffee shop, NOT a Java/software tool. Category: Meals
- **SUBWAY RESTAURANT** -- Sandwich shop, NOT subway transit. Category: Meals
- **SHELL OIL CO** -- Gas station, NOT Shell scripting/tech. Category: Travel (fuel for trips)
- **APPLEBEES** -- Restaurant, NOT Apple Store. Category: Meals
- **DR PEPPER SNAPPLE GROUP** -- Beverage company, NOT a medical office. Category: Meals

## Your Tasks

### Step 1: Design Category Patterns

Create a dictionary mapping category names to lists of regex patterns. Use word boundaries (`\b`) to prevent partial matches.

### Step 2: Build False-Positive Guards

Before matching patterns, check against a list of known false positives. For example, if you see "DELTA" in a merchant name, first check if it is "DELTA FAUCETS" before categorizing as Travel.

### Step 3: Build the Categorizer

Write a script that:
- Reads the CSV
- Applies false-positive guards first
- Then applies category patterns
- Assigns "Uncategorized" to anything that does not match
- Outputs a categorized report

### Step 4: Verify with Spot Checks

Manually verify at least 10 transactions, including all the known false-positive traps. Ensure DELTA FAUCETS is NOT in Travel, JAVA CITY COFFEE is NOT in Software, etc.

### Step 5: Generate Summary Report

Output:
- Count and total amount per category
- List of all Uncategorized transactions (for manual review)
- The Uncategorized list should be small and should NOT contain obvious miscategorizations

## Expected Results

- A working `categorize-expenses.py` script
- Category summary with counts and totals
- All false-positive traps handled correctly
- Small Uncategorized list (merchants that genuinely do not fit)

## Reflection

1. Why must false-positive guards run BEFORE category pattern matching?
2. What is the difference between `"DELTA" in merchant` and `re.search(r"\bDELTA AIR\b", merchant)`?
3. If a new false positive appeared next month (e.g., "AMAZON PHARMACY" getting categorized as Shopping), how would you add it to your system?
