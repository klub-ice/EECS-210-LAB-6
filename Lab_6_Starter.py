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

def variable_term(var, power): # returns "", "x", or "x^3" depending on the power
    if power == 0:
        return ""
    if power == 1:
        return var
    return f"{var}^{power}"

def expand_binomial(n): # expands (x+y)^n and returns the expanded form as a string
    terms = []
    for k in range(n + 1):
        coeff = binomial_coefficient(n, k)
        coeff_str = "" if coeff == 1 else str(coeff)
        terms.append(coeff_str + variable_term("x", n - k) + variable_term("y", k))

    return " + ".join(terms)


if __name__ == "__main__":
    n = get_input(0)           # e.g. 4 (int)
    print(expand_binomial(n))