

import time

my_time = input("Enter the tie in secounds ")

for x in range(my_time, 0, -1):
    seconds = x % 60
    mins = int(x / 60)
    hour = int(x/3600)

    print(f"{hour:02}:{min:02}:{seconds:02}")
    time.sleep(1)


print("Times's UP!")
