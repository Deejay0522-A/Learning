import time

#start = time.time()
#time.sleep(1)
#print("hello")
#end = time.time()
#print(end - start)

run = True

while run:
    start = time.time()

    if start >= 100000000000:
        print("Shot!")
        start = 0
    if start <= 100000000000:
        print(start)
        continue

    end = time.time()