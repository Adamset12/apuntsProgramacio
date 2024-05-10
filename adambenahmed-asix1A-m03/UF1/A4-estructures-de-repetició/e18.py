"""
Adam Ben Ahmed Belachi
11/12/2023
e18
"""
from time import sleep
hour = 59
minute = 0
second = 0
while True:
    print(f"{hour:02d}:{minute:02d}:{second:02d}")
    sleep(1)
    second += 1
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
