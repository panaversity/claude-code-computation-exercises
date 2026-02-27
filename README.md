# Claude Code: Computation & Data Extraction Exercises

**Build Verified Data Processing Tools**

Practice exercises for the Computation & Data Extraction chapter of the Agent Factory curriculum. You will build Python-based data processing utilities, debug broken scripts with hidden logic bugs, and construct multi-step pipelines that handle real-world CSV messiness.

## Package Structure

```
claude-code-computation-exercises/
├── EXERCISE-GUIDE.md                          # Comprehensive guide with rubrics
├── README.md                                  # This file
├── module-1-arithmetic-and-stdin/             # Decimal math & stdin tools
│   ├── exercise-1.1-expense-splitter/         # Build: per-person receipt splits
│   └── exercise-1.2-rounding-trap/            # Debug: floating-point accumulation
├── module-2-testing-and-verification/         # Zero-trust verification
│   ├── exercise-2.1-bulletproof-calculator/   # Build: test suite for working script
│   └── exercise-2.2-green-light-lie/          # Debug: 3 hidden logic bugs
├── module-3-csv-processing/                   # Real-world CSV parsing
│   ├── exercise-3.1-messy-payroll/            # Build: parse messy payroll data
│   └── exercise-3.2-awk-disaster/             # Debug: awk vs quoted CSV fields
├── module-4-categorization/                   # Pattern matching & regex
│   ├── exercise-4.1-expense-report-builder/   # Build: categorize 150+ expenses
│   └── exercise-4.2-over-eager-matcher/       # Debug: 8 false positives
├── module-5-pipeline-orchestration/           # Multi-step data pipelines
│   ├── exercise-5.1-quarterly-report/         # Build: 4-step quarterly pipeline
│   └── exercise-5.2-broken-pipeline/          # Debug: interface bugs between steps
└── module-6-capstone/                         # Choose-your-own capstone
    ├── capstone-A-freelancer-tax-prep/        # 6-month tax categorization
    ├── capstone-B-subscription-auditor/       # 12-month recurring charge detection
    └── capstone-C-your-own-data/              # Use your own bank exports
```

## Getting Started

### Prerequisites

- **Claude Code** -- all exercises involve writing and running Python scripts in the terminal
- **Python 3.x** -- scripts use standard library modules (`csv`, `decimal`, `sys`, `re`)
- No external packages required

### How to Begin

1. Clone or download this repository
2. Read `EXERCISE-GUIDE.md` for the full walkthrough and assessment rubrics
3. Start with Module 1, Exercise 1.1
4. Use Claude Code to write, run, and debug Python scripts directly in the terminal

## Recommended Order

| Module | Focus | Exercises | Time |
|--------|-------|-----------|------|
| **1. Arithmetic & Stdin** | Decimal math, composable tools | 1.1 Build, 1.2 Debug | 30-60 min |
| **2. Testing & Verification** | Zero-trust, test data design | 2.1 Build, 2.2 Debug | 30-60 min |
| **3. CSV Processing** | Real-world parsing, edge cases | 3.1 Build, 3.2 Debug | 45-75 min |
| **4. Categorization** | Regex precision, false positives | 4.1 Build, 4.2 Debug | 45-75 min |
| **5. Pipeline Orchestration** | Multi-step pipes, interfaces | 5.1 Build, 5.2 Debug | 45-75 min |
| **6. Capstone** | Full workflow integration | Choose A, B, or C | 2-4 hours |

## Data Processing Framework

Every exercise follows these 7 steps:

1. **Understand the Data** -- What format? What edge cases? What does "correct" look like?
2. **Build the Tool** -- Write a script that reads stdin and produces stdout
3. **Create Test Data** -- Make small datasets with known correct answers
4. **Verify** -- Run on test data and compare against expected results
5. **Handle Edge Cases** -- Quoted fields, missing values, mixed formats
6. **Pipeline** -- Connect tools with pipes for multi-step processing
7. **Make Permanent** -- Save scripts, create aliases, document usage

## Exercise Pattern

Each module follows the same structure:

- **X.1 = Build** -- Create a working utility from real data
- **X.2 = Debug** -- Find and fix bugs in broken scripts

Build exercises teach you to create tools. Debug exercises teach you that "runs without errors" is not the same as "produces correct results."

## License

Educational exercises by Panaversity. For learning purposes.
