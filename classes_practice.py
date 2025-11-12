'''class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name          # Instance attribute
        self.age = age            # Instance attribute

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing class attribute
print(Dog.species)     # ✅ "Canis familiaris"
print(dog1.species)    # ✅ "Canis familiaris"

# Accessing instance attribute
print(dog1.name)       # ✅ "Buddy"
print(dog2.name)       # ✅ "Max"
print(Dog.name)        # ❌ Error
dog1.species = "Wolf"  # Creates a new instance attribute
print(dog1.species)    # "Wolf"
print(dog2.species)    # "Canis familiaris"
print(Dog.species)     # "Canis familiaris"'''
'''class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, rupees):
        self.amount += rupees
        print(f"{self.name} deposited {rupees}. New balance: {self.amount}")

    def withdraw(self, rupees):
        if rupees <= self.amount:
            self.amount -= rupees
            print(f"{self.name} withdrew {rupees}. New balance: {self.amount}")
        else:
            print("Insufficient funds!!")

    def display(self):
        print(f"Hi {self.name}, your current balance is ₹{self.amount}")
account1 = BankAccount("Alice", 1000)
account1.display()          # Hi Alice, your current balance is ₹1000       
account1.deposit(500)      # Alice deposited 500. New balance: 1500
account1.withdraw(200)     # Alice withdrew 200. New balance: 1300
'''
