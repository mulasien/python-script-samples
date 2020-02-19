"""
Think of classes as the blueprint of creating many individual versions of a 'thing'
"""
# import our Tire class from the separate tire.py file
from tire import Tire


class Car:
    """
    Car models a car w/ tires and an engine
  """

    # __init__ is the 'thing' that happens when a class is invoked
    def __init__(self, engine, tires):  # functions inside of classes are 'methods'
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires.")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].wheel_circumference()
        else:
            return 0


# example usage
civic = Car(
    "4-cylinder", ["front driver", "front passenger", "rear driver", "rear passenger"]
)

# print(civic.engine)  # will print 4-cylinder
# print(civic.tires)  # will print the tires list
# print(civic.description)  # will print the formatted string from the description method

# # # testing calling on Tires class with a honda
# tire = Tire("P", 205, 55, 15)  # set Tire class parameters from tire.py
# tires = [
#     tire,
#     tire,
#     tire,
#     tire,
# ]  # set 4 tires with above paremeters to our list of 4 tires
# honda = Car(tires=tires, engine="4-cylinder")
# #  # setting Car class parameters, notice we are assigning argument values directly
# # This time, the honda has more details provider about the tires based on info from the Tires class

