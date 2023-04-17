from DataMain import Input
from DataMain import Calculator

to = Input()
state_choice = to.state()

calc = Calculator()
percentage_change_1 = calc.wages_calculator()
mean_calculator = calc.mean_house_calculator()

di = to.dictionary()

results = f'Employment rates in {state_choice} have seen a {percentage_change_1} change\n' \
          f'over the last quarter of 2022.\n' \
          f'The average house price in {state_choice} in the last three years was {mean_calculator}.'
print(results)
print(di)
