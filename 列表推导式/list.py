# for i in range(0,60):
#     num=3*i-2
#     if 0<num<60:
#         print(num)
#列表推导式
list=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58]
evens=[list[i] for i in range(0,10) if 0<3*i-2<60]
#print(evens)
#range()三元写法
# for i in range(1,10,2):
# #     print('i',i)
# for x in range(10,0,-1):
#     print(x)

#print(list[3:1:-1])
even=[i for i in range(0,10)]
even2=[1, 2, 3, 4, 5,6, 4, 5, 6, 7, 8]
print(even)
print(even[8:0:2])