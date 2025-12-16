def validate_nic(nic):
    state = 0

    for ch in nic:
        if state < 9 and ch.isdigit():
            state += 1

        elif state == 9:
            if ch in ['V', 'X']:
                return "ACCEPT (Valid Old NIC)"
            elif ch.isdigit():
                state += 1
            else:
                return "REJECT"

        elif 10 <= state < 11 and ch.isdigit():
            state += 1

        elif state == 11 and ch.isdigit():
            state += 1  

        else:
            return "REJECT"

    
    if state == 12:
        return "ACCEPT (Valid New NIC)"
    
    return "REJECT"


tests = [
    # Valid Old NIC format (9 digits + V/X)
    "931234567V",
    "931234567X",
    "850123456V",
    "750987654X",
    
    # Valid New NIC format (12 digits)
    "199312345678",
    "200036612345",
    "198512349876",
    "200156789012",
    
    # Invalid - too short
    "12345678",
    "123456789",
    "1234567V",
    "12345678V",
    
    # Invalid - wrong character in middle
    "93123V567X",
    "9312A4567V",
    "199312X45678",
    "19931234A678",
    
    # Invalid - too long
    "9312345678V",
    "1993123456789",
    
    # Invalid - wrong ending character for old NIC
    "931234567A",
    "931234567Y",
    "9312345671",
    
    # Invalid - 10 digits (neither format)
    "1234567890",
    
    # Invalid - 11 digits (neither format)
    "12345678901",
    
    # Invalid - 13 digits (too long)
    "1234567890123",
    
    # Invalid - empty or special characters
    "",
    "931234567 ",
    "931234567-V",
    "931-234-567V",
    
    # Edge cases with V and X
    "000000000V",
    "999999999X",
    "000000000000",
    "999999999999",
]


for t in tests:
    result = validate_nic(t)
    print(f"{t:20} → {result}")
