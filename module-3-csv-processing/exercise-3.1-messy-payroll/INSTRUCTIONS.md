# Exercise 3.1 -- The Messy Payroll

**Build** -- Parse a messy payroll CSV with real-world formatting challenges

## Goal

Build a Python script that correctly parses `payroll-data.csv` (85 employee records) and extracts the total payroll cost for all active employees. The data has every common CSV messiness: company names with commas, names with apostrophes, currency-formatted salaries, mixed date formats, empty fields, and extra whitespace.

## What You Have

- `payroll-data.csv` -- 85 employee records with columns: employee_id, name, company, department, hire_date, salary, bonus, status

### Data Challenges You Will Encounter

- **Commas in company names**: "Acme, Inc." -- breaks naive comma splitting
- **Apostrophes in names**: "O'Brien" -- watch for quote handling
- **Currency formatting**: "$85,000.00" -- dollar signs AND comma thousands separators in numbers
- **Mixed date formats**: "01/15/2023" and "2023-03-22" in the same file
- **Empty bonus fields**: Some employees have no bonus listed
- **Status values**: Active, On Leave, Terminated -- you only want Active employees
- **Extra whitespace**: Some fields have leading/trailing spaces

## Your Tasks

### Step 1: Examine the Data

Look at the first 10-15 rows of the CSV. Identify each type of messiness. Note which columns will need cleaning before you can do math.

### Step 2: Build the Parser

Write a Python script that:
- Uses `csv.reader` (not string splitting) to correctly handle quoted fields
- Strips currency symbols and comma separators from salary and bonus columns
- Handles empty bonus fields (treat as $0)
- Filters for Active employees only
- Outputs: active employee count, total salary, total bonus, combined total

### Step 3: Verify with Manual Spot Checks

Pick 3 employees from the CSV and compute their contribution to the total by hand. Verify your script includes them correctly.

### Step 4: Handle All Edge Cases

Make sure your script handles:
- Names with apostrophes and commas
- Companies with commas (the CSV file uses proper quoting, but your parser must respect it)
- Both date formats (you do not need to normalize dates, just ensure they do not break parsing)
- Whitespace in any field

## Expected Results

- A working `process-payroll.py` script
- Output showing: number of active employees, total salary, total bonus, grand total
- Correct handling of all 85 rows (no skipped rows, no parse errors)

## Reflection

1. What would have happened if you used `line.split(",")` instead of `csv.reader`? How many rows would break?
2. How did you handle the currency formatting ($85,000.00)? What string operations were needed?
3. If this payroll data were updated monthly, what would you change in your script to make it a reusable tool?
