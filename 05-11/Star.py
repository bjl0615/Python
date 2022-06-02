# for i in range(5) :
#     for j in range(i+1) :
#         print('*', end="")
#     print('')

# for i in range(5) :
#     print('{:<5}'.format('*' * (i+1)))

# # for i in range(5,0,-1) :
# #     for j in range(i) :
# #         print('*' , end="")

# #     print('')
# for i in range(6, 0 , -1) :
#     print('{:<5}'.format('*' * (i -1)))

# # for i in range(5) :
# #     for j in range(i):
# #         print(' ' , end="")
# #     for j in range(5-i) :
# #         print('*' , end="")
# #     print('')
# for i in range(6, 0 , -1) :
#     print("{:>5}".format('*' * (i -1)))

# # for i in range(1,6): 
# #     for j in range(5-i): 
# #         print(' ',end="") 
# #     for j in range(i): 
# #         print('*',end="") 
# #     print('')
# for i in range(5) :
#     print("{:>5}".format('*' * (i + 1)))

# for i in range(1,6) :
#     for j in range(5-i) :
#         print(' ', end="")
#     for j in range(1,i*2,1) :
#         print('*' , end="")
#     print('')
# for i in range(1, 11 , 2) :
#     print("{:^10}".format('*' * i))
























for i in range(5) :
    for j in range(i+1) :
        print('*', end="")
    print('')

for i in range(1,6) :
    for j in range(6 - i) :
        print('*' , end="")
    print('')

for i in range(5):
    for j in range(i+1) :
        print(' ', end="")
    for j in range(5 - i):
        print('*' , end="")
    print('')
for i in range(5) :
    for j in range(5- i) :
        print(" " , end = "")
    for j in range(i + 1) :
        print('*' , end="")
    print('')

for i in range(5) :
    for j in range(5 - i) :
        print(' ' , end="")
    for j in range(1, i*2 , 1) :
        print('*', end="")
    print("")
for i in range(5) :
    for j in range(i) :
        print(' ', end="")
    for j in range(10, 1+i*2 , -1) :
        print('*', end="")
    print('')
