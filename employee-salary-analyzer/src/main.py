import os

from data_manager import (
    load_data,
    clean_data,
    display_data,
    dataset_info,
    create_employee_objects
)

from analyzer import (
    display_salary_statistics,
    display_experience_statistics,
    display_age_statistics,
    highest_paid_employee,
    lowest_paid_employee,
    department_analysis,
    education_analysis,
    gender_analysis,
    city_analysis,
    search_employee,
    salary_by_experience,
    annual_salary_column
)

from visualization import (
    salary_bar_chart,
    department_salary_chart,
    salary_distribution_chart,
    department_distribution_chart
)


# ==================================================
# PROJECT PATHS
# ==================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_FILE = os.path.join(
    BASE_DIR,
    "data",
    "employee.csv"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output"
)


# ==================================================
# CREATE OUTPUT DIRECTORY
# ==================================================

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


# ==================================================
# LOAD DATA
# ==================================================

df = load_data(DATA_FILE)

df = clean_data(df)


# ==================================================
# MENU
# ==================================================

def show_menu():

    print("\n")

    print("=" * 60)
    print("          EMPLOYEE SALARY ANALYZER")
    print("=" * 60)

    print("1.  Display Employees")
    print("2.  Dataset Information")
    print("3.  Salary Statistics")
    print("4.  Experience Statistics")
    print("5.  Age Statistics")
    print("6.  Highest Paid Employee")
    print("7.  Lowest Paid Employee")
    print("8.  Department Analysis")
    print("9.  Education Analysis")
    print("10. Gender Analysis")
    print("11. City Analysis")
    print("12. Search Employee")
    print("13. Salary by Experience")
    print("14. Generate Charts")
    print("15. Show Employee Object")
    print("16. Exit")

    print("=" * 60)


# ==================================================
# DISPLAY EMPLOYEE
# ==================================================

def display_employee_details(employee):

    print("\nHighest/Selected Employee")
    print("=" * 50)

    print(
        f"Employee ID      : {employee['EmployeeID']}"
    )

    print(
        f"Name             : {employee['Name']}"
    )

    print(
        f"Department       : {employee['Department']}"
    )

    print(
        f"Experience       : "
        f"{employee['Experience_Years']} years"
    )

    print(
        f"Education        : "
        f"{employee['Education_Level']}"
    )

    print(
        f"Age              : {employee['Age']}"
    )

    print(
        f"Gender           : {employee['Gender']}"
    )

    print(
        f"City             : {employee['City']}"
    )

    print(
        f"Monthly Salary   : "
        f"₹{employee['Monthly_Salary']:,.2f}"
    )

    print(
        f"Annual Salary    : "
        f"₹{employee['Monthly_Salary'] * 12:,.2f}"
    )

    print("=" * 50)


# ==================================================
# MAIN PROGRAM
# ==================================================

def main():

    if df.empty:

        print(
            "Dataset could not be loaded."
        )

        return

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()


        # ==========================================
        # 1. DISPLAY DATA
        # ==========================================

        if choice == "1":

            display_data(df)


        # ==========================================
        # 2. DATASET INFORMATION
        # ==========================================

        elif choice == "2":

            dataset_info(df)


        # ==========================================
        # 3. SALARY STATISTICS
        # ==========================================

        elif choice == "3":

            display_salary_statistics(df)


        # ==========================================
        # 4. EXPERIENCE STATISTICS
        # ==========================================

        elif choice == "4":

            display_experience_statistics(df)


        # ==========================================
        # 5. AGE STATISTICS
        # ==========================================

        elif choice == "5":

            display_age_statistics(df)


        # ==========================================
        # 6. HIGHEST PAID
        # ==========================================

        elif choice == "6":

            employee = highest_paid_employee(df)

            display_employee_details(
                employee
            )


        # ==========================================
        # 7. LOWEST PAID
        # ==========================================

        elif choice == "7":

            employee = lowest_paid_employee(df)

            display_employee_details(
                employee
            )


        # ==========================================
        # 8. DEPARTMENT ANALYSIS
        # ==========================================

        elif choice == "8":

            print("\nDepartment Analysis")

            print("=" * 70)

            result = department_analysis(df)

            print(
                result.to_string()
            )


        # ==========================================
        # 9. EDUCATION ANALYSIS
        # ==========================================

        elif choice == "9":

            print("\nEducation Analysis")

            print("=" * 50)

            result = education_analysis(df)

            print(result)


        # ==========================================
        # 10. GENDER ANALYSIS
        # ==========================================

        elif choice == "10":

            print("\nGender Analysis")

            print("=" * 50)

            result = gender_analysis(df)

            print(result)


        # ==========================================
        # 11. CITY ANALYSIS
        # ==========================================

        elif choice == "11":

            print("\nCity Analysis")

            print("=" * 50)

            result = city_analysis(df)

            print(result)


        # ==========================================
        # 12. SEARCH EMPLOYEE
        # ==========================================

        elif choice == "12":

            name = input(
                "Enter employee name: "
            )

            result = search_employee(
                df,
                name
            )

            if result.empty:

                print(
                    "\nEmployee not found."
                )

            else:

                print(
                    "\nEmployee Found"
                )

                print("=" * 100)

                print(
                    result.to_string(
                        index=False
                    )
                )


        # ==========================================
        # 13. SALARY BY EXPERIENCE
        # ==========================================

        elif choice == "13":

            print(
                "\nAverage Salary by Experience"
            )

            print("=" * 50)

            result = salary_by_experience(
                df
            )

            print(result)


        # ==========================================
        # 14. GENERATE CHARTS
        # ==========================================

        elif choice == "14":

            print(
                "\nGenerating charts..."
            )

            salary_bar_chart(
                df,
                os.path.join(
                    OUTPUT_DIR,
                    "salary_chart.png"
                )
            )

            department_salary_chart(
                df,
                os.path.join(
                    OUTPUT_DIR,
                    "department_salary.png"
                )
            )

            salary_distribution_chart(
                df,
                os.path.join(
                    OUTPUT_DIR,
                    "salary_distribution.png"
                )
            )

            department_distribution_chart(
                df,
                os.path.join(
                    OUTPUT_DIR,
                    "department_distribution.png"
                )
            )

            print(
                "\nAll charts generated successfully!"
            )


        # ==========================================
        # 15. OOP EMPLOYEE OBJECT
        # ==========================================

        elif choice == "15":

            employees = create_employee_objects(
                df
            )

            print(
                f"\nTotal Employee Objects: "
                f"{len(employees)}"
            )

            print(
                "\nDisplaying first employee object:"
            )

            employees[0].display()


        # ==========================================
        # 16. EXIT
        # ==========================================

        elif choice == "16":

            print(
                "\nThank you for using "
                "Employee Salary Analyzer!"
            )

            break


        # ==========================================
        # INVALID OPTION
        # ==========================================

        else:

            print(
                "\nInvalid choice."
                " Please select 1-16."
            )


# ==================================================
# PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":

    main()