class employee:
    def __init__(self, emid, name, salary, address):
        self.emid = emid
        self.name = name
        self.salary = salary
        self.address = address

    def show(self):
        print("Employee id:",self.emid)
        print("Employee name:",self.name)
        print("Employee salary:",self.salary)
        print("Employee address:",self.address)



class teacher(employee):
    def __init__(self, department, subject = []):
        super().__init__(emid,name,salary,address)
        self.department = department
        self.subject = subject
        

    def show(self):
        super().show()
        print("Department:",self.department)
        print("Subject:",self.subject)

emid = int(input("enter eployee id"))
name = input("enter employee name")
salary = float(input("enter salary"))
address = input("enter your address")
department = input("enter ur department")
subject = (input("enter subject you taught")).split(" ")


ob2 = teacher(department,subject)

ob2.show()
