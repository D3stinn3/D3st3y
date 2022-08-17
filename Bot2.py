"""object oriented programming"""
from time import time

start = time()

class Student:

    def __init__(self, name, age, grade):

        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):

        return self.grade

class Course:

    def __init__(self, name, max_students):

        self.name = name
        self.max_students = max_students
        self.students = []
        self.special_students = []

    def add_student(self, student):

        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def special_case(self):

        while True:

            if self.name != 'Destinne':
                return f'{self.name}'

            else:
                
                self.special_students.append(self.name)
                return self.special_students

    def get_average_grade(self):

        value = 0

        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student('Tim', 19, 95)
s2 = Student('Destinne', 26, 10)
s3 = Student('Sam', 2, 100)

course = Course('Python', 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_average_grade())
print(course.special_case())


class Account:

    num_of_transactions = 0

    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance
        Account.trans_instance()

    def deposit(self):

        dep_amount = int(input('Tafadhali Weka Kiwango Cha Kuwekeza: '))
        self.balance += dep_amount
        print('Wekezo Kamili!')
        Account.trans_instance() # this is the instance of a transac defined by the object class Account via the trans_instance method

    def withdraw(self):

        wit_amount = int(input('Tafadhali Weka Kiwango Cha Kutoa: '))
        
        if self.balance > wit_amount:
            self.balance -= wit_amount
            print('Process Ya Kutoa Yakamilika! ' + ' Mabaki: ' + f'{0}'.format(self.balance))

        else:
            print('Process Ya Kutoa Yasitishwa')

        Account.trans_instance()

    def show_balance(self):

        Account.trans_instance()
        return self.balance

    @classmethod
    def trans(num_of_transac): # this is an instance of a class!
        return num_of_transac.num_of_transactions


    @classmethod
    def trans_instance(num_of_transac): # this defines the instance of the class!
        num_of_transac.num_of_transactions += 1

    def trans_count(self):

        total_transac = Account.trans_instance()

        for one_transac in range(int(total_transac)):

            if one_transac < 6:

                print('this is a good zone!')

            else:
                print('this beyond transac count')

                break

"""both must exist to harmonize the instance of the class through arguments"""



first_acc = Account('Destinne', 1000)
second_acc = Account('Maria', 1000)
first_acc.deposit()
second_acc.deposit()
first_acc.withdraw()
second_acc.withdraw()
first_acc.trans_count()

print(Account.trans())


"""the main object orinted programming project objective"""

"""polymorphism in object oriented programming"""

class GrandFather:

    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name

class Father(GrandFather):
    def __init__(self, father_name, grandfather_name):
        self.father_name = father_name

        GrandFather.__init__(self, grandfather_name)

class Child(Father):
    def __init__(self, child_name, father_name, grandfather_name):
        self.child_name = child_name

        self.names = []
        self.phone_numbers = []

        Father.__init__(self, father_name, grandfather_name)

    def gen(self):

        print('Grand Father Name registered is ', self.grandfather_name)
        print('Father Name registered is ', self.father_name)
        print('Child Name registered is ', self.child_name)

        self.names.append(self.grandfather_name)
        self.names.append(self.father_name)
        self.names.append(self.child_name)
        sorted_list = sorted(self.names)
        print(sorted_list)

        for name in self.names:

            phone_number = input(f'Please enter phone number for {name} : ')
            self.phone_numbers.append(phone_number)
            print(self.phone_numbers)



# information unlocks at certain age
# only yhr parents can input the child
# after death memories are written
# no access to another family tree for anyone in distinct family trees
# 80 per cent should validate entry to new family tree

obj = Child('Destinne', 'Albert', 'Salesio')

print(f'The head is : {obj.grandfather_name}')

obj.gen()

end = time()

exec_time = end - start

print(f'Execution time is: {exec_time} seconds')






