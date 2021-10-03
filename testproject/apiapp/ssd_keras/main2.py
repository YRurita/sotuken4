import time
from conunt_person import count_person

def main2():
    num = count_person()
    #print("人数は" + str(num) + "人です")
    #return num


"""""
count = []
def worker():
    num = count_person()
    print("人数は" + str(num) + "人です") 
    count.append(num)
    time.sleep(1)


interval = 5
for i in range(1,10):
    worker()
    time.sleep(interval)

print(count)
#num = count_person()
#print(num)
"""