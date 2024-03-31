'''def power_of_2_numbers():
    a=int(input('enter the whole number'))
    b=int(input('enter the power number'))
    a=abs(a)
    b=abs(b)
    s=a**b
    return s

print(f'the power of the 2 numbers are',power_of_2_numbers())
'''
'''def sum_of_series():
    s=0
    n=int(input('enter the limit'))
    for i in range(5,n+1,2):
        s+=(i**2)
    return s
    
print('sumof series is',sum_of_series())

def sides_of_a_triangle():
    a=int(input('enter 1st side of triangle '))
    b=int(input('enter 2nd side '))
    c=int(input('enter the 3rd side '))
    if a or b or c <=0:
        print('invalid side of triangle')
        return "invalid"
    type_of_triangle=''
    if a==b==c:type_of_triangle='the triangle is equilateral'
    elif a!=b!=c:type_of_triangle='scalene triangle'
    else:type_of_triangle='isosceles triangle'
    return type_of_triangle

print('type of triangle:',sides_of_a_triangle())  

def sum_of_digits():
    n=int(input('enter any number'))
    s=0
    while n!=0:
        t=n%10
        s+=t
        n//=10
    return s

print('sum of digits',sum_of_digits())

def reverse_an_integer():
    n=int(input('enter number'))
    ni=0
    while n!=0:
        t=n%10
        ni=(ni*10)+t
        n//=10
    return ni

print('the reversed number ',reverse_an_integer())

def hcf_of_2_numbers():
    a=int(input('enter a number'))
    b=int(input('enter a number'))
    hcf=0
    while b:
        a,b=b,a%b
    return a
hcf=hcf_of_2_numbers()
def lcm_of_2_numbers():
    a=int(input('enter the 1st number again '))
    b=int(input('enter the 2nd number again '))
    return(a*b)//(hcf)
print('the lcm and hcf of the 2 numbers',hcf_of_2_numbers(),lcm_of_2_numbers())

def prime_composite_analyse():
    n=int(input('enter the number to be checked'))
    f=0
    for i in range(2,n):
        if n%i==0:f+=1
    if f==0:return 'prime'
    else: return 'composite number'

print(prime_composite_analyse())

def sum_list():
    l=[]
    for i in range(10):
        n=int(input('enter elements'))
        l+=[n]
    so=se=0
    for i in range(len(l)):
        if i%2==0:
            se+=l[i]
        else:so+=l[i]
    return so,se
print('sum of the odd index and even index is',sum_list())

def freq_of_data():
    l=[]
    for i in range(10):
        n=int(input('enter elements'))
        l+=[n]
    data=int(input('enter data to be searched'))
    i=a=0
    while i<=len(l)-1:
        if l[i]==data: return i
        else:i+=1
    else:return a
a=freq_of_data()
print('data found in data',a+1) if a!=0 else print('notfound')

def sort_search():
    l=[]
    for i in range(10):
        n=int(input('enter elements'))
        l+=[n]
    for i in range(len(l)):
        j=i-1
        m=i
        for j in range(i,len(l)):
            if l[m]>l[j]:m=j
        l[m],l[i]=l[i],l[m]
    data=int(input('enter data to be searched'))
    lb=0
    ub=len(l)-1
    m=(lb+ub)//2
    fd=False
    while lb<=ub and fd==False :
        if l[m]==data:
            fd=True 
            return m+1
        elif l[m]<data: lb=m+1w
        else:ub=m-1
        m=(lb+ub)//2

print('found at index ',sort_search())'''
