# Exercise 1.1 -- The Expense Splitter

**Build** -- Create a reusable receipt-splitting utility that handles decimal arithmetic correctly

## Goal

Build a Python script that reads a dinner receipt from stdin and calculates the per-person split. The tool should handle decimal math correctly (no lost cents), work with any receipt in the provided format, and follow the stdin/stdout pattern so it can be used in pipelines.

## What You Have

- `dinner-receipts/receipt-1-italian.txt` -- 4 attendees, straightforward split
- `dinner-receipts/receipt-2-thai.txt` -- 5 attendees, uneven total (odd cents)
- `dinner-receipts/receipt-3-sushi.txt` -- 6 attendees, one person had only drinks
- `dinner-receipts/receipt-4-bbq.txt` -- 3 attendees, includes a discount/coupon (negative line item)
- `dinner-receipts/receipt-5-large-party.txt` -- 8 attendees, many items, large total

Each receipt follows the same format: header with restaurant name and attendee count, itemized list, then subtotal/tax/tip/total.

## Your Tasks

### Step 1: Examine the Data

Read at least two receipt files. Note the format -- where is the attendee count? Where is the total? Are there any edge cases in the numbers?

### Step 2: Build the Splitter

Write a Python script (`split-receipt.py`) that:
- Reads a receipt from stdin
- Extracts the number of attendees and the total
- Calculates the per-person amount
- Outputs: total, number of people, per-person amount, and any remainder cents

### Step 3: Test on Each Receipt

Run your script on all 5 receipts:
```bash
python split-receipt.py < dinner-receipts/receipt-1-italian.txt
```

### Step 4: Handle Edge Cases

- What happens when the total does not divide evenly? (Receipt 2)
- What about the receipt with a discount? (Receipt 4)
- Does your script handle the large party correctly? (Receipt 5)

### Step 5: Verify Arithmetic

For at least one receipt, compute the per-person split by hand. Compare against your script's output. They must match to the cent.

## Expected Results

- A working `split-receipt.py` that processes any receipt in the provided format
- Correct per-person amounts for all 5 receipts
- Proper handling of uneven splits (remainder cents accounted for)
- Script reads from stdin and writes to stdout

## Reflection

1. What happens to the "remainder" when a total does not split evenly among attendees? How did you handle it?
2. Why is `decimal.Decimal` preferable to `float` for this kind of calculation?
3. Could your script be piped with other tools? For example, processing all 5 receipts and summing the per-person amounts?
