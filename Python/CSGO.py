import time

bomb = True
timer = 2

while bomb:
    if timer <= 0:
        break
    timer -= 0.05
    print(timer)
    time.sleep(timer)