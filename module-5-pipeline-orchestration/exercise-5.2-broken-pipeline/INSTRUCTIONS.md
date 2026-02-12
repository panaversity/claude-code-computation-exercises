# Exercise 5.2 -- The Broken Pipeline

**Debug** -- Find two interface bugs in a 3-step data pipeline

## Goal

A 3-step pipeline (clean, categorize, report) processes `input-data.csv` (100 transactions) and produces `wrong-report.txt`. Each script looks reasonable when you read it in isolation. The bugs are in how the steps connect: step 1 outputs amounts in an inconsistent format, and step 2 silently drops rows it cannot parse.

## What You Have

- `input-data.csv` -- 100 source transactions (clean, plain numeric amounts)
- `step1-clean.py` -- Step 1: Cleans data but formats amounts with "$" prefix and inconsistent negative sign placement
- `step2-categorize.py` -- Step 2: Categorizes transactions but uses `lstrip("$")` which fails on some formats, silently dropping rows
- `step3-report.py` -- Step 3: Generates summary report from whatever rows it receives
- `wrong-report.txt` -- The incorrect final report (produced by running the pipeline)

The intended pipeline is:
```bash
python step1-clean.py < input-data.csv | python step2-categorize.py | python step3-report.py
```

## Your Tasks

### Step 1: Run the Pipeline and Compare

Run the full pipeline and compare against `wrong-report.txt`:
```bash
python step1-clean.py < input-data.csv | python step2-categorize.py | python step3-report.py
```

Note the total transaction count. It should be 100, but it is not.

### Step 2: Check Intermediate Outputs

Debug by checking row counts between steps:
```bash
python step1-clean.py < input-data.csv | wc -l
python step1-clean.py < input-data.csv | python step2-categorize.py | wc -l
```

Where do rows disappear?

### Step 3: Find Bug 1 -- Format Mismatch

Examine step1-clean.py output. Look at how negative amounts are formatted. Are all negative amounts formatted the same way? What two formats does step 1 use?

Then look at step2-categorize.py. How does it strip the "$" from amounts? Does that method work for BOTH negative formats?

### Step 4: Find Bug 2 -- Silent Data Loss

Step 2 has a `try/except` that catches `ValueError` and `continue`s (skips the row). This means unparseable rows disappear silently. How many rows are lost? What is the financial impact?

### Step 5: Fix Both Bugs

Fix the format mismatch (use `replace("$", "")` instead of `lstrip("$")`, or fix step 1 to use consistent formatting). Fix the silent data loss (log skipped rows, or better yet, fix the parsing so no rows are skipped).

Verify that all 100 rows flow through the entire pipeline.

## Expected Results

- Identification of both bugs with specific file and line references
- A fixed pipeline that processes all 100 transactions
- Correct final report showing all categories and correct totals
- An explanation of why checking row counts between pipeline steps catches these bugs

## Reflection

1. Step 1 and Step 3 each work correctly for their own assumed input format. Why did the pipeline still fail?
2. How many dollars of transactions were lost due to the silent skip in step 2? How would a real business discover this error?
3. What is the simplest change you could make to step 2 that would have made the bug immediately obvious (instead of silent)?
