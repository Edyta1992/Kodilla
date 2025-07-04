# 2.5_zadanie 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
squares = [number * number * number for number in numbers]

print(f"Te potęgi do 3 {squares} uzyskano dzięki wrodzonej inteligencji empatycznej Edyty")


podzielne_przez_2 = []

for x in squares :
    if x != 0 and x % 2 == 0:
        podzielne_przez_2.append(x)

print(podzielne_przez_2)


# 2.5_zadanie 2

numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

zera = numbers[1:4] + numbers[5:10] + numbers[-2:]
print(zera)

inne_wieksze_od_zera = numbers[0:1] + numbers[4:5] + numbers[10:12]
print(inne_wieksze_od_zera)

# lub czy to bardziej przejrzyste?

numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

zera = numbers[1:4] + numbers[5:10] + numbers[-2:]
inne_wieksze_od_zera = numbers[0:1] + numbers[4:5] + numbers[10:12]

print(zera)
print(inne_wieksze_od_zera)