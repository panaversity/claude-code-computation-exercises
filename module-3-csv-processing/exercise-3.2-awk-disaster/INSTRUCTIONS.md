# Exercise 3.2 -- The Awk Disaster

**Debug** -- Find why awk extracts wrong amounts from a bank CSV

## Goal

Someone processed `bank-export.csv` (200 transactions) with `process-with-awk.sh`, a simple awk script that extracts the amount column. The output in `broken-awk-output.txt` has 39 rows with wrong values. The awk script splits on commas, which breaks whenever a merchant name is quoted and contains commas. Identify exactly which rows are wrong, explain why, and build a correct replacement.

## What You Have

- `bank-export.csv` -- 200 bank transactions, some with quoted merchant names containing commas
- `process-with-awk.sh` -- The broken awk script: `awk -F',' '{print $3}'`
- `broken-awk-output.txt` -- The incorrect output from the awk script (200 lines, 39 wrong)

## Your Tasks

### Step 1: Understand the Bug

Look at `bank-export.csv`. Find a row where the merchant name contains a comma (e.g., "AMAZON.COM, INC."). Now manually trace what `awk -F','` does to that line. What does it think column 3 is?

### Step 2: Build a Correct Extractor

Write a Python script that uses `csv.reader` to correctly extract all 200 amounts from `bank-export.csv`.

### Step 3: Compare Outputs

Compare your correct output against `broken-awk-output.txt` line by line. For each discrepancy:
- Which row number is it?
- What did awk produce?
- What is the correct amount?
- What merchant name caused the problem?

### Step 4: Count the Damage

How many rows are wrong? What is the total dollar difference between the awk output and the correct output?

## Expected Results

- A correct Python extraction script
- A comparison report showing all 39 discrepancies
- An explanation of why `awk -F','` fails on quoted CSV fields
- The total dollar impact of the incorrect extraction

## Reflection

1. The awk script is just one line. It looks correct. Why is "looks correct" not the same as "is correct"?
2. When is awk appropriate for CSV processing? When should you reach for Python's csv module instead?
3. If you received `broken-awk-output.txt` without the original CSV, could you tell that 39 values were wrong? Why or why not?
