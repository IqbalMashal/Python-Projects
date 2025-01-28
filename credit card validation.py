

sum_odd_digits = 0
sum_even_digits = 0
total = 0


credit_Card = input("Enter you credit card number: ")

credit_Card = credit_Card.replace("-", "")
credit_Card = credit_Card.replace(" ", "")
credit_Card = credit_Card[::-1]


for x  in credit_Card[::2]:
    sum_odd_digits += int(x) 


for x in credit_Card[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x


total = sum_odd_digits + sum_even_digits


if total % 10 == 0:
    print("VALID")

else:
    print("INVALID")