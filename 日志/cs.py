import random
lis = [1, 2, 3, 'a', 'b','3']
print(lis)

a = lis.pop()

print(a)
print(lis)

# while len(lis)>0:
#     num=len(lis)
#     print(num)
#     for  i in  range(num):
#         x=random.randint(0,len(lis)-1)
#         print('序号',x)
#         print('内容',lis[x])
#         lis.pop(x)
#         continue
#
# print(lis)