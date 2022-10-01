"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for element in items:
        string_element = str(element).strip()
        if string_element in frequencies.keys():
            frequencies[string_element] += 1
        else:
            frequencies[string_element] = 1    
    return frequencies
