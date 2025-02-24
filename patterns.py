# print(('*'*5).center(20))



#q5.-
# flag='downwards'

# n=6
# i=0

# while True:
#     if flag=='downwards':
#         i=i+1
#         print('*'*i)

#     if i==n:
#         flag='upwards'

#     if flag=='upwards':
#         i-=1
#         print('*'*i)

#     if i==0:
#         break


# # Q11.-
# n=int(input('Enter number of levels'))
# for i in range(1,n*2,2):
#     print(('*'*(i)).center(n*2))
# for i in range((n-1)*2-1,0,-2):
#     print(('*'*(i)).center(n*2))


#q12.-
# n=int(input('Enter number of levels'))

# for i in range(n*2-1,0,-2):
#     print(('*'*(i)).center(n*2))
# for i in range(3,(n)*2,2):
#     print(('*'*(i)).center(n*2))


#q13.-
# n=int(input('Enter number of levels'))

# for i in range(1,n+1):
#     print(('*'*i).ljust(n)+('*'*i).rjust(n))


#q14.-
# n=int(input('Enter number of levels'))

# for i in range(n,0,-1):
#     print(('*'*i).ljust(n)+('*'*i).rjust(n))


#q15.-
# n=int(input('Enter number of levels'))

# for i in range(1,n):
#     print(('*'*i).ljust(n)+('*'*i).rjust(n))

# for i in range(n,0,-1):
#     print(('*'*i).ljust(n)+('*'*i).rjust(n))


#q16.-
# n=int(input('Enter number of levels'))

# for i in range(n,1,-1):
#     print(('*'*i).ljust(n)+('*'*i).rjust(n))
# for i in range(1,n+1):
#     print(('*'*i).ljust(n)+('*'*i).rjust(n))

#q.17-
# n=5
# print('*')
# for i in  range(1,n-1):
#     print('*'+('*'+' '*(n-i)).rjust(n))

# print('*'*n)


#q.18-
# n=5
# print('*'*n)
# for i in  range(n-2,0,-1):
#     print('*'+('*'+' '*(n-i)).rjust(n))
# print('*')


#q.19-
# n=5
# print('*'.rjust(n))
# for i in  range(n-1,1,-1):
#     print('*'.rjust(i)+'*'.rjust(n-i))
# print('*'*n)


#q20. 
# n=5
# print('*'*n)
# for i in range(2,n):
#     print('*'.rjust(i)+'*'.rjust(n-i))
# print('*'.rjust(n))

#q21.-
n=5
print('*')
for i in range(1,n):
    print('*'.ljust(i)+'*'.ljust(n-i))

for i in range(n,0,-1):
    print('*'.ljust(i)+'*'.ljust(n-i))
print('*')

#q22.-
# n=5
# print('*'*n)

# for i in range(n-2,0,-1):
#     print('*'.ljust(i)+'*'.ljust(n-i))
# print('*')
# for i in range(1,n-1):
#     print('*'.ljust(i)+'*'.ljust(n-i))

# print('*'*n)

#q23.

# n=5
# print('*'.rjust(n))
# for i in  range(n-1,1,-1):
#     print('*'.rjust(i)+'*'.rjust(n-i))
# # print('*'*n)

# n=5
# # print('*'*n)
# for i in range(1,n):
#     print('*'.rjust(i)+'*'.rjust(n-i))
# print('*'.rjust(n))

#q24.

# n=5
# print('*'*n)
# for i in range(2,n):
#     print('*'.rjust(i)+'*'.rjust(n-i))
# print('*'.rjust(n))

# n=5
# # print('*'.rjust(n))
# for i in  range(n-1,1,-1):
#     print('*'.rjust(i)+'*'.rjust(n-i))
# print('*'*n)



#  check-
# #q25.
# n=5
# print('*'.center(10))
# for i in range(1,n-1):
#     print('*'.rjust(n-i)+' '*(i)+' '.ljust(i)+'*')
# print('*')



# #30.
# n=5
# print(n*'*')
# for i in range(1,n-1):
#     print('*'+' '*(n-2)+'*')
# print(n*'*')


#29.

n=5
# print(n*'*')
for i in range(n):
    print('*'*n)
# print(n*'*')
