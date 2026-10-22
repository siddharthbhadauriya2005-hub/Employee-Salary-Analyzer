import matplotlib.pyplot as plt


def salary_bar_chart(df, output_path):
    """
    Employee monthly salary bar chart.
    """

    plt.figure(figsize=(12, 6))

    plt.bar(
        df["Name"],
        df["Monthly_Salary"]
    )

    plt.title(
        "Employee Monthly Salary"
    )

    plt.xlabel("Employee")

    plt.ylabel(
        "Monthly Salary (₹)"
    )

    plt.xticks(rotation=90)

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()

    print(
        f"Salary chart saved: {output_path}"
    )


def department_salary_chart(df, output_path):
    """
    Average salary by department.
    """

    department_salary = (
        df.groupby("Department")[
            "Monthly_Salary"
        ]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(9, 6))

    plt.bar(
        department_salary.index,
        department_salary.values
    )

    plt.title(
        "Average Salary by Department"
    )

    plt.xlabel("Department")

    plt.ylabel(
        "Average Monthly Salary (₹)"
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()

    print(
        f"Department salary chart saved: {output_path}"
    )


def salary_distribution_chart(df, output_path):
    """
    Salary distribution histogram.
    """

    plt.figure(figsize=(9, 6))

    plt.hist(
        df["Monthly_Salary"],
        bins=10,
        edgecolor="black"
    )

    plt.title(
        "Monthly Salary Distribution"
    )

    plt.xlabel(
        "Monthly Salary (₹)"
    )

    plt.ylabel(
        "Number of Employees"
    )

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()

    print(
        f"Salary distribution chart saved: {output_path}"
    )


def department_distribution_chart(
    df,
    output_path
):
    """
    Employee distribution by department.
    """

    department_count = (
        df["Department"]
        .value_counts()
    )

    plt.figure(figsize=(8, 8))

    plt.pie(
        department_count.values,
        labels=department_count.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(
        "Employee Distribution by Department"
    )

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()

    print(
        f"Department distribution chart saved: {output_path}"
    )