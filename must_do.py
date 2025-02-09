# 1. Find the frequency of each character of string without using inbuilt
# methods
# x='asdsadsadsa'
# d={}
# for i in x:
#     d[i]=d.get(i,0)+1
# print(d) 


# 2. Reverse Link List
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None
        
a = Node(4)
b = Node(2)
c = Node(3)
d = Node(1)
e = Node(7)

a.next=b
b.next=c
c.next=d
d.next=e

#print a linked list-
head=a
# while head!=None:
#     print(head.val)
#     head=head.next

def rev_linked_list(head):
    prev=None
    curr=head
    while curr!=None:
        next1= curr.next 
        curr.next=prev
        prev=curr
        curr=next1
    return prev

new_ll=rev_linked_list(a)

print(new_ll)
    
while new_ll!=None:
    print(new_ll.val)
    new_ll=new_ll.next


##diamond pattern
#    *
#   ***
#  *****
# *******   
#  *****
#   ***
#    *
n=int(input('Enter the value of n: '))
for i in range(n):
    print(' '*(n-i)+'*'*i+(i-1)*'*')
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*i+(i-1)*'*')


# 3. Write a Python program to reverse the order of the items in the array.
# Sample Output
# Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# Reverse the order of the items:
# array('i', [3, 9, 1, 7, 3, 5, 3, 1])
arr = [1, 3, 5, 3, 7, 1, 9, 3]
print(arr[::-1])


# 4. Write a program to print the sum of two numbers using variables.
# 5. Write a program to swap two numbers without a third variable.
# 6. Write a program to swap two numbers with a third variable.
# 7. Write a Python program to get the number of occurrences of a specified
# element in an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
# Number of occurrences of the number 3 in the said array: 3

# 8. Write a program to check whether a number is positive, negative or
# zero.
# 9. Write a program to check whether a number is prime or not.
# 10. Write a program to check whether a number is odd or even.
# 11. Write a language program in which accepts the user's first and last
# name and prints them in reverse order with a space between them.
# Sample Output:
# Input First Name: Vineeta
# Input Last Name: Singh
# Name in reverse is: Singh Vineeta
# 12. Write a program to swap first and last digits of any number.
# Sample Output:
# Input any number: 12345
# The number after swapping the first and last digits are: 52341
# 9. Write a program which prints three highest numbers from a list of
# numbers in descending order.
# 10. Write a program to add all the numbers from 1 to a given number

# Sample output:
# Add 1 to 4: 10
# Add 1 to 100: 5050

# 11. Write a program to read an integer n and prints the factorial of n, assume
# that n = 10(n can be any number)

# 12. Write a program to replace all the lower-case letters of a given string
# with the corresponding capital letters

# Sample Output:
# Input String: Vineeta
# Output String: VINEETA

# 13. Write a program to print Fibonacci series without using recursion and
# using recursion.

# 14. Write a program to check palindrome numbers.

# 15. Write a program to check whether a string is palindrome or not.

# 16.Write a program to check Whether a number is Armstrong or not.
# 17. Write a program to print the sum of digits.
# Input: 624
# Output: 12
# 18. Write a program to reverse a given number
# Input: 1 2 3
# Output: 3 2 1
# 19. Write a program to convert decimal numbers to binary.
# Input: 9
# Output: 1001