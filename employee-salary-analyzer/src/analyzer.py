import numpy as np
import pandas as pd


def salary_statistics(df):
    """
    Calculate salary statistics using NumPy.
    """

    salaries = np.array(
        df["Monthly_Salary"]
    )

    result = {
        "Total Monthly Salary": np.sum(salaries),
        "Average Monthly Salary": np.mean(salaries),
        "Maximum Monthly Salary": np.max(salaries),
        "Minimum Monthly Salary": np.min(salaries),
        "Median Monthly Salary": np.median(salaries),
        "Salary Standard Deviation": np.std(salaries)
    }

    return result


def experience_statistics(df):
    """
    Calculate experience statistics.
    """

    experience = np.array(
        df["Experience_Years"]
    )

    result = {
        "Average Experience": np.mean(experience),
        "Maximum Experience": np.max(experience),
        "Minimum Experience": np.min(experience),
        "Median Experience": np.median(experience)
    }

    return result


def age_statistics(df):
    """
    Calculate age statistics.
    """

    ages = np.array(
        df["Age"]
    )

    result = {
        "Average Age": np.mean(ages),
        "Maximum Age": np.max(ages),
        "Minimum Age": np.min(ages),
        "Median Age": np.median(ages)
    }

    return result


def display_salary_statistics(df):

    result = salary_statistics(df)

    print("\nSalary Statistics")
    print("=" * 55)

    for key, value in result.items():

        print(
            f"{key:<30}: ₹{value:,.2f}"
        )


def display_experience_statistics(df):

    result = experience_statistics(df)

    print("\nExperience Statistics")
    print("=" * 50)

    for key, value in result.items():

        print(
            f"{key:<30}: {value:.2f}"
        )


def display_age_statistics(df):

    result = age_statistics(df)

    print("\nAge Statistics")
    print("=" * 50)

    for key, value in result.items():

        print(
            f"{key:<30}: {value:.2f}"
        )


def highest_paid_employee(df):
    """
    Find employee with highest monthly salary.
    """

    index = df["Monthly_Salary"].idxmax()

    return df.loc[index]


def lowest_paid_employee(df):
    """
    Find employee with lowest monthly salary.
    """

    index = df["Monthly_Salary"].idxmin()

    return df.loc[index]


def department_analysis(df):
    """
    Department-wise salary analysis.
    """

    result = (
        df.groupby("Department")[
            "Monthly_Salary"
        ]
        .agg(
            Employee_Count="count",
            Average_Salary="mean",
            Maximum_Salary="max",
            Minimum_Salary="min"
        )
        .round(2)
    )

    return result


def education_analysis(df):
    """
    Education-wise employee analysis.
    """

    return (
        df["Education_Level"]
        .value_counts()
    )


def gender_analysis(df):
    """
    Gender-wise employee analysis.
    """

    return (
        df["Gender"]
        .value_counts()
    )


def city_analysis(df):
    """
    City-wise employee analysis.
    """

    return (
        df["City"]
        .value_counts()
    )


def search_employee(df, name):
    """
    Search employee by name.
    """

    result = df[
        df["Name"].str.contains(
            name,
            case=False,
            na=False
        )
    ]

    return result


def salary_by_experience(df):
    """
    Analyze average salary according to experience.
    """

    result = (
        df.groupby("Experience_Years")[
            "Monthly_Salary"
        ]
        .mean()
        .round(2)
    )

    return result


def annual_salary_column(df):
    """
    Add annual salary column.
    """

    df = df.copy()

    df["Annual_Salary"] = (
        df["Monthly_Salary"] * 12
    )

    return df