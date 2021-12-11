import time


MIN = 0
licznik = 10

print("Countdown!")
while licznik >= MIN:
    time.sleep(1)
    print(f"Countdown: {licznik}")
    licznik -= 1