def find_non_consecutive_repeated_chars(s):
    from collections import defaultdict

    # Initialize a dictionary to keep track of character occurrences
    char_positions = defaultdict(list)

    # Store the positions of each character in the string
    for index, char in enumerate(s):
        char_positions[char].append(index)

    # List to hold valid characters that meet the condition
    valid_chars = []

    # Check each character's positions
    for char, positions in char_positions.items():
        if len(positions) >= 2:
            # Check if the character appears at least twice and is not consecutive
            for i in range(1, len(positions)):
                if positions[i] > positions[i - 1] + 1:
                    valid_chars.append(char)
                    break

    # Sort the valid characters alphabetically
    valid_chars.sort()

    # Return the result as a string or 'N' if no valid characters found
    return ''.join(valid_chars) if valid_chars else 'N'

# Example usage
s = 'edeaaabbccd'
result = find_non_consecutive_repeated_chars(s)
print(result)  # Output: 'd' (since 'e' appears twice but consecutively)
