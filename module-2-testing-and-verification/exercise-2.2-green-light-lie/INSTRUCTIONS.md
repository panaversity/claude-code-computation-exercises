# Exercise 2.2 -- The Green Light Lie

**Debug** -- Find three hidden logic bugs in a script that always exits successfully

## Goal

`broken-calc.py` processes `test-data.csv` and exits with code 0 every time. No errors. No warnings. No stack traces. But the reported transaction count and total are both wrong. Three separate logic bugs produce incorrect results while the script appears to work perfectly. The correct answers are in `expected-results.txt`.

## What You Have

- `broken-calc.py` -- Script with 3 hidden logic bugs (no syntax errors, no crashes)
- `test-data.csv` -- 20 rows of transaction data (positive and negative amounts)
- `expected-results.txt` -- The correct transaction count and total

## Your Tasks

### Step 1: Run and Compare

Run the script and compare its output against `expected-results.txt`:
```bash
python broken-calc.py < test-data.csv
```

Note both the count discrepancy and the total discrepancy.

### Step 2: Find Bug 1 -- The Filter

One of the three bugs causes the script to silently exclude valid transactions from the total. Which transactions are being excluded, and why?

### Step 3: Find Bug 2 -- The Count

The transaction count is wrong. The bug is in HOW the script counts rows. Look carefully at what it counts versus what it should count.

### Step 4: Find Bug 3 -- The Mask

Even after fixing the first two bugs, the total might still look "reasonable" because a third bug masks the sign of the result. What operation hides the true direction of the error?

### Step 5: Fix All Three

Fix each bug and verify that your corrected script produces the exact values from `expected-results.txt`.

## Expected Results

- Identification of all three bugs with specific line references
- For each bug: what it does wrong, what incorrect behavior it causes, and how to fix it
- A corrected script that matches `expected-results.txt` exactly

## Reflection

1. Bug 3 (`abs()`) makes the total always look positive. Why is this particularly dangerous in financial calculations?
2. If you only had the script's output (no `expected-results.txt`), which bug would be hardest to detect? Why?
3. The script exits with code 0 regardless of correctness. What should exit codes actually communicate?
