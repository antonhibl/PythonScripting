# Bitwise Calculator Program
# author: Anton Hibl

# Import libraries
from ctypes import c_uint8 as uint_8

# Take User inputs
# Input A
input_a = int(input("Enter value A: "))

# Input B
input_b = int(input("Enter value B: "))

# Convert to binary Fucntion
def binConvert(input_val):
    binary_form = f"{uint_8( input_val ).value:08b}"
    return binary_form


# Convert to decimal function
def decConvert(input_val1, input_val2):
    decimal_form = input_val1 >> input_val2
    return decimal_form


# Convert to hexadecimal function
def hexConvert(inputdecimal):
    hex_form = hex(inputdecimal).lstrip("0x")
    if inputdecimal < 0:
        hex_form = hex(inputdecimal).lstrip("-0x")
        return hex_form
    else:
        return hex_form


# Perform Calculations
# Print Title
print("Operation   Decimal   Binary    Hexadecimal")
# A AND B
AandB = input_a & input_b
print(f"A & B    =    {AandB}      {binConvert(AandB)}      {hexConvert(AandB)}")

# A OR B
AorB = input_a | input_b
print(f"A | B    =    {AorB}      {binConvert(AorB)}      {hexConvert(AorB)}")

# A XOR B
AxorB = input_a ^ input_b
print(f"A ^ B    =    {AxorB}      {binConvert(AxorB)}      {hexConvert(AxorB)}")

# Compliment of A
complimentA = ~input_a
print(
    f"~A       =    {complimentA}      {binConvert(complimentA)}      -{hexConvert(complimentA)}"
)

# A Right Shift by B
aright = input_a >> input_b
print(f"A >> B   =    {aright}      {binConvert(aright)}      {hexConvert(aright)}")

# A Left Shift by B
aleft = input_a << input_b
print(f"A << B   =    {aleft}      {binConvert(aleft)}      {hexConvert(aleft)}")
