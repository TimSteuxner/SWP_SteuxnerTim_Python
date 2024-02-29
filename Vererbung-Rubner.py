class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Employee(Person):
    def __init__(self, name, gender, department):
        super().__init__(name, gender)
        self.department = department

class Manager(Employee):
    pass 

class Company:
    def __init__(self):
        self.employees = []
        self.departments = []
        self.Manager = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def employeeCount(self):
        return len(self.employees)

    def addManager(self, manager):
        man_deps = [i.department for i in self.Manager]
        if manager.department not in man_deps:
            self.Manager.append(manager)    
        else:
            print("Gibt schon einen Manager mit diesem Department")
    
    def totalEmployees(self):
        return len(self.employees)

    def totalManagers(self):
        return sum(1 for manager in self.Manager if isinstance(manager, Manager))

    def totalDepartments(self):
        return len(set(employee.department for employee in self.employees ))

    def genderPercentage(self):
        total_employees = self.totalEmployees()

        total_men = sum(1 for employee in self.employees if employee.gender == "Male")
        total_women = total_employees - total_men

        return (total_women / total_employees) * 100, (total_men / total_employees) * 100
    

if __name__ == "__main__":  
    manager = Manager("Florian", "Male", "IT")  
    manager2 = Manager("Klemens", "Male", "IT" )
    employee1 = Employee("Max", "Male", "HR")
    employee2 = Employee("Luca", "Female", "IT")
    employee3 = Employee("Henry", "Male", "HR")

   
    company1 = Company()
    
    company1.addManager(manager) 
    company1.addManager(manager2) 
    company1.addEmployee(employee1)
    company1.addEmployee(employee2)
    company1.addEmployee(employee3)
    

    print("Statistik: Firma")
    print("Gesamtanzahl Mitarbeiter:", company1.totalEmployees())
    print("Gesamtanzahl Abteilungsleiter:", company1.totalManagers())
    print("Gesamtanzahl Abteilungen:", company1.totalDepartments())
    womenPercentage, menPercentage = company1.genderPercentage()
    print("Prozentanteil Frauen:", womenPercentage, "%")
    print("Prozentanteil Männer:", menPercentage, "%")
   
