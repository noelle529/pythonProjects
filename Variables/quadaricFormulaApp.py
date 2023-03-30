import cmath

a = 2.0
b = -7.0
c = 4.0

root1 = 0.0
root2 = 0.0

#root1 = float((-b + (b*b - 4*a*c).sqrt()) / (2*a) )
root1 = (-b+cmath.sqrt(b*b - 4*a*c)) / (2*a)
root2 = (-b-cmath.sqrt(b*b - 4*a*c)) / (2*a)
#root2 = float((-b - (b*b - 4*a*c).sqrt()) / (2*a) )

print(root1)
print(root2)