# Write a program that determines if a given year is a leap year

print("Enter a year to check if it is a leap year or not")
year = int(input())

if year > 0:
    if year%4==0 and (year%100!=0 or year%400==0) :
        print(f'{year} is a leap year.')

    else:
        print(f'{year} is not a leap year')