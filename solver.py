import math
import re

#(\^\d+)|(\^\d*.\d+)

def request_complex_num():
    complex_num = str(input("Please provide the complex number in standard form, including a power: "))
    if not re.fullmatch("[(](\d+)|(\d*.\d+)[+-](\d+i\))|(\d*.\d+i\))\^", complex_num):
        print("Please use valid standard form.")
        request_complex_num()
    else:
        return complex_num


complexNum = request_complex_num()

operatorLocation = complexNum.find("+") if complexNum.find("-") == -1 else complexNum.find("-")
a = float(complexNum[1:operatorLocation])
b = float(complexNum[operatorLocation:complexNum.find("i")])
#power = float(complexNum[complexNum.find("^")+1:])
#print(power)


m = math.sqrt(a**2+b**2)
theta = math.atan(b/a) if a > 0 else math.atan((b/a)+180)


