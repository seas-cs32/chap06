### chap06/ale04_double.py
import time

# FIXME: initialize i appropriately
next_bound = 1

while True:
    # FIXME: update i so it doubles each time
    if i > next_bound:
        print(f'Passed {i}')
        next_bound *= 10
        time.sleep(0.5)
