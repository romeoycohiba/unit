#class from object oriented series
#code allows us to create employee instances
#it sets


'''
1. Why use classes?
2. What do you mean by a method?
3. Employee class. 
-It is a real life example of an employee who has attributes such
as email address, skin color and actions he can perform. These are attributes
and functions. 
4. How to make an empty class with no attributes and methods?
5. What is the difference between a class and an instance of a class?
6. What is self?

'''
class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@company.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    