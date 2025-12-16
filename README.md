# NIC Validator - Automata Theory Assignment

A finite state automaton implementation that validates Sri Lankan National Identity Card (NIC) numbers.

## Overview

This project demonstrates the application of finite state machines (FSM) to validate two formats of NIC numbers:

### NIC Formats Supported

1. **Old NIC Format**: 9 digits followed by 'V' or 'X'
   - Example: `931234567V`, `931234567X`
   - Pattern: `[0-9]{9}[VX]`

2. **New NIC Format**: Exactly 12 digits
   - Example: `199312345678`, `200036612345`
   - Pattern: `[0-9]{12}`

## How It Works

The `validate_nic()` function implements a state machine with the following states:

- **States 0-8**: Read first 9 digits
- **State 9**: Accept 'V' or 'X' (old format) OR read 10th digit (new format path)
- **States 10-11**: Read 10th-11th digits
- **State 12**: Reached after reading 12th digit (new format complete)

### State Transitions

```
Input: Digit (0-9)
- States 0-8 → increment state
- State 9 (new format path) → State 10
- State 10 → State 11
- State 11 → State 12 (ACCEPT if string ends)

Input: V or X
- State 9 → ACCEPT (old format complete)

Invalid: Any other character → REJECT
```

## Usage

Run the script:

```bash
python transition.py
```

This will execute all test cases and display validation results.

## Test Cases

The script includes comprehensive test cases covering:

- ✓ Valid old NIC formats (with V and X)
- ✓ Valid new NIC formats (12 digits)
- ✗ Invalid formats (wrong length, wrong characters, special characters)
- ✗ Edge cases (boundary conditions, empty strings)

### Sample Output

```
931234567V           → ACCEPT (Valid Old NIC)
199312345678         → ACCEPT (Valid New NIC)
93123V567X           → REJECT
1234567890123        → REJECT
```

## Files

- `transition.py` - Main validation script with test cases
- `README.md` - This file
- `.gitignore` - Git ignore rules

## Requirements

- Python 3.6+

## Author

AUTOMATA Theory Makeup Assignment - BSc.AI L3S1

## Course

Automata Theory
