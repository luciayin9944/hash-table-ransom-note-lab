def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # TODO: Implement this function

    letter_count = {} #hash table

    # populate hash table
    for letter in magazine:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Check each character in ransomNote
    for l in ransomNote:
        if l not in letter_count or letter_count[l]==0:
            return False
        letter_count[l] -= 1

    # All characters matched
    return True
        



