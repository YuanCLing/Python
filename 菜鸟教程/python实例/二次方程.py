import cmath
a = float(input('输入a：'))
b = float(input('输入b：'))
c = float(input('输入c：'))
d = b**2 - 4*a*c
sol1 = (-b+cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)
print(f'结果是{sol1}和{sol2}')
