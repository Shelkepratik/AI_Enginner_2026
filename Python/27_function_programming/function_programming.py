from functools import reduce
nums=[3,2,6,8,4,6,2,9]

fun1=lambda x,y:x+y
print(fun1(2,3))

evens=list(filter(lambda n:n%2==0,nums))

double=list(map(lambda x:x*2,evens))

print(evens)

print(double)

num=reduce(lambda a,b:a+b,double)

print(num)