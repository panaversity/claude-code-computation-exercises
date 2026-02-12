# Exercise 2.1 -- The Bulletproof Calculator

**Build** -- Design a test suite that exposes the weaknesses of a working script

## Goal

You have a working expense summation script (`sum-expenses.py`). Your job is NOT to build a calculator -- it is to BREAK the one you have. Design a comprehensive test suite of CSV files that test every edge case you can think of. The script has a subtle weakness that your tests should reveal.

## What You Have

- `sum-expenses.py` -- A working script that reads a CSV from stdin and sums the amount column

## Your Tasks

### Step 1: Read the Script

Read `sum-expenses.py` and understand what it does. Pay attention to how it handles errors.

### Step 2: Design Test Cases

Create at least 5 test CSV files, each targeting a different edge case category:

1. **Normal data** -- Standard transactions with typical amounts (your baseline)
2. **Decimal edge cases** -- Amounts like 0.10, 0.01, -0.001, 99.999
3. **Non-numeric data** -- Rows with "N/A", empty strings, text in the amount column
4. **Structural edge cases** -- Empty file, header only, single row, rows with wrong column count
5. **Extreme values** -- Very large numbers (999999999.99), very small (0.001), mixed positive/negative

### Step 3: Compute Expected Answers

For EACH test file, calculate the expected output BY HAND before running the script. Write down: expected transaction count and expected total.

### Step 4: Run and Compare

Run the script on each test file. Compare against your hand-computed answers. Document any discrepancies.

### Step 5: Find the Weakness

The script has a design flaw: it silently skips rows it cannot parse. Your tests should reveal this. How many rows does it silently discard? Does it tell you about them?

## Expected Results

- At least 5 test CSV files in a `tests/` directory you create
- A document (or comments) showing expected vs. actual output for each test
- Identification of the script's silent-skip weakness
- An explanation of why this weakness matters in real data processing

## Reflection

1. Which edge case was hardest to think of? Which one surprised you when you ran it?
2. The script exits with code 0 even when it skips rows. Is that acceptable behavior? Why or why not?
3. How would you modify the script to make silent skips impossible?
