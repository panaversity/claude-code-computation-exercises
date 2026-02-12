# Exercise 5.1 -- The Quarterly Report

**Build** -- Construct a 4-step data pipeline to produce a quarterly financial summary

## Goal

Three monthly bank statement CSVs (January, February, March) need to be combined, cleaned, categorized, and summarized into a quarterly financial report. Build each step as a separate script, then connect them with pipes. Verify at each stage.

## What You Have

- `monthly-statements/january.csv` -- 60 transactions
- `monthly-statements/february.csv` -- 60 transactions
- `monthly-statements/march.csv` -- 60 transactions

Each CSV has columns: date, description, amount, category (category column is empty -- you will fill it).

## Your Tasks

### Step 1: Combine (combine.py)

Write a script that merges all three CSVs into one stream, keeping only ONE header row. The output should have 180 data rows plus one header.

Technique: Print header from the first file. For each file, skip the header and print all data rows.

### Step 2: Clean (clean.py)

Write a script that reads combined CSV from stdin and normalizes the data:
- Ensure consistent date format
- Strip whitespace from descriptions
- Verify amounts are valid numbers
- Pass through all rows, flagging any that have issues

### Step 3: Categorize (categorize.py)

Write a script that reads cleaned CSV from stdin and fills in the category column. Use the same categorization skills from Module 4. Categories: Income, Groceries, Dining, Utilities, Shopping, Transportation, Subscriptions, Other.

### Step 4: Summarize (summarize.py)

Write a script that reads categorized CSV from stdin and produces a quarterly report:
- Transaction count per category
- Total amount per category
- Grand totals (income, expenses, net)
- Monthly breakdown

### Step 5: Connect the Pipeline

Run the full pipeline:
```bash
python combine.py | python clean.py | python categorize.py | python summarize.py
```

### Step 6: Verify Each Stage

Check intermediate outputs between steps:
```bash
python combine.py | wc -l                    # Should be 181 (180 data + 1 header)
python combine.py | python clean.py | wc -l  # Should also be 181
```

If row counts change between stages, you have a bug.

## Expected Results

- Four standalone scripts that each work independently
- A working pipeline that produces a quarterly financial report
- Correct row counts at each stage (no silent data loss)
- Category totals that sum to the correct grand total

## Reflection

1. What happens if you rearrange the pipeline steps? Which steps depend on which?
2. How did you handle the header row when combining files? What would go wrong if you did not?
3. What is the advantage of separate scripts versus one monolithic script that does everything?
