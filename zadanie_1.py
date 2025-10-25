# Funkcja zip() służy do łączenia wielu iterowalnych obiektów (np. list, krotek) w pary elementów o tych samych indeksach. Zwraca iterator krotek.
# Jeśli listy mają różną długość, wynik będzie tak długi jak najkrótsza lista.
# 
# https://docs.python.org/pl/3.14/library/functions.html#zip
# 
# 
# Moduł math zawiera funkcje matematyczne, które działają na liczbach rzeczywistych (typu float).
# Zawiera m.in. funkcje trygonometryczne, logarytmy, stałe matematyczne (pi, e) oraz funkcje zaokrąglające.
# 
# https://docs.python.org/pl/3.14/library/math.html#module-math
# 
# 
# ValueError występuje, gdy funkcja otrzymuje argument o poprawnym typie, ale niewłaściwej wartości.
# Na przykład, gdy próbujesz przekonwertować napis, który nie jest liczbą, na typ int.
# 
# https://docs.python.org/pl/3.14/library/exceptions.html#ValueError


import math

dog_names = ["Reksio", "Azor", "Burek"]
dog_ages = [2, 5, 4]

combined = list(zip(dog_names, dog_ages))
print("Lista psów i ich wieku:")
print(combined)

try:
    user_input = float(input("\nPodaj liczbę, aby obliczyć pierwiastek kwadratowy: "))
    result = math.sqrt(user_input) 
    print(f"Pierwiastek kwadratowy z {user_input} wynosi {result:.2f}")
except ValueError:
    print("Błąd: podana wartość nie jest liczbą!")

