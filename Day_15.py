# Day 15: Simple Employee Manager App

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def describe(self):
        return f"{self.name} - {self.position} - ${self.salary}"

class DataAnalysis:
    def __init__(self, employees):
        self.employees = employees

    def show_all(self):
        print("\nAll Employees:")
        for emp in self.employees:
            print(emp.describe())

    def average_salary(self):
        if not self.employees:
            print("No employees.")
            return
        avg = sum(emp.salary for emp in self.employees) / len(self.employees)
        print(f"Average Salary: ${avg:.2f}")

class ManagerAnalysis(DataAnalysis):
    def show_managers(self):
        print("\nManagers:")
        found = False
        for emp in self.employees:
            if "manager" in emp.position.lower():
                print(emp.describe())
                found = True
        if not found:
            print("No managers found.")

def main():
    employees = [
        Employee("Alice", "Manager", 70000),
        Employee("Bob", "Developer", 50000),
        Employee("Carol", "Designer", 55000)
    ]
    analysis = ManagerAnalysis(employees)

    while True:
        print("\nMenu:")
        print("1. Show all employees")
        print("2. Add employee")
        print("3. Show average salary")
        print("4. Show managers")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            analysis.show_all()
        elif choice == '2':
            name = input("Name: ")
            position = input("Position: ")
            try:
                salary = float(input("Salary: "))
            except ValueError:
                print("Invalid salary.")
                continue
            employees.append(Employee(name, position, salary))
            print("Employee added.")
        elif choice == '3':
            analysis.average_salary()
        elif choice == '4':
            analysis.show_managers()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()