class Employee:
    """
    Employee class representing an employee.
    """

    def __init__(
        self,
        employee_id,
        name,
        department,
        experience_years,
        education_level,
        age,
        gender,
        city,
        monthly_salary
    ):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.experience_years = experience_years
        self.education_level = education_level
        self.age = age
        self.gender = gender
        self.city = city
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        """
        Calculate annual salary.
        """
        return self.monthly_salary * 12

    def experience_level(self):
        """
        Categorize employee based on experience.
        """

        if self.experience_years <= 2:
            return "Junior"

        elif self.experience_years <= 7:
            return "Mid-Level"

        else:
            return "Senior"

    def display(self):
        """
        Display employee information.
        """

        print("=" * 50)

        print(f"Employee ID       : {self.employee_id}")
        print(f"Name              : {self.name}")
        print(f"Department        : {self.department}")
        print(f"Experience        : {self.experience_years} years")
        print(f"Education         : {self.education_level}")
        print(f"Age               : {self.age}")
        print(f"Gender            : {self.gender}")
        print(f"City              : {self.city}")
        print(f"Monthly Salary    : ₹{self.monthly_salary:,.2f}")
        print(f"Annual Salary     : ₹{self.annual_salary():,.2f}")
        print(f"Experience Level  : {self.experience_level()}")

        print("=" * 50)