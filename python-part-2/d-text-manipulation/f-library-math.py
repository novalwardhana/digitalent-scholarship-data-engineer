import math

# Fungsi math ceil
print(">>> Fungsi math ceil()")
x = 10.32
y = 12.97
z = 123.212
print("x ceil: ", math.ceil(x))
print("y ceil: ", math.ceil(y))
print("z ceil: ", math.ceil(z), "\n---------------\n")

# Fungsi math floor
print(">>> Fungsi math floor()")
x = 10.32
y = 12.97
z = 123.212
print("x floor: ", math.floor(x))
print("y floor: ", math.floor(y))
print("z floor: ", math.floor(z), "\n---------------\n")

# Fungsi math fabs
print(">>> Fungsi math fabs()")
x = 10.32
y = -12.97
z = 123.212
print("x fabs: ", math.fabs(x))
print("y fabs: ", math.fabs(y))
print("z fabs: ", math.fabs(z), "\n---------------\n")

# Fungsi factorial
print(">>> fungsi math factorial()")
x = 5
y = 12
z = 38
xFactorial = math.factorial(x)
yFactorial = math.factorial(y)
zFactorial = math.factorial(z)
print("x factorial: ", xFactorial)
print("y factorial: ", yFactorial)
print("z factorial: ", zFactorial, "\n--------------\n")

# Fungsi sum
print(">>> Fungsi math fsum()")
x = [1, 2, 3, 4, 5, 6, -6, -5, -4]
y = [8, 2, 5, 8, 9, 12, 15, 2, 9, 11]
z = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
xSum = math.fsum(x)
ySum = math.fsum(y)
zSum = math.fsum(z)
print("x sum: ", xSum)
print("y sum: ", ySum)
print("z sum: ", zSum, "\n---------------\n")

# Fungsi math log
print("Fungsi math log()")
x = math.log(8, 2)
y = math.log(16, 4)
z = math.log(256, 16)
print("Log basis 2 dari 8: ", x)
print("Log basis 4 dari 16: ", y)
print("Log basis 16 dari 256", z, "\n---------------\n")

# Fungsi math sqrt
print(">>> Fungsi math sqrt()")
x = 256
y = 121
z = 75
xSqrt = math.sqrt(x)
ySqrt = math.sqrt(y)
zSqrt = math.sqrt(z)
print("Akar dari ", x ," adalah ", xSqrt)
print("Akar dari ", y, " adalah ", ySqrt)
print("Akar dari ", z, " adalah ", zSqrt, "\n---------------\n")

# Fungsi math copysign
print(">>> Fungsi math copysign")
x = 10.32
y = -13.87
z = -15
x = math.copysign(x, y)
y = math.copysign(y, z)
z = math.copysign(z, 9)
print("x copysign: ", x)
print("y copysign: ", y)
print("z copysign: ", z)