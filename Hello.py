Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
l=32
b=42
print(2*(l+b))
148
print(l*b)
1344
p=18
r=10
t=2
print((p*r*t)/100)
3.6
a=22
b=88
c=44
print((a+b+c)/3)
51.333333333333336
l=33
w=55
h=44
print(2((l*w)+(w*h)+(l*h)))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(2((l*w)+(w*h)+(l*h)))
TypeError: 'int' object is not callable
print(2*((l*w)+(w*h)+(l*h)))
11374
r=56
print(3.14*(r*r))
9847.04
r=88
print((4/3)*(3.14)*(r*r*r))
2853096.1066666665

\
n1,n2,n3=10,20,30
avg=20
print("Average of %i %i and %i is %f "%(n1,n2,n3,avg))
Average of 10 20 and 30 is 20.000000 
name="Sanchita"
print("hi %s" % name)
hi Sanchita
print("hi (%20s)" % name)
hi (            Sanchita)
print("hi %20s" % name)
hi             Sanchita
print("hi (%-20s)" % name)
hi (Sanchita            )
print("hi %c, %c" % (name[0],name[1]))
hi S, a
num=123.456789
>>> print('the value is %f' %num)
the value is 123.456789
>>> print("%o"%(16))
20
>>> print('the value is %.2f' %num)
the value is 123.46
>>> n1,n2,n3,n4=10,20,30,40
>>> print("num1={10},num2={1},num3={2},num4={3}".format(n1,n2,n3,n4))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print("num1={10},num2={1},num3={2},num4={3}".format(n1,n2,n3,n4))
IndexError: Replacement index 10 out of range for positional args tuple
>>> print('num1={one}, num2={zero}, num3={two}'.format(zero=n1,one=n2,two=n3))
num1=20, num2=10, num3=30
>>> print('num1={}, num2={}, num3{}'.format(n1,n2,n3))
num1=10, num2=20, num330
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> \
...   n
SyntaxError: unexpected indent
>>> n4=45.5678
>>> print('num={:.2f}'.format(n4))
num=45.57
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
