import random
n = int(input())
while n == len(list):
    f = random.randint(0 , 50)
    if f not in list:
        list.append(f)
print(list)