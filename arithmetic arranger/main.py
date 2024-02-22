# This entrypoint file to be used in development. Start by reading README.md
'''
  DISCLAIMER: The test enviroment doesn't work like it shoud and this code can't be tested properly. The other exercises are function all right. I've searched the solution in online forums but nothing worked.
'''

from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(['-vv'])
