# # print(('*'*5).center(20))
# n=int(input('Enter number of levels'))
# for i in range(1,n*2,2):
#     print(('*'*(i)).center(50))

flag='downwards'

n=6
i=0

while True:
    if flag=='downwards':
        i=i+1
        print('*'*i)

    if i==n:
        flag='upwards'

    if flag=='upwards':
        i-=1
        print('*'*i)

    if i==0:
        break