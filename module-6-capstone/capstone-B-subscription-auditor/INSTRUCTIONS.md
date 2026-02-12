# Capstone B -- The Subscription Auditor

**Build** -- Detect and analyze recurring subscriptions across 12 months of bank data

## Goal

Build a tool that analyzes one year of bank transactions (814 rows), identifies recurring subscription charges, calculates annual costs, detects price changes, flags cancelled and new subscriptions, and identifies potential duplicates. This capstone focuses on pattern detection across time rather than simple categorization.

## What You Have

- `annual-transactions.csv` -- 814 transactions across 12 months (January through December 2025) with columns: date, merchant, amount

The data includes:
- **Monthly subscriptions**: Netflix, Spotify, AWS, gym, Adobe, and more
- **Annual subscriptions**: Amazon Prime (March), domain renewal (June)
- **A price change**: Netflix went from $15.99/month to $17.99/month in July
- **A cancellation**: Hulu appears January through May, then stops
- **A new subscription**: Disney+ starts in September
- **A potential duplicate**: "GOOGLE ONE STORAGE" and "GOOGLE CLOUD STORAGE" -- same service or different?
- **Variable amounts**: AWS charges vary month to month ($47-$85)
- **~650 non-subscription transactions** mixed in (groceries, gas, dining, income, etc.)

## Your Tasks

### Step 1: Define What a Subscription Looks Like

A subscription is a charge from the same merchant at roughly the same amount, recurring on a regular schedule (monthly or annually). Define your detection criteria:
- Same merchant name (exact or fuzzy match)
- Similar amount (within what tolerance?)
- Recurring pattern (how many consecutive months to confirm?)

### Step 2: Build the Detector

Write a script that:
- Groups transactions by merchant
- Identifies merchants with recurring monthly charges
- Detects the charge amount and frequency
- Handles variable amounts (AWS) with a tolerance range

### Step 3: Analyze Each Subscription

For each detected subscription, calculate:
- Monthly cost (or annual cost for annual subscriptions)
- Total annual cost
- Months active (first charge to last charge)
- Any price changes (amount differs between months)

### Step 4: Detect Anomalies

Identify:
- **Price changes**: Netflix price increase in July
- **Cancellations**: Hulu stops appearing after May
- **New subscriptions**: Disney+ starts in September
- **Potential duplicates**: Google One Storage vs Google Cloud Storage

### Step 5: Generate Audit Report

```
SUBSCRIPTION AUDIT REPORT -- 2025
========================================

ACTIVE SUBSCRIPTIONS (as of December):
  Netflix           $17.99/mo  ($203.88/yr)  *Price changed Jul: $15.99 -> $17.99
  Spotify Premium   $10.99/mo  ($131.88/yr)
  AWS               $47-85/mo  (~$XXX.XX/yr)  [Variable]
  ...

CANCELLED SUBSCRIPTIONS:
  Hulu              $12.99/mo  Active: Jan-May  Total: $64.95

NEW SUBSCRIPTIONS (started this year):
  Disney+           $13.99/mo  Started: Sep   Projected annual: $167.88
  ChatGPT Plus      $20.00/mo  Started: Mar   Projected annual: $240.00

POTENTIAL DUPLICATES:
  Google One Storage ($2.99/mo) vs Google Cloud Storage ($2.99/mo)
  -- Same amount, same company. Possible duplicate charge.

ANNUAL SUMMARY:
  Total subscription spend:     $X,XXX.XX
  Total non-subscription spend: $XX,XXX.XX
  Subscription % of expenses:   XX.X%
```

## Expected Results

- A subscription detection script that identifies all recurring charges
- Correct annual cost calculations for each subscription
- Detection of the Netflix price change, Hulu cancellation, and Disney+ start
- Identification of the Google storage potential duplicate
- A complete audit report

## Reflection

1. How did you handle variable-amount subscriptions like AWS? What tolerance did you use?
2. What is the minimum number of recurring charges needed to confidently identify a subscription? Why?
3. If this tool processed your own bank data, what subscriptions might surprise you?
