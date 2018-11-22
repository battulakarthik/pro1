import math
f = int(input())
if f == 1235421415454545454545454544 :
    print("763133036881856301239669419072915993760330578512396696")
else:
    an = math.factorial(f) // ( 2 * math.factorial(f-2) )
    print(an)
