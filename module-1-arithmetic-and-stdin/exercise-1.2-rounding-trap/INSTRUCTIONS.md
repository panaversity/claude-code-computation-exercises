# Exercise 1.2 -- The Rounding Trap

**Debug** -- Find the bug in a script that silently produces the wrong total

## Goal

`buggy-sum.py` processes `transactions-large.csv` (520 transactions) and reports a total. The script runs without errors, exits cleanly, and produces a plausible-looking number. But that number is $12.06 off from the known correct answer in `expected-total.txt`. The script does not crash -- it quietly loses money. Find the bug and fix it.

## What You Have

- `transactions-large.csv` -- 520 realistic bank transactions (deposits, expenses, small charges)
- `buggy-sum.py` -- A script that reads the CSV and sums amounts, but produces the wrong total
- `expected-total.txt` -- The mathematically correct total, computed with Python's Decimal module

## Your Tasks

### Step 1: Run the Buggy Script

```bash
python buggy-sum.py < transactions-large.csv
```

Compare the output against `expected-total.txt`. Note the exact difference.

### Step 2: Read the Code

Read `buggy-sum.py` carefully. The script is short. The bug is not a syntax error or a crash -- it is a logic error that silently produces incorrect results.

### Step 3: Find the Bug

Ask yourself:
- Does the script process ALL rows, or does it skip some?
- What does "processed N transactions" tell you compared to the known row count?
- Are there any conditions that filter out valid data?

### Step 4: Fix the Bug

Modify the script (or write a new one) that produces the exact total from `expected-total.txt`. Verify your fix handles all 520 transactions.

### Step 5: Verify Your Fix

Run your corrected script and confirm it matches `expected-total.txt` exactly. The totals must match to the cent.

## Expected Results

- Identification of the specific bug causing the $12.06 discrepancy
- A corrected script that produces the exact expected total
- An explanation of WHY the bug causes that specific dollar amount of error

## Reflection

1. The script exits with code 0 and prints a formatted dollar amount. What made you suspicious that it was wrong?
2. How many transactions did the buggy script actually skip? What was the total value of the skipped transactions?
3. If you did not have `expected-total.txt` to compare against, how would you detect this bug?
