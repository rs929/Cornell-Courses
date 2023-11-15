"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Noelle Pappous (ntp26) Richie Sun (rs929)
Date:   09/18/21
"""
import a1

original = input("Enter original currency: ")
new = input("Enter desired currency: ")
amount = str(input("Enter original amount: "))
amount2 = float(amount)

print("You can exchange " + amount + " " + original + " for " +
        str(a1.exchange(original, new, amount2)) + " " + new + ".")
