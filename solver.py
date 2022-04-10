import math
import re


def request_complex_num():
    num_type = str(input("Will you provide a complex number in standard form or trigonometric form? Please answer with "
                         "either \"trigonometric\", \"trig\", or \"standard\": ")).lower()
    if num_type == "standard" or num_type == "s":
        return request_standard_form()
    elif num_type == "trigonometric" or num_type == "trig" or num_type == "t":
        return request_trig_form()
    else:
        return request_complex_num()


def request_standard_form():
    complex_num = str(input("Please provide the complex number in standard form: "))
    if not re.fullmatch("\(-?((\d+)|(\d*.\d+))[+-]((\d+i)|(\d*.\d+i))\)\^((\d+)|(\d*.\d+))", complex_num)\
            and not re.fullmatch("-?((\d+)|(\d*.\d+))[+-]((\d*i)|(\d*.\d+i))", complex_num):
        # print(re.fullmatch("-?((\d+)|(\d*.\d+))[+-]((\d+i)|(\d*.\d+i))", complex_num))
        print("Please use valid standard form.")
        complex_num = request_standard_form()
        return complex_num
    else:
        return complex_num


def request_trig_form():
    trig_num = str(input("Please provide the complex number in trigonometric form, with a power: "))
    if not re.fullmatch("\(\d+\(cos\(\d+\)[+-]sin\(\d+\)\)\^\d+", trig_num):
        print("Please use the form of (num(cos(theta)+-sin(theta))^power.")
        trig_num = request_trig_form()
        return trig_num
    else:
        return trig_num


def is_num_negative(num):
    if num < 0:
        return "-"
    else:
        return "+"


complexNum = request_complex_num()

operatorLocation = complexNum.find("+") if complexNum.find("-", 2) == -1 else complexNum.find("-", 2)
a = float(complexNum[1:operatorLocation]) if complexNum.find("(") != -1 else float(complexNum[:operatorLocation])
b = float(complexNum[operatorLocation:complexNum.find("i")]) if complexNum[operatorLocation+1] != "i" else 1.0
n = 1.0 if complexNum.find("^") == -1 else float(complexNum[complexNum.find("^") + 1:])
# print(f"a is {a}, b is {b}, power is {n}")


m = math.sqrt(a**2+b**2)
theta_rad = math.atan(b/a) if a > 0 else 0.0 if a == 0 else math.atan((b/a)+180)
theta = math.degrees(theta_rad)

# print(theta_rad*n)

if n == 1:
    print(f"Trig form is {m}(cos({theta})+isin({theta})).")

else:
    print(f"Trig form is {m ** n:.5f}(cos({n * theta:.5f})+isin({n * theta:.5f}).\nStandard form simplified is "
          f"{(m ** n) * (math.cos(n * theta_rad)):.5f}"
          f"{is_num_negative((m ** n) * (math.sin(n * theta_rad)))}i*{abs((m ** n) * (math.sin(n * theta_rad))):.5f}")
