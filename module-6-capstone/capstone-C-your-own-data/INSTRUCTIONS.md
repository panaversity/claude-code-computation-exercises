# Capstone C -- Your Own Financial Data

**Build** -- Process your real bank data with a custom pipeline

## Goal

Export your own bank statement CSVs and build a complete processing pipeline tailored to YOUR financial categories, YOUR merchants, and YOUR patterns. This is not a simulation -- you will build a tool you can actually use every month.

## What You Have

- Your own bank's CSV export (you will obtain this yourself)
- All the skills from Modules 1-5

## Your Tasks

### Step 1: Export Your Data

Download CSV exports from your bank for at least 3 months. Note:
- Every bank formats CSVs differently (column names, date formats, amount signs)
- Some banks use positive numbers for debits and negative for credits (or vice versa)
- Some include running balance, others do not
- File encoding may be UTF-8, Latin-1, or include a BOM marker

### Step 2: Understand Your Format

Examine the CSV carefully:
- What are the column headers?
- How are dates formatted?
- How are amounts represented? (Negative for debits? Separate debit/credit columns?)
- Are there any quoted fields with commas?

### Step 3: Define Your Categories

Create categories that reflect YOUR life. Examples:
- Housing (rent, mortgage, maintenance)
- Transportation (gas, transit, car payment)
- Food (groceries, restaurants, delivery)
- Entertainment (streaming, events, hobbies)
- Health (medical, pharmacy, gym)
- Professional (tools, education, conferences)
- Savings/Investment (transfers to savings)
- Income (salary, freelance, side projects)

### Step 4: Build and Test Your Categorizer

Create a categorizer for YOUR merchants. Start with your 20 most frequent merchants and add more as you discover them. Test with known transactions first.

### Step 5: Process and Review

Run your pipeline on the full dataset. Review the results:
- Are the category assignments correct?
- What ended up as Uncategorized? Add those merchants to your patterns.
- Do the totals make sense for your spending patterns?

### Step 6: Make It Reusable

Structure your tool so that next month you can:
```bash
python process-statements.py < march-2025.csv >> spending-report.csv
```

Document:
- How to export from your bank
- What categories you defined and why
- Any merchant-specific rules or overrides

## Expected Results

- A working pipeline that processes YOUR bank data
- Category definitions documented in a config file or at the top of your script
- At least 3 months of categorized data
- A summary report showing spending by category

## Privacy Note

Your financial data is private. You do not need to share it with anyone. The deliverable is the TOOL (scripts and configuration), not the data.

## Reflection

1. What was the hardest part of adapting the exercise patterns to your real data?
2. How did your bank's CSV format differ from the exercise files? What adjustments were needed?
3. What surprised you about your own spending when you saw it categorized?
