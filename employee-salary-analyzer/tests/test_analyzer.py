import sys
import os

import pandas as pd


# Add src folder to Python path

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)


from analyzer import (
    salary_statistics,
    age_statistics,
    experience_statistics,
    department_analysis
)


def test_salary_statistics():

    data = {
        "Monthly_Salary": [
            40000,
            50000,
            60000
        ]
    }

    df = pd.DataFrame(data)

    result = salary_statistics(df)

    assert result[
        "Total Monthly Salary"
    ] == 150000

    assert result[
        "Average Monthly Salary"
    ] == 50000

    assert result[
        "Maximum Monthly Salary"
    ] == 60000

    assert result[
        "Minimum Monthly Salary"
    ] == 40000

    assert result[
        "Median Monthly Salary"
    ] == 50000


def test_age_statistics():

    data = {
        "Age": [
            20,
            30,
            40,
            50
        ]
    }

    df = pd.DataFrame(data)

    result = age_statistics(df)

    assert result[
        "Average Age"
    ] == 35

    assert result[
        "Minimum Age"
    ] == 20

    assert result[
        "Maximum Age"
    ] == 50

    assert result[
        "Median Age"
    ] == 35


def test_experience_statistics():

    data = {
        "Experience_Years": [
            1,
            3,
            5
        ]
    }

    df = pd.DataFrame(data)

    result = experience_statistics(df)

    assert result[
        "Average Experience"
    ] == 3

    assert result[
        "Minimum Experience"
    ] == 1

    assert result[
        "Maximum Experience"
    ] == 5

    assert result[
        "Median Experience"
    ] == 3


def test_department_analysis():

    data = {
        "Department": [
            "IT",
            "IT",
            "HR"
        ],

        "Monthly_Salary": [
            40000,
            60000,
            50000
        ]
    }

    df = pd.DataFrame(data)

    result = department_analysis(df)

    assert result.loc[
        "IT",
        "Employee_Count"
    ] == 2

    assert result.loc[
        "IT",
        "Average_Salary"
    ] == 50000