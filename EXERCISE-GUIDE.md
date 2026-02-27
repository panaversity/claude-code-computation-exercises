# Computation & Data Extraction -- Practice Exercises

## Build Verified Data Processing Tools That Handle Real-World Messiness

**By Panaversity -- Build Tools, Not Answers**

---

## How This Guide Works

Every module in this guide follows the same two-exercise pattern. Exercise X.1 is a **Build** exercise: you create a working utility from real data, starting from scratch or from a provided dataset. Exercise X.2 is a **Debug** exercise: you receive a broken script that runs without crashing but produces wrong results, and your job is to find the specific bugs hiding in plain sight. This pattern mirrors real-world data work, where half the job is building tools and the other half is figuring out why existing tools are quietly giving you wrong answers.

The exercises develop three core skills that compound across modules. First, **building composable stdin/stdout tools** -- Python scripts that read from standard input and write to standard output, so they can be piped together like Unix utilities. Second, **zero-trust verification with test data** -- the discipline of never trusting a script's output until you have compared it against independently computed correct answers. Third, **processing real-world CSV data with proper parsing** -- handling the quoted fields, mixed formats, missing values, and encoding issues that break naive text splitting.

All exercises require **Claude Code** as your working environment. You will write Python scripts, run them in the terminal, pipe data between them, and use Claude Code to help you debug when things go wrong. The exercises are designed so that Claude Code is your development partner -- you direct the work, Claude Code helps you implement it, and together you verify that the results are correct. Python 3.x with standard library modules (`csv`, `decimal`, `sys`, `re`) is all you need. No external packages are required.

---

## Data Processing Framework

Every exercise follows these seven steps. As you work through the modules, this framework becomes second nature.

### Step 1: Understand the Data

Before writing any code, examine the data files. What format are they in? CSV, plain text, something else? What do the columns represent? What edge cases might exist -- quoted fields, missing values, mixed date formats, currency symbols embedded in numbers? Most importantly: what does a "correct" result look like? If you cannot describe the expected output before writing code, you are not ready to write code.

### Step 2: Build the Tool

Write a Python script that reads from stdin and writes to stdout. This is the Unix philosophy applied to data processing: each tool does one thing well, and tools compose through pipes. Your script should handle the specific data format you identified in Step 1, including its edge cases.

### Step 3: Create Test Data

Before running your tool on the full dataset, create a small test file (5-10 rows) where you can compute the correct answer by hand. This is your ground truth. If your tool cannot produce the correct answer on 5 rows, it will not produce the correct answer on 500 rows.

### Step 4: Verify

Run your tool on the test data. Compare the output against your hand-computed answer. If they match, you have evidence (not proof) that your tool works. If they do not match, you have a bug to find before proceeding.

### Step 5: Handle Edge Cases

Now run on the full dataset. Check for: quoted fields with commas inside them, empty fields, numbers with currency symbols or thousand separators, mixed date formats, rows with extra or missing columns, Unicode characters, and BOM markers at the start of files.

### Step 6: Pipeline

For multi-step processing, connect your tools with pipes. The output of one tool becomes the input of the next. Verify at each stage -- check intermediate outputs to catch problems before they cascade through the pipeline.

### Step 7: Make Permanent

Once your tool works and is verified, save the script somewhere useful. Add a usage comment at the top. Consider creating a shell alias for common invocations. A tool that works once and is lost is not a tool -- it is a demo.

---

## Assessment Rubric

Use this rubric to evaluate your work on each exercise. Each criterion is scored from 1 (Beginner) to 4 (Advanced).

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|-------------|----------------|----------------|--------------|
| **Decimal Handling** | Uses Bash arithmetic or naive integer math | Uses Python floats but rounds poorly or inconsistently | Correct float handling with rounding at output | Uses `Decimal` module for financial precision throughout |
| **Verification** | Does not test; trusts first output | Tests with one simple case | Tests with known answers plus edge cases | Comprehensive test suite with automated comparison scripts |
| **CSV Processing** | Splits on commas naively (string split) | Handles basic CSV with `csv` module | Handles quoted fields, mixed formats, edge cases | Handles encoding, BOM, mixed line endings, malformed rows |
| **Pattern Matching** | Hardcoded string checks (`if "DELTA" in name`) | Basic regex without anchoring | Regex with word boundaries (`\b`) and case handling | False positive guards, categorization hierarchy, adversarial testing |
| **Pipeline Design** | Single monolithic script does everything | Separate scripts but manual copy-paste between steps | Piped pipeline with verification at each stage | Automated pipeline with error handling, row counting, and data validation at each step |

---

## Module 1: Arithmetic & Stdin Tools

**Lessons Covered**: 1-2
**Core Skill**: Building composable Python utilities that handle decimal math correctly

The foundational problem: Bash cannot do decimal arithmetic, and floating-point math accumulates errors over hundreds of operations. These exercises teach you to build Python tools that handle money correctly and plug into Unix-style pipelines.

---

### Exercise 1.1 -- The Expense Splitter (Build)

**Time**: 20-35 minutes

**The Problem**: You have 5 dinner receipt files from team outings. Each file lists line items with prices, a subtotal, tax, and tip. You need a reusable utility that reads a receipt and calculates the per-person split. Bash arithmetic cannot handle the decimals ($167.05 / 4 people). Build a Python tool that can.

**What You Will Learn**:
1. Why stdin/stdout composability matters for reusable tools -- a script that reads from stdin can process any receipt file via pipe or redirect
2. How to handle decimal arithmetic without cent-rounding errors -- the difference between `float` division and correct financial rounding
3. The pattern for building Unix-style utilities -- read stdin, process, write stdout, exit with appropriate code

**Files Provided**:
- `dinner-receipts/receipt-1-italian.txt` through `receipt-5-large-party.txt` -- Five receipts with varying numbers of attendees, items, and edge cases (odd splits, discounts, large parties)

**The Challenge**: Your tool should work on ANY receipt file with this format, not just these five. After building it, you should be able to pipe any similarly-formatted receipt through it and get a correct per-person split.

---

### Exercise 1.2 -- The Rounding Trap (Debug)

**Time**: 20-35 minutes

**The Problem**: `buggy-sum.py` processes `transactions-large.csv` (520 transactions) and reports a total. The script runs without errors. It produces a number. But that number is off by several dollars from the known correct answer in `expected-total.txt`. The script does not crash -- it quietly produces the wrong result by skipping transactions it considers "trivial."

**What You Will Learn**:
1. How filtering conditions can silently exclude valid data -- a reasonable-looking filter can drop real transactions
2. Why the transaction count is as important as the total -- if the count is wrong, the total is wrong
3. The difference between "runs successfully" and "produces correct results" -- exit code 0 means "did not crash," not "correct"

**Files Provided**:
- `transactions-large.csv` -- 500+ realistic bank transactions
- `buggy-sum.py` -- A script that sums all amounts but loses precision
- `expected-total.txt` -- The mathematically correct total

**The Challenge**: Find the bug, fix it, and verify your fix produces the exact expected total. Then explain WHY the original script produces a different number than the correct answer.

---

## Module 2: Testing & Verification

**Lessons Covered**: 3
**Core Skill**: Zero-trust verification -- proving correctness with test data before trusting results

A script that exits with code 0 has told you exactly one thing: it did not crash. It has told you nothing about whether its output is correct. These exercises teach you to verify outputs against independently known answers, and to discover that "green" does not mean "right."

---

### Exercise 2.1 -- The Bulletproof Calculator (Build)

**Time**: 20-35 minutes

**The Problem**: You have a working script, `sum-expenses.py`. Your job is NOT to build a calculator -- it is to BREAK the one you have. Design a comprehensive test suite that covers: normal numbers, decimals, negatives, zero, empty lines, non-numeric data, extremely large numbers, single-item input, currency symbols mixed in, and rows with wrong column counts. Your test data files are the deliverable, not the script.

**What You Will Learn**:
1. Good tests anticipate edge cases the developer did not -- the script has a subtle weakness that your tests should reveal
2. A test suite is more valuable than the code it tests -- a good test suite can validate any replacement implementation
3. Exit code 0 means "did not crash," not "correct" -- the script silently skips bad rows without reporting them

**Files Provided**:
- `sum-expenses.py` -- A working expense summation script

**The Challenge**: Create at least 5 test CSV files, each targeting a different edge case category. For each test file, compute the expected output by hand FIRST, then run the script and compare. Document any discrepancies -- especially cases where the script "succeeds" but loses data.

---

### Exercise 2.2 -- The Green Light Lie (Debug)

**Time**: 25-40 minutes

**The Problem**: `broken-calc.py` processes `test-data.csv` and exits with code 0 every time. No errors. No warnings. But the totals are wrong. Three separate logic bugs produce incorrect results while the script looks perfectly fine on the surface. The correct answers are in `expected-results.txt`.

**What You Will Learn**:
1. How scripts can be "green" (exit 0) while silently producing wrong answers -- the most dangerous bugs are the ones that do not crash
2. The three most common silent calculation bugs: filtering errors (skipping valid data), counting errors (off-by-one), and masking errors (hiding the sign of a result)
3. Why comparing against known answers catches bugs that exit codes miss -- the only reliable test is comparing output to independently computed truth

**Files Provided**:
- `broken-calc.py` -- Script with 3 hidden logic bugs
- `test-data.csv` -- 20 rows of test data
- `expected-results.txt` -- The correct count and total

**The Challenge**: Find all three bugs. For each bug, explain: (1) what the bug is, (2) what incorrect behavior it causes, (3) how to fix it. Do not just make the numbers match -- understand WHY each bug produces the specific wrong answer it does.

---

## Module 3: CSV Processing

**Lessons Covered**: 4
**Core Skill**: Processing real-world CSV data that breaks naive parsing

The comma in "CSV" is a lie. Real CSV files contain commas inside quoted fields, currency symbols in numeric columns, mixed date formats, empty fields, and encoding issues. Splitting on commas is not parsing CSV. These exercises teach you the difference.

---

### Exercise 3.1 -- The Messy Payroll (Build)

**Time**: 30-45 minutes

**The Problem**: `payroll-data.csv` has 80+ employee records. Company names contain commas ("Acme, Inc."), salaries have currency symbols and thousand separators ($85,000.00), dates come in two different formats (01/15/2023 and 2023-03-22), some bonus fields are empty, and names have apostrophes ("O'Brien"). Build a processor that correctly parses all of this and extracts the total payroll cost (salary + bonus for all active employees).

**What You Will Learn**:
1. Python's `csv` module handles what `awk` and `cut` cannot -- quoted fields with embedded commas are parsed correctly
2. Real-world data is never clean -- your code must handle every variation present in the file
3. Data cleaning is a prerequisite to data processing -- you must strip currency symbols and parse dates before you can compute anything

**Files Provided**:
- `payroll-data.csv` -- 80+ employee records with the edge cases described above

**The Challenge**: Build a script that reads the payroll CSV and outputs: total number of active employees, total salary for active employees, total bonus for active employees, and combined total payroll cost. Handle all the messiness -- do not skip rows because they are hard to parse.

---

### Exercise 3.2 -- The Awk Disaster (Debug)

**Time**: 25-40 minutes

**The Problem**: Someone processed `bank-export.csv` (200 rows) with `process-with-awk.sh`, a simple awk script that extracts transaction amounts. The output in `broken-awk-output.txt` has approximately 40 rows with wrong amounts. The awk script split on commas, which broke whenever a field was quoted and contained commas. Your job: identify exactly which rows are wrong, explain why each one failed, and build a correct replacement.

**What You Will Learn**:
1. Why awk fails on real CSV -- `awk -F','` splits on ALL commas, including those inside quoted fields
2. How to compare two outputs systematically to find discrepancies -- diff, paste, or scripted comparison
3. When to reach for Python's `csv` module versus simple text tools -- any time your data might contain quoted fields

**Files Provided**:
- `bank-export.csv` -- 200 bank transactions, ~40 with quoted fields
- `process-with-awk.sh` -- The broken awk script
- `broken-awk-output.txt` -- The incorrect output from the awk script

**The Challenge**: Write a Python script that correctly extracts all 200 amounts. Compare its output against the awk output line-by-line to identify exactly which rows differ and why. Count the discrepancies.

---

## Module 4: Categorization & Patterns

**Lessons Covered**: 5
**Core Skill**: Building categorizers with regex precision and false-positive guards

String matching sounds simple until "DR PEPPER" gets categorized as a medical expense and "SUBWAY RESTAURANT" gets filed under transit. These exercises teach you to build categorizers that are precise enough for real data, with explicit guards against the false positives that naive matching produces.

---

### Exercise 4.1 -- The Expense Report Builder (Build)

**Time**: 30-45 minutes

**The Problem**: `corporate-expenses.csv` has 150+ corporate card transactions. Categorize every transaction into one of five categories: Travel (airlines, hotels, rental cars, rideshares), Meals (restaurants, coffee shops, fast food), Software (subscriptions, SaaS, licenses), Office Supplies (paper, equipment, repairs), and Uncategorized (everything else). But watch for tricky merchants: "DELTA FAUCETS" is a plumbing company, not Delta Airlines. "JAVA CITY COFFEE" is a coffee shop, not a software tool. "SUBWAY RESTAURANT" serves sandwiches, not transit rides.

**What You Will Learn**:
1. How to build category-pattern dictionaries with regex -- structured mapping from patterns to categories
2. Why false positive guards must check BEFORE category matching -- exclude known false positives first, then apply patterns
3. How word boundaries (`\b`) prevent partial matches -- "APPLE" should not match "APPLEBEES"

**Files Provided**:
- `corporate-expenses.csv` -- 150+ corporate card transactions with realistic merchants

**The Challenge**: Build a categorizer that correctly handles every transaction, including the false-positive traps. Output a summary showing: count and total per category, plus a list of any transactions you could not confidently categorize. Your Uncategorized list should be small and should NOT contain obvious miscategorizations.

---

### Exercise 4.2 -- The Over-Eager Matcher (Debug)

**Time**: 30-45 minutes

**The Problem**: `buggy-categorizer.py` processes `transactions.csv` and produces categorized output, but it has exactly 8 false positives. Each one is a different regex/matching mistake:
1. "DR PEPPER SNAPPLE GROUP" categorized as Medical (matches "DR")
2. "RED LOBSTER" categorized as Charitable (matches "RED" from "RED CROSS" pattern)
3. "SUBWAY RESTAURANT" categorized as Transit (matches "SUBWAY")
4. "TARGET" categorized as a specialty store instead of general retail
5. "SHELL GAS STATION" categorized as Tech/Computing (matches "SHELL")
6. "APPLEBEES" categorized as Electronics (matches "APPLE" from Apple Store pattern)
7. "AMAZON FRESH" double-counted in both Grocery and Shopping
8. "BEST BUY" matches anything containing "BEST" in the description

Fix all 8 without breaking the legitimate matches those patterns are supposed to catch.

**What You Will Learn**:
1. The most common regex mistakes in categorization: no word boundaries, no false positive exclusion list, greedy substring matching
2. How to systematically audit a categorizer's output -- compare against manually categorized samples
3. Why testing with adversarial data matters more than testing with clean data -- clean data makes every categorizer look correct

**Files Provided**:
- `transactions.csv` -- 100+ transactions including the 8 tricky merchants
- `buggy-categorizer.py` -- Categorizer with all 8 false positive patterns

**The Challenge**: Fix each false positive. For every fix, document: (1) what the bug was, (2) which legitimate matches the pattern was supposed to catch, (3) how your fix preserves the legitimate matches while blocking the false positive.

---

## Module 5: Pipeline Orchestration

**Lessons Covered**: 4
**Core Skill**: Connecting verified tools into multi-step data pipelines

Individual tools are useful. Pipelines of connected tools are powerful. But pipelines introduce a new class of bugs: interface mismatches between steps, silent data loss in the middle, and cascading errors that make the final output wrong even when each step looks correct in isolation. These exercises teach you to build and debug multi-step pipelines.

---

### Exercise 5.1 -- The Quarterly Report (Build)

**Time**: 30-45 minutes

**The Problem**: Three monthly bank statement CSVs (January, February, March) need to be combined, cleaned, categorized, and summarized into a quarterly financial report. Build a 4-step pipeline:
1. **Combine**: Merge three CSV files into one, preserving a single header row
2. **Clean**: Normalize data (consistent date format, clean amount parsing)
3. **Categorize**: Assign each transaction to a category
4. **Summarize**: Generate a report with per-category totals and a grand total

**What You Will Learn**:
1. How to chain tools with pipes for multi-step processing -- each step is a separate script connected with `|`
2. Why verification at each pipeline step prevents cascading errors -- check row counts and intermediate totals
3. The head/tail technique for combining CSVs without duplicate headers -- `head -1 file1.csv; tail -n +2 file1.csv file2.csv file3.csv`

**Files Provided**:
- `monthly-statements/january.csv` -- ~60 transactions
- `monthly-statements/february.csv` -- ~60 transactions
- `monthly-statements/march.csv` -- ~60 transactions

**The Challenge**: Build each step as a standalone script. Verify each step independently with small test data before connecting them. Then run the full pipeline and verify the final report. Your report should include: transaction count, per-category totals, and a grand total that matches the sum of all three source files.

---

### Exercise 5.2 -- The Broken Pipeline (Debug)

**Time**: 30-45 minutes

**The Problem**: A 3-step pipeline (clean, categorize, report) processes `input-data.csv` and produces `wrong-report.txt`. Each script LOOKS correct when you read the code in isolation. The bugs are in how the steps connect:
- Step 1 outputs amounts with dollar-sign prefixes (`$-45.67`), but Step 2 expects plain numbers (`-45.67`)
- Step 2 silently drops any row it cannot parse (instead of erroring), so rows disappear without warning
- Step 3 sums whatever it receives, producing wrong totals because it is working with incomplete data

**What You Will Learn**:
1. Pipeline bugs often live in the INTERFACES between steps, not inside steps -- each script may be "correct" for its assumed input format
2. Silent data loss (dropped rows) is harder to catch than crashes -- a script that processes 80 of 100 rows still exits with code 0
3. How to debug a pipeline by checking intermediate outputs at each stage -- row counts, spot checks, and checksums between steps

**Files Provided**:
- `input-data.csv` -- 100 source transactions
- `step1-clean.py` -- Cleaning step (outputs `$` prefixed amounts)
- `step2-categorize.py` -- Categorizing step (expects plain numbers, silently drops unparseable rows)
- `step3-report.py` -- Reporting step (sums whatever it receives)
- `wrong-report.txt` -- The incorrect final report

**The Challenge**: Debug the pipeline by examining intermediate outputs between each step. Identify both bugs (format mismatch and silent data loss). Fix the pipeline so all 100 rows flow through all three steps and the final report is correct.

---

## Module 6: Capstone Projects

**Choose one (or more). Build a real tool you will actually use.**

These capstone exercises combine every skill from the previous modules into substantial projects. Each one produces a genuinely useful tool, not just a homework assignment. Budget 2-4 hours.

---

### Capstone A -- The Freelancer's Tax Prep

**Time**: 2-4 hours

**The Problem**: You have 6 months of bank statements (July through December). Build the complete data processing pipeline: combine all statements, parse every transaction, categorize into tax-relevant categories (Income, Medical, Business Expense, Charitable Donation, Education, Personal), handle ambiguous entries with a review queue, and generate an accountant-ready report with category subtotals and quarterly summaries.

**What You Will Learn**:
1. How all chapter skills combine into a real workflow -- decimal math, verification, CSV parsing, categorization, and pipelines all in one project
2. Verification-first orchestration -- build test data first, verify each pipeline step, then process the full dataset
3. Building something genuinely useful -- a tool that could actually save hours during tax season

**Files Provided**:
- `bank-statements/july.csv` through `bank-statements/december.csv` -- Six months of realistic freelancer transactions including client payments, medical expenses, business tools, charitable donations, and education costs

**The Challenge**: Produce a final report that an accountant could use. It should include: total income, total deductible expenses by category, net income, and a list of ambiguous transactions that need human review. Verify your pipeline against a subset of hand-categorized transactions before running the full dataset.

---

### Capstone B -- The Subscription Auditor

**Time**: 2-4 hours

**The Problem**: One year of bank transactions (800+ rows, January through December). Build a tool that identifies recurring subscription charges, calculates the annual cost of each subscription, detects price changes mid-year, flags cancelled and new subscriptions, identifies potential duplicates, and generates an audit report showing total subscription spend versus one-time purchases.

**What You Will Learn**:
1. Pattern detection across time -- a subscription is the same merchant charging a similar amount on a monthly cycle
2. Anomaly detection -- price changes, new subscriptions starting, old ones stopping
3. Building analytical tools, not just processing tools -- you are detecting patterns, not just summing numbers

**Files Provided**:
- `annual-transactions.csv` -- 800+ transactions across 12 months, including subscriptions at various frequencies (monthly, annual), price changes, cancelled services, new services, and ambiguous near-duplicates

**The Challenge**: Produce an audit report showing: each detected subscription with its monthly cost, annual total, and any price changes. Flag subscriptions that appear to be duplicates. Show total annual subscription spend. List subscriptions that started or stopped during the year.

---

### Capstone C -- Your Own Financial Data

**Time**: 2-4 hours

**The Problem**: Export your own bank statement CSVs. Build a custom pipeline for YOUR categories and merchants. Your bank's CSV format will be different from the exercise files. Your merchants will be specific to your life. Your categories will reflect your actual financial priorities.

**What You Will Learn**:
1. Real data has edge cases that exercises cannot simulate -- your bank's CSV format, your merchants' exact naming conventions, your specific transaction patterns
2. Custom categories reflect YOUR life, not generic templates -- "Dog Expenses" or "Side Project Hosting" might be real categories for you
3. The tool you build is genuinely useful beyond this course -- this is not a homework assignment, it is a personal finance utility

**Files Provided**:
- None -- you bring your own data

**The Challenge**: Build a complete pipeline that processes your actual bank statements. Document your category definitions. Create test data from known transactions to verify your categorizer. Process at least 3 months of data and produce a summary report. The tool should be rerunnable -- next month, you should be able to drop in a new CSV and get an updated report.

---

## How to Self-Assess

After completing each exercise, evaluate yourself against the rubric. Be honest -- the goal is not to score 4 on everything immediately. The goal is to know where you are and what to practice next.

| Score | Meaning |
|-------|---------|
| **16-20** | Advanced -- you are building production-quality data tools |
| **12-15** | Proficient -- solid foundation, edge case handling needs refinement |
| **8-11** | Developing -- core concepts understood, practice with messier data needed |
| **5-7** | Beginner -- review the chapter material and redo Module 1-2 exercises |

After completing all modules, you should be able to take any CSV file, build a verified processing pipeline, and produce correct results -- even when the data is messy, the formats are inconsistent, and the edge cases are plentiful.

**Build tools, not answers. Verify everything. Trust nothing.**
