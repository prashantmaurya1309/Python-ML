# print('hello world')
# name=input('what is your name:\n')
# print('hi,%s'%name)
# last=input('ur surname:')
# print('%s' %last)

# x=int(input('enter integer:'))
# y=float(input('enter a float:'))
# print(x+y)

# r=float(input('enter a radius of circle:'))
# print('area:',3.14*r**2)
# print('perimeter:',2*3.14*r)
# s=float(input('enter side:'))
# print('primeter:',4*s)


# swaping
# x=int(input())
# y=int(input())
# x=x+y
# y=x-y
# x=x-y
# print(x,y)

# a=int(input('enter a number:'))
# if a%2==0:
#     print('even')
# else:
#     print('odd')

# sum=0
# for i in range(1,5):
#     sum+=i
#
# print(sum)
#
# lst=[23,45,7]
# sum=0
# for i in lst:
#     sum+=i
# print(sum)
#
#
# #while
# sum=0
# i=0
# while i<10:
#     sum+=i
#     i+=1
#
# print(sum)


# for i in 'apple':
#     if i == 'l':
#         break
#     else:
#         print(i)

# year = int(input('year:'))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} is a leap year".format(year))
#        else:
#            print("{0} is not a leap year".format(year))
#    else:
#        print("{0} is a leap year".format(year))
# else:
#    print("{0} is not a leap year".format(year))

x=int(input('enter x'))
y=int(input('enter y'))
if x > y:
        smaller = y
else:
        smaller = x
for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i
print('hcf:',hcf)