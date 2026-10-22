import pandas as pd


def load_data(file_path):
    """
    Load employee data from CSV.
    """

    try:

        df = pd.read_csv(file_path)

        print("Employee dataset loaded successfully.")

        return df

    except FileNotFoundError:

        print("Error: employees.csv not found.")

        return pd.DataFrame()


def clean_data(df):
    """
    Clean employee dataset.
    """

    if df.empty:
        return df

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    numeric_columns = [
        "Experience_Years",
        "Age",
        "Monthly_Salary"
    ]

    categorical_columns = [
        "Name",
        "Department",
        "Education_Level",
        "Gender",
        "City"
    ]

    # Fill numerical missing values
    for column in numeric_columns:

        if column in df.columns:

            df[column] = df[column].fillna(
                df[column].median()
            )

    # Fill categorical missing values
    for column in categorical_columns:

        if column in df.columns:

            if not df[column].mode().empty:

                df[column] = df[column].fillna(
                    df[column].mode()[0]
                )

    return df


def display_data(df, rows=10):
    """
    Display employee records.
    """

    if df.empty:

        print("No employee data available.")

        return

    print("\nEmployee Data")
    print("=" * 120)

    print(
        df.head(rows).to_string(index=False)
    )

    print("=" * 120)


def dataset_info(df):
    """
    Display basic dataset information.
    """

    print("\nDataset Information")
    print("=" * 50)

    print(f"Total Employees : {df.shape[0]}")
    print(f"Total Columns   : {df.shape[1]}")

    print("\nColumn Names:")

    for column in df.columns:

        print(f"- {column}")


def create_employee_objects(df):
    """
    Convert DataFrame records into Employee objects.
    """

    from employee import Employee

    employees = []

    for _, row in df.iterrows():

        employee = Employee(
            employee_id=row["EmployeeID"],
            name=row["Name"],
            department=row["Department"],
            experience_years=row["Experience_Years"],
            education_level=row["Education_Level"],
            age=row["Age"],
            gender=row["Gender"],
            city=row["City"],
            monthly_salary=row["Monthly_Salary"]
        )

        employees.append(employee)

    return employees