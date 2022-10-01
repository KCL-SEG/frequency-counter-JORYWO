"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for element in items:
        if element in frequencies.keys():
            frequencies[element] += 1
        else:
            frequencies[element] = 1    
    return frequencies
