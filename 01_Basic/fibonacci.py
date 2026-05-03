# Develop a program that prints out the fibonacci sequence up to a specified number

print('Enter number upto which fibonacci sequence is to be printed')
max_num = int(input())

if max_num>0:
    num1,num2 = 0,1

    print(num1)
    print(num2)


    while(num2<=max_num):
        print(num2)
        num1 = num2
        num2+=num1