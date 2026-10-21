# Name: Zoey Spies
# KUID: 3136594
# LAB Session (Day/Time): Monday 11 AM
# LAB Assignment: Lab 6
# Description: This program calculates the binomial expansion of (x+y)^n.
#
#
#
# Collaborators/Sources: 268 notes, stackoverflow.com, geeksforgeeks.org, python documentation
import sys
import math as m

def get_input(mode):
    """
    Reads the (x+y)^n expression from command line arguments if provided,
    otherwise prompts the user. Strips all whitespace.

    mode == 1: returns the full cleaned expression as a string, e.g. "(x+y)^4"
    mode == 0: returns only the exponent n as an int, e.g. 4
    """
    if len(sys.argv) > 1:
        raw = " ".join(sys.argv[1:])
    else:
        raw = input("Enter expression (e.g. (x+y)^4): ")

    # Remove all whitespace
    cleaned = "".join(raw.split())

    if mode == 0:
        # Keep only digit characters, then convert to int
        digits = "".join(ch for ch in cleaned if ch.isdigit())
        return int(digits)

    return cleaned

def binomial_coefficient(n, k): # returns the binomial coefficient C(n, k) = n! / (k! * (n-k)!)
    return m.factorial(n) // (m.factorial(k) * m.factorial(n - k))

def validate_expression(expr): # validates the expression (x+y)^n
    import re
    pattern = r'^\(\w+\+\w+\)\^\d+$'
    return bool(re.match(pattern, expr))

def variables_from_expression(expr): # extracts the variables x and y from the expression (x+y)^n
    import re
    match = re.match(r'^\((\w+)\+(\w+)\)\^\d+$', expr)
    if match:
        return match.groups()
    else:
        raise ValueError("Invalid expression format. Expected format: (x+y)^n")

def expand_binomial(expr): # expands the binomial expression (x+y)^n and returns the expanded form as a string
    # Validate the expression
    if not validate_expression(expr):
        raise ValueError("Invalid expression format. Expected format: (x+y)^n")

    # Extract variables and exponent
    import re
    match = re.match(r'^\((\w+)\+(\w+)\)\^(\d+)$', expr)
    if not match:
        raise ValueError("Invalid expression format. Expected format: (x+y)^n")

    x, y, n = match.groups()
    n = int(n)

    terms = []
    for k in range(n + 1):
        coeff = binomial_coefficient(n, k)
        term = f"{coeff}{x}^{n-k}{y}^{k}" if coeff != 1 else f"{x}^{n-k}{y}^{k}"
        terms.append(term)

    return " + ".join(terms)


if __name__ == "__main__":
    full_expr = get_input(1)   # e.g. "(x+y)^4" (string)
    print(full_expr)           # type string

    expanded = expand_binomial(full_expr)
    print(expanded)            # type string

    n = get_input(0)           # e.g. 4 (int)
    print(n)                   # type int