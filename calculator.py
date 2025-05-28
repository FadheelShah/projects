# Calculator class
# Methods Add and Subtract // Done
# new methods multiply and devide

from functools import reduce
from operator import mul, sub, truediv
import time


class Calc:

    def add(self, data):
        self.total = sum(data)

        print("numbers: " + str(data))
        print("Total: " + str(self.total))
        time.sleep(2)

    def subtract(self, data):
        if not data:
            print("no input provided")
            return

        self.new_data = data[:]

        # self.total = self.new_data[0] - sum(self.new_data[1:])
        self.total = reduce(sub, self.new_data)

        print("Numbers: " + str(self.new_data))
        print("Total: " + str(self.total))
        time.sleep(2)

    def multiply(self, data):
        if not data:
            print("no input provided")
            return

        self.new_data = data[:]

        self.total = reduce(mul, self.new_data)

        print("Numbers: " + str(self.new_data))
        print("Total: " + str(self.total))
        time.sleep(2)

    def divide(self, data):
        if not data:
            print("no input provided")

            return

        self.new_data = data[:]
        try:

            self.total = reduce(truediv, self.new_data)

            print("Numbers: " + str(self.new_data))
            print("Total: " + str(self.total))
            time.sleep(2)

        except ZeroDivisionError:
            print("Error: Tried to divide by zero.")
            print(self.new_data)
            time.sleep(2)
            return


calculator = Calc()

num = []

while True:
    print("Select a Operation to compute:")
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. divide")

    print()

    choice = input("Select: ")
    print()

    if choice == "1":
        print("Addition")

        while True:
            try:
                inputs = input()

                if inputs == "=":
                    calculator.add(num)
                    num.clear()
                    break

                num.append(float(inputs))

            except ValueError:
                print("Please enter a number: ")
                continue

    elif choice == "2":
        print("Subtraction")

        while True:
            try:
                inputs = input()

                if inputs == "=":
                    calculator.subtract(num)
                    num.clear()

                    break

                num.append(float(inputs))

            except ValueError:
                print("Please enter a number: ")
                continue

    elif choice == "3":
        print("Multiply")

        try:
            while True:
                inputs = input()

                if inputs == "=":
                    # print(reduce(mul, num))
                    calculator.multiply(num)
                    num.clear()

                    break

                num.append(float(inputs))

        except ValueError:
            print("Please enter a number: ")
            continue

    elif choice == "4":
        print("Division")
        try:
            while True:
                inputs = input()

                if inputs == "=":
                    # print(reduce(truediv, num))
                    calculator.divide(num)
                    num.clear()

                num.append(float(inputs))

        except ValueError:
            print("Please enter a number: ")
            continue

    elif choice == "0":
        break
