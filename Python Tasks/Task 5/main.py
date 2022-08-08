# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos
from modules.math.composition import composition as addition
from modules.math.division import division
from modules.math.multiplication import multiplication
from modules.math.subtraction import substraction
from modules.numbers.numbers import *

# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four)
b = division(four, two)
c = substraction(three, two)
d = multiplication(five, two)

print(a)
print(b)
print(c)
print(d)
