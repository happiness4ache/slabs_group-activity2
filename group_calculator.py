# Authors: Ndivhuwo, Lehlogonolo, Nthabiseng, Lemuel and Bontle 

"""
This program group demonstrates dynamic variables and arithmetic operations of addition, division, integer division
, Modulus.
"""

# This is number 1 it's an integer that ask for user input
Num_1 = int(input("enter the first number: "))

# This is number 2 it's an integer that ask for user input
Num_2 = int(input("enter the second number: "))

# This variable asks for the group name
group_name = input("what is your group name: ")


Add = Num_1 + Num_2 # Addition of Num_1 and Num_2
Divide = Num_1 / Num_2  # Divide of Num_1 and Num_2
Integer_division = Num_1 // Num_2  # Integer_division of Num_1 and Num_2
Modulus = Num_1 % Num_2  # Modulus of Num_1 and Num_2

# This prints the output or results of the arithmetic operations and the group name
print("Your group name is", group_name)
print("Addition :", Num_1 , " + " , Num_2, " = ", Add, ", Type ", type(Add) )
print("Divide :", Num_1 , " / " , Num_2, " = ", Divide, ". Type ", type(Divide) )
print("Integer_division :", Num_1 , " // " , Num_2, " = ", Integer_division, ". Type ", type(Integer_division) )
print("Modulus :", Num_1 , " % " , Num_2, " = ", Modulus, ", Type ", type(Modulus) )

