# Dokumentacja funkcji zip():
# https://docs.python.org/3/library/functions.html#zip

# Dokumentacja modułu math:
# https://docs.python.org/3/library/math.html

# Dokumentacja wyjątku ValueError:
# https://docs.python.org/3/library/exceptions.html#ValueError

import math  # import modułu matematycznego

# Tworzenie dwóch list z imionami i wiekiem psów
dog_names = ["Reksio", "Azor", "Burek"]
dog_ages = [2, 5, 4]

# Łączenie list funkcją zip() – tworzy listę krotek (imię, wiek)
combined = list(zip(dog_names, dog_ages))
print("Lista psów i ich wieku:")
print(combined)

# Pobranie liczby od użytkownika i obliczenie pierwiastka kwadratowego
try:
    user_input = float(input("\nPodaj liczbę, aby obliczyć pierwiastek kwadratowy: "))
    result = math.sqrt(user_input)  # funkcja sqrt() oblicza pierwiastek
    print(f"Pierwiastek kwadratowy z {user_input} wynosi {result:.2f}")
except ValueError:
    # Obsługa wyjątku, gdy użytkownik poda wartość niebędącą liczbą
    print("Błąd: podana wartość nie jest liczbą!")

