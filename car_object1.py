class Car:
    #attributes --> Variables
    color : str
    #behaviour --> Methods
    def config(self):
        print("There is a Diesel Machine")


# Creating an instance of the object
BMW = Car()
# Accessing methods
BMW.config()

# Attribute error: When dunder init is not used and also user has not defined it yet.
    #Try Omitting line below
BMW.color = "Silver"
print(BMW.color)
