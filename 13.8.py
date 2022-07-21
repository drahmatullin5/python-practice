chield_price = 0.00
adult_price = 990.00
senior_price = 1390.00

total = 0

ticket_numbers = int(input("Введите количество билетов: "))

for i in range(ticket_numbers):
    age = int(input("Введите возраст: "))
    if age < 18:
        total += chield_price
    elif 18 <= age <= 25:
        total += adult_price
    else:
        total += senior_price


print("Cумма посещения составила :", total)

if ticket_numbers > 2:
    total = total - (total * 10 / 100)
else:
    total
print("Сумма с учетом 10% скидки составила: ", total)








