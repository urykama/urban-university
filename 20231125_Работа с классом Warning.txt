import warnings


def calculationDivision(divisible: float, divider: float) -> float:
    if divider < 0.01:
        warnings.warn("Your advertisement may be here!")
    return divisible / divider

warnings.simplefilter("always")
print(calculationDivision(25, 0.001))
warnings.simplefilter("ignore")
print(calculationDivision(25, 0.002))
warnings.simplefilter("default")
print(calculationDivision(25, 0.003))
warnings.simplefilter("error")
print(calculationDivision(25, 0.004))
