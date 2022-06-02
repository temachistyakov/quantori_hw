listed_num = [1,2,3,4,5,6,7,8,9,10,33,54,453,666,254,2342,111,22]
for x in listed_num:
    mod = x % 2
    if x == 254:
        break
    elif mod == 0:
        print(x)
