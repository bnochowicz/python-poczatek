def pole_prostokata(a, b):
    result = a* b
    return result


a = int(input(f"Podaj pierwszy bok prostokata: "))
b = int(input(f"Podaj drugi bok prostokata: "))

wynik = pole_prostokata(a, b)
print(wynik)