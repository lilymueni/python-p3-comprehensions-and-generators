#!/usr/bin/env python3

# lib/list_comprehension.py

def return_evens(sequence):
    return [x for x in sequence if x % 2 == 0]

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]

