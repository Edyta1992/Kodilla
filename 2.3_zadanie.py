# 2.3_zadanie 1

name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
print(name_list)

name_dictionary = ["John", "Michael", "Terry", "Eric", "Graham"]

ilosci_liter = {}

for name in name_dictionary:
    ilosci_liter[name] = len(name)
print(ilosci_liter)


# 2.3_zadanie 2


my_numbers_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
print(my_numbers_list)

def czy_liczba_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True

wynik = []   
for name in name_list:
    dlugosc = len(name)
    if dlugosc in my_numbers_list and czy_liczba_pierwsza(dlugosc):
        wynik.append(name)
print("Imiona spełniające warunki:", wynik)



# 2.3_zadanie 3

my_list = ["pon", "śro", "pią", "sob"]
my_list.append("wt")
my_list.append("czw")
my_list.append("nd")
print(my_list)
sorted_my_list = sorted(my_list)
print(f"Lista po sortowaniu{sorted_my_list}")
print(f"Lista pierwotna{my_list}")



# 2.3_zadanie 4

print("nalej wody do czajnika")
print("włącz czajnik")
print("wyjmij kubek")
print("znajdź opakowanie herbaty")
print("włóż herbatę do kubka")
print("zalej herbatę")
