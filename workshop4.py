
# For this assignment, you will write "driver code" for each task. Driver code is not a part of your application but is used to test parts of your application.
# Write this driver code in the same file (workshop4.py), but keep it at the bottom of the file, separated from the rest of your code.
# Add a comment above your driver code to separate it from the rest of your code, similar to this:
#     """ Driver Code for Task 1 """
# Then write your driver code for Task 1 underneath this comment.
# For your driver code:
# Write code to instantiate an object from the User class, providing the name, pin, and password as arguments.
# For example, you could use "Bob" as the name, 1234 as the pin, and "password" as the password. 
# Write a print statement to print the name, pin, and password attributes of this object. 


# Write three methods for the User class:
# change_name() - Changes the name of the User.
# change_pin() - Changes the PIN of the User.
# change_password() - Changes the password of the User.
class User:
    #Class Properties
    def __init__(self, name, pin, password):
        self.name = name
        self.password = password
        self.pin = pin

    #Class Methods
    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password


#INSTANTIATION OF User CLASS
bankUser1 = User("Bob", 1234, "password")
# Test Task 2
# Below the commented-out driver code for Task 1, add the driver code for Task 2.
# You can add a comment such as:
#     """ Driver Code for Task 2 """
# ...then write your driver code under this comment.
# For your driver code:
# Once again, instantiate an object from the User class, providing the name, pin, and password as arguments.
# These can be the same code and arguments as in Task 1. For example, the arguments: "Bob", 1234, "password".
# Again, print the object's attributes. 
# Call each of the three methods you created to change the name, pin, and password. 
# Print the updated attributes. 
# Save your changes and run the updated code.


bankUser1.change_name("Jane")
bankUser1.change_pin(456)
bankUser1.change_password("new password")

#Driver Code, Task 2
print(bankUser1.name, bankUser1.pin, bankUser1.password)





#Driver Code, Task 1
# print(bankUser1.name, bankUser1.pin, bankUser1.password)