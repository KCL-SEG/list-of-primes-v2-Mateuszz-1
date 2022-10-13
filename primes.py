"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import os

def primes(number_of_primes):
    noError = False
    while noError == False:
        try:
            if type(number_of_primes) is not int:
                raise ValueError
            if number_of_primes < 1:
                raise ValueError
            list = []
            num = 2
            while len(list) != number_of_primes:
                successfulDivisions = 0
                for i in range(1, num+1):
                    if (num%i) == 0:
                        successfulDivisions += 1
                if successfulDivisions == 2:
                    list.append(num)
                num += 1
            noError = True
            return list
        except:
            if (os.name == "nt"):
                os.system("cls")
            else:
                os.system("clear")
            print("An error occured. Please note you can only enter a whole number greater than 0.")
            number_of_primes = int(input("How many prime numbers would you like to view: "))
