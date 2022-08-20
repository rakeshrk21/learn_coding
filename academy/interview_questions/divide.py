# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

def divide(divident, divisor):
    flag = True
    count = 0
    rem  = divident
    while(flag):
        divident = rem
        rem = divident - divisor
        count += 1
        if rem < divisor:
            flag = False
            return count
    
print(divide(10,3))
print(divide(25,5))
print(divide(7,-3))
        