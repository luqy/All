numberlist=[4,3,2,5,1]
length = len(numberlist)
for i in range(length):
    print("---")
    for j in range(1, length - i):
        if numberlist[j - 1] > numberlist[j]:
            print(numberlist[j-1],numberlist[j])
            numberlist[j], numberlist[j-1] = numberlist[j-1 ], numberlist[j]
            print(numberlist)
print(numberlist)


str='123'
print(list(str))
# list=[3,4]
# list[0],list[1]=list[1],list[0]
# print(list)