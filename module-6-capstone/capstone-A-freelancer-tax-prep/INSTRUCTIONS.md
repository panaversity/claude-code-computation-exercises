# Capstone A -- The Freelancer's Tax Prep

**Build** -- Create a complete tax-preparation pipeline from 6 months of bank data

## Goal

Build a complete data processing pipeline that takes 6 months of bank statements (July through December), combines them, categorizes every transaction into tax-relevant categories, handles ambiguous entries, and produces an accountant-ready report. This capstone combines every skill from the previous modules.

## What You Have

- `bank-statements/july.csv` through `bank-statements/december.csv` -- Six months of freelancer bank transactions (80 rows each, 480 total)

Each CSV has columns: date, description, amount, balance

### Transaction Categories for Tax Purposes

| Category | Tax Relevance | Example Merchants |
|----------|--------------|-------------------|
| Income | Taxable income | CLIENT PAYMENT, FREELANCE INVOICE, CONSULTING FEE |
| Medical | Deductible | DR SMITH, CVS PHARMACY, BLUE CROSS |
| Business Expense | Deductible | ZOOM, GITHUB, ADOBE, WEWORK, STAPLES |
| Charitable Donation | Deductible | RED CROSS, UNITED WAY, FOOD BANK |
| Education | Possibly deductible | UDEMY, COURSERA, CONFERENCE, OREILLY |
| Personal | Not deductible | STARBUCKS, NETFLIX, GROCERY, GAS |
| Ambiguous | Needs review | AMAZON (business or personal?), BEST BUY, HOME DEPOT |

## Your Tasks

### Step 1: Combine All Statements

Merge all 6 CSVs into one dataset with a single header row. Verify you have 480 data rows.

### Step 2: Build the Categorizer

Create a categorizer with:
- Pattern dictionaries for each tax category
- False-positive guards (lessons from Module 4)
- An "Ambiguous" category for transactions that could go either way

### Step 3: Create Test Data

Before processing the full dataset, create a small test file (10-15 transactions with known categories). Verify your categorizer handles them correctly.

### Step 4: Process and Verify

Run the full pipeline. Spot-check at least 20 transactions to verify correct categorization. Count how many end up Ambiguous.

### Step 5: Generate the Report

Produce a report suitable for an accountant:

```
FREELANCER TAX PREPARATION REPORT
July - December 2025
=====================================

INCOME
  Total Income: $XX,XXX.XX (N transactions)

DEDUCTIBLE EXPENSES
  Medical:     $X,XXX.XX (N transactions)
  Business:    $X,XXX.XX (N transactions)
  Charitable:  $X,XXX.XX (N transactions)
  Education:   $X,XXX.XX (N transactions)

  Total Deductions: $XX,XXX.XX

NET TAXABLE INCOME: $XX,XXX.XX

ITEMS REQUIRING REVIEW (Ambiguous):
  [date] [merchant] [amount] -- [reason for ambiguity]
  ...
```

### Step 6: Verify Pipeline Integrity

- Row count at each stage matches (no silent data loss)
- Category totals sum to grand total
- All amounts are accounted for

## Expected Results

- A complete multi-script pipeline
- An accountant-ready report
- A list of ambiguous transactions with explanations
- Verification that all 480 transactions are categorized

## Reflection

1. How did you handle transactions that could belong to multiple categories (e.g., AMAZON could be business or personal)?
2. What percentage of transactions ended up as Ambiguous? Is that acceptable for a real tax preparation?
3. Which skill from earlier modules was most critical for this capstone?
