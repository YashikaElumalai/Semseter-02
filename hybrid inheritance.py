class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print(f"person name:{self.name}\nperson age:{self.age}")

class stud_ID(person):
    def __init__(self,ID):
        self.ID=ID
    def display_stud_ID(self):
        print(f"stud_ID:{self.ID}")

class employee_EID(person):
    def __init__(self,EID):
        self.EID=EID
    def display_employee_EID(self):
        print(f"employee_EID:{self.EID}")

person1=person("Ria",10)
person1.display_person()
stud_ID1=stud_ID(814)
stud_ID1.display_stud_ID()
employee_EID1=employee_EID(142)
employee_EID1.display_employee_EID()
        

    
