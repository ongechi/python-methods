
# python-methods

Python is a wonderful language but it can be daunting for a newcomer to master. Like any spoken language, Python requires us to
first understand the basics before we can jump to building more diverse and broader applications in the data science field.
Python is of course an Object-Oriented Programming (OOP) language. This is a wide concept and is not quite possible to grasp all at once.
In fact, mastering OOP can take several months or even years. It totally depends upon your understanding capability.
I highly recommend going through my previous article on the ‘Basic concepts of Object-Oriented Programming‘ first.
So in this particular article, I’ll expand the concept of methods in Object-Oriented Programming further.
We’ll talk about the different types of Methods in Python. Since python Methods can be confusing sometimes if you are new to OOP,
I’ll cover methods in Python and their types in detail in this article. And then we’ll see the use cases of these methods.

What are Methods in Python?
Python offers various types of these methods. These are crucial to becoming an efficient programmer and consequently are useful for a data science professional.

 

Types of Methods in Python

There are basically three types of methods in Python:

Instance Method
Class Method
Static Method
Let’s talk about each method in detail.

 

Instance Methods
The purpose of instance methods is to set or get details about instances (objects), and that is why they’re known as instance methods.
They are the most common type of methods used in a Python class.

They have one default parameter- self, which points to an instance of the class. Although you don’t have to pass that every time.
You can change the name of this parameter but it is better to stick to the convention i.e self.

Class Methods
The purpose of the class methods is to set or get the details (status) of the class. That is why they are known as class methods. 
They can’t access or modify specific instance data. They are bound to the class instead of their objects. Two important things about class methods:
In order to define a class method, you have to specify that it is a class method with the help of the @classmethod decorator
Class methods also take one default parameter- cls, which points to the class. Again, this not mandatory to name the default parameter “cls”.
But it is always better to go with the conventions

Static Methods
Static methods cannot access the class data. In other words, they do not need to access the class data.
They are self-sufficient and can work on their own.  Since they are not attached to any class attribute, 
they cannot get or set the instance state or class state.
In order to define a static method, we can use the @staticmethod decorator (in a similar way we used @classmethod decorator).
Unlike instance methods and class methods, we do not need to pass any special or default parameters.


