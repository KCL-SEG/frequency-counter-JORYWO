"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for element in items:
        if str(element).strip() in frequencies.keys():
            frequencies[str(element).strip()] += 1
        else:
            frequencies[str(element).strip()] = 1    
    return frequencies
