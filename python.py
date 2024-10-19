Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
n1,n2=10,20
g=n1 if n1>n2 else n2
print("greater numbers among",n1,"and",n2,"is",g)
greater numbers among 10 and 20 is 20
n1,n2,n3=10,20,30
g=n1 if (n1>n2 and n1>n3) else (n2 if(n2>n3))
SyntaxError: expected 'else' after 'if' expression
g=n1 if (n1>n2 and n1>n3) else (n2 if (n2>n3) else n3)
print("greater of",n1, "and",n2,"and",n3,"is"g)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("greater of",n1,"and",n2,"and",n3,"is",g)
greater of 10 and 20 and 30 is 30
print((bin(10)))
0b1010
print((bin(12)))
0b1100
print((hex(10)))
0xa
print((bin(10|12)))
0b1110
print((bin(~10)))
-0b1011
print(bin(4))
0b100
>>> print(bin(4>>))
SyntaxError: invalid syntax
>>> print(bin(4>>19))
0b0
>>> n=300
>>> m=n
>>> id(n)
4347468144
>>> id(m)
4347468144
>>> m=400
>>> id(m)
4347461712
>>> a=10
>>> b=10
>>> print(a is b)
True
>>> print(id(a), id(b))
4361446032 4361446032
>>> str1="hello"
>>> str2="hello"
>>> print(str1 is str2)
True
>>> print(id(str1), id(str2))
4342127936 4342127936
>>> x="its is raining today"
>>> print('r' in x)
True
>>> print('d' in x)
True
>>> print('python' in x)
False






>>> print('today' in x)
True
>>> print('Today' in x)
False







