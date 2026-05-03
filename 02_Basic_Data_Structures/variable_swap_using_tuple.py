print("Input Variable A")
var_A = str(input())

print("Input Variable B")
var_B = str(input())

print(f'Right now, Variable A : {var_A}')
print(f'Right now, Variable B : {var_B}')

var_A,var_B = var_B,var_A

print('After Swapping.....')
print(f'Variable A : {var_A}')
print(f'Variable B : {var_B}')
