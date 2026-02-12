# Exercise 4.2 -- The Over-Eager Matcher

**Debug** -- Fix 8 false positives in a transaction categorizer

## Goal

`buggy-categorizer.py` processes `transactions.csv` and categorizes each transaction. But it has exactly 8 false-positive bugs -- merchants that get assigned to the wrong category because the regex patterns are too broad. Fix all 8 without breaking the legitimate matches those patterns are supposed to catch.

## What You Have

- `transactions.csv` -- 114 transactions including the 8 tricky merchants
- `buggy-categorizer.py` -- Categorizer with 8 false positive patterns

### The 8 False Positives

| # | Merchant | Wrong Category | Correct Category | Why It Matches Wrong |
|---|----------|---------------|-----------------|---------------------|
| 1 | DR PEPPER SNAPPLE GROUP | Medical | Food/Grocery | Pattern `DR\s` matches "DR PEPPER" |
| 2 | RED LOBSTER | Charitable | Food | Pattern `RED` matches "RED LOBSTER" (meant for RED CROSS) |
| 3 | SUBWAY RESTAURANT | Transit | Food | Pattern `SUBWAY` matches the restaurant |
| 4 | TARGET | Shopping | Shopping (ok) but pattern is too broad | Would match any merchant with "TARGET" in name |
| 5 | SHELL GAS STATION | Tech | Gas/Transit | Pattern `SHELL` matches gas station (meant for Shell scripting) |
| 6 | APPLEBEES | Electronics | Food | Pattern `APPLE` matches "APPLEBEES" (meant for Apple Store) |
| 7 | AMAZON FRESH | Grocery AND Shopping | Grocery only | Matches `FRESH` in Grocery and `AMAZON` in Shopping -- double-counted |
| 8 | BEST BUY | Food | Electronics | Pattern `BEST` in Food category matches "BEST BUY" |

## Your Tasks

### Step 1: Run the Buggy Script

```bash
python buggy-categorizer.py < transactions.csv
```

Examine the output. Note which categories have inflated counts (due to false positives) or double-counted amounts.

### Step 2: Trace Each False Positive

For each of the 8 bugs, identify:
- Which line in the script contains the problematic pattern
- What the pattern matches that it should not
- What legitimate merchants the pattern IS supposed to match

### Step 3: Fix Each Bug

Apply the appropriate fix for each:
- **Word boundaries** (`\b`) to prevent partial matches (e.g., `\bAPPLE\b` does not match APPLEBEES)
- **More specific patterns** (e.g., `RED CROSS` instead of just `RED`)
- **False-positive exclusion lists** (check before matching)
- **Category priority/deduplication** (prevent double-counting)

### Step 4: Verify Fixes

After fixing, run the script again. Verify:
- DR PEPPER is categorized as Food, not Medical
- RED LOBSTER is categorized as Food, not Charitable
- SUBWAY RESTAURANT is Food, not Transit
- SHELL GAS STATION is not Tech
- APPLEBEES is Food, not Electronics
- AMAZON FRESH appears in only ONE category
- BEST BUY is Electronics, not Food

### Step 5: Confirm No Regressions

Make sure your fixes did not break legitimate matches:
- DR SMITH FAMILY MEDICINE should still be Medical
- RED CROSS DONATION should still be Charitable
- MTA SUBWAY FARE should still be Transit
- APPLE STORE should still be Electronics
- Regular AMAZON purchases should still be Shopping

## Expected Results

- All 8 false positives fixed
- For each fix: documentation of what the bug was and how you fixed it
- No regressions in legitimate matches
- Corrected category totals with no double-counting

## Reflection

1. Which fix technique was most broadly useful: word boundaries, specific patterns, or exclusion lists?
2. Why does the order of category matching matter? How does matching Medical before Food cause different results than the reverse?
3. If you had 1000 merchants instead of 114, how would you systematically test for new false positives?
