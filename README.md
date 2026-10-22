# Employee Salary Analyzer 📊🐍

Employee Salary Analyzer is a Python-based mini project that
analyzes employee salary and demographic information.

The project uses Python, Object-Oriented Programming, NumPy,
Pandas, and Matplotlib.

---

## 🎯 Project Objective

The main objective is to analyze employee information and
generate useful salary statistics and visualizations.

The system can:

- Display employee data
- Calculate salary statistics
- Calculate age statistics
- Calculate experience statistics
- Find highest-paid employee
- Find lowest-paid employee
- Analyze salary by department
- Analyze education
- Analyze gender
- Analyze city
- Search employees
- Generate charts

---

# 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Pytest
- CSV

---

# 📁 Project Structure

```text
employee-salary-analyzer/
│
├── data/
│   └── employees.csv
│
├── src/
│   ├── main.py
│   ├── employee.py
│   ├── data_manager.py
│   ├── analyzer.py
│   └── visualization.py
│
├── output/
│   ├── salary_chart.png
│   ├── department_salary.png
│   ├── salary_distribution.png
│   └── department_distribution.png
│
├── tests/
│   └── test_analyzer.py
│
├── requirements.txt
├── README.md
└── .gitignore



=========================================================================================
=========================================================================================

# EMPLOYEE_SALARY_ANALYZER : PROBLEM STATEMENT AND SOLUTION

# Employee Salary Analyzer

## 1. What is the Problem?

The **Employee Salary Dataset** contains information about different employees, including:

* Employee ID
* Employee Name
* Department
* Experience
* Education Level
* Age
* Gender
* City
* Monthly Salary

The main problem is that this data is stored in a **raw CSV format**. Looking at the CSV file manually makes it difficult to understand important information such as:

* Which employee has the highest salary?
* Which employee has the lowest salary?
* What is the average employee salary?
* Which department has the highest average salary?
* How does experience affect salary?
* What is the salary distribution?
* How many employees are working in each department?
* What is the average age and experience of employees?

Therefore, the project solves the problem of **converting raw employee data into meaningful information using Python data analysis and visualization techniques**.

---

# 2. Problem in the Existing Dataset

The dataset itself is not necessarily a "bad" dataset. The problem is mainly that it is **raw and unprocessed**.

For example, the CSV may contain 50 employee records. If we want to find the average salary manually, we would have to calculate all salary values ourselves.

Similarly, finding department-wise salary, highest-paid employee, or salary distribution manually would take time and could lead to mistakes.

### Main Problems

**1. Raw Data**

The employee information is stored in rows and columns without analysis.

**2. Manual Calculation**

Calculating salary statistics manually is time-consuming.

**3. Difficult Comparison**

It is difficult to compare salaries between departments, cities, education levels, and experience levels.

**4. Lack of Visualization**

Numbers in a CSV file do not immediately show patterns or trends.

**5. Data Quality**

Real-world datasets may contain duplicate records or missing values, so the data needs to be checked and cleaned before analysis.

---

# 3. Solution Used in This Project

To solve these problems, we developed an **Employee Salary Analyzer using Python**.

The project uses:

* **Python** → Main programming language
* **OOP** → Employee objects and class
* **Pandas** → Data loading, cleaning, filtering and analysis
* **NumPy** → Numerical calculations
* **Matplotlib** → Graphs and visualization

The basic workflow is:

```text
Employee CSV Dataset
        ↓
   Load Dataset
        ↓
    Data Cleaning
        ↓
   Data Processing
        ↓
   Data Analysis
        ↓
   Salary Statistics
        ↓
 Department / Experience Analysis
        ↓
   Data Visualization
        ↓
     Final Insights
```

---

# 4. How the Project Solves the Problem

### Step 1 — Load the Dataset

Pandas is used to read the CSV file.

```python
df = pd.read_csv("data/employees.csv")
```

This converts the CSV data into a **Pandas DataFrame**.

---

### Step 2 — Clean the Data

The project checks the dataset for duplicate and missing values.

For example:

```python
df = df.drop_duplicates()
```

For missing numerical values, the project can use the median:

```python
df["Monthly_Salary"] = df["Monthly_Salary"].fillna(
    df["Monthly_Salary"].median()
)
```

This makes the dataset more suitable for analysis.

---

### Step 3 — Calculate Salary Statistics

NumPy is used for numerical calculations.

The project calculates:

* Total salary
* Average salary
* Maximum salary
* Minimum salary
* Median salary
* Standard deviation

Example:

```python
salary = np.array(df["Monthly_Salary"])

average_salary = np.mean(salary)
maximum_salary = np.max(salary)
minimum_salary = np.min(salary)
```

This solves the problem of manually calculating salary statistics.

---

### Step 4 — Find Highest and Lowest Paid Employees

Pandas can identify employees with the highest and lowest salaries.

```python
highest = df.loc[df["Monthly_Salary"].idxmax()]
lowest = df.loc[df["Monthly_Salary"].idxmin()]
```

This provides quick information about salary extremes.

---

### Step 5 — Department Analysis

The project compares salaries between departments.

```python
df.groupby("Department")["Monthly_Salary"].mean()
```

This helps answer:

> Which departments have higher or lower average salaries?

---

### Step 6 — Experience Analysis

Employee experience can also be analyzed against salary.

For example:

```python
df.groupby("Experience_Years")["Monthly_Salary"].mean()
```

This helps identify salary patterns based on experience.

---

### Step 7 — Create Visualizations

Matplotlib is used to convert numerical information into graphs.

The project can generate:

**Salary Bar Chart**

```text
Employee 1  ███████████
Employee 2  █████████
Employee 3  ███████
```

**Department Salary Chart**

```text
IT           ███████████
Marketing    █████████
HR           ███████
Finance      ██████████
```

**Salary Distribution**

A histogram shows how employee salaries are distributed.

**Department Distribution**

A pie chart shows the percentage of employees in different departments.

These graphs make the results easier to understand.

---

# 5. Role of OOP in the Project

The project also uses **Object-Oriented Programming**.

An `Employee` class is created:

```python
class Employee:

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
```

Each employee can then be represented as an **object**.

For example:

```text
Employee Object
       ↓
Employee_1
       ↓
Department = Marketing
Experience = 15 years
Education = Master
Salary = ₹111416/month
```

The class also contains methods such as:

```python
annual_salary()
```

which calculates:

```text
Monthly Salary × 12
```

---

# 6. What is the Final Solution?

The final solution is a **menu-driven Employee Salary Analyzer**.

The user can select operations such as:

```text
1. Display Employees
2. Dataset Information
3. Salary Statistics
4. Experience Statistics
5. Age Statistics
6. Highest Paid Employee
7. Lowest Paid Employee
8. Department Analysis
9. Education Analysis
10. Gender Analysis
11. City Analysis
12. Search Employee
13. Salary by Experience
14. Generate Charts
15. Show Employee Object
16. Exit
```

Instead of manually examining the CSV file, the user can select an option and immediately receive the required information.

---

# 7. Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Main programming language      |
| OOP        | Employee class and objects     |
| Pandas     | CSV handling and data analysis |
| NumPy      | Numerical calculations         |
| Matplotlib | Graphs and charts              |
| Pytest     | Testing project functions      |
| CSV        | Employee dataset storage       |

---

# 8. One-Minute College Viva Explanation

**"Our project is Employee Salary Analyzer. The main problem is that employee data is available in raw CSV format, which makes it difficult to manually calculate salary statistics and identify useful patterns. To solve this problem, we developed a Python-based data analysis application. Pandas is used to load, clean and analyze the dataset, NumPy is used for numerical calculations such as mean, median, maximum and minimum salary, and Matplotlib is used to create graphs. We also implemented OOP using an Employee class to represent individual employees. The system can perform salary analysis, department analysis, experience analysis, find the highest and lowest paid employees, search employees and generate visualizations. The main objective is to convert raw employee data into meaningful and easy-to-understand information."**

---

# 9. Simple Problem → Solution

```text
PROBLEM
Raw Employee CSV Data
        ↓
Difficult to analyze manually
        ↓
No quick salary statistics
        ↓
No department comparison
        ↓
No visual representation

              ↓

SOLUTION
Python Employee Salary Analyzer
        ↓
Pandas → Load & Clean Data
        ↓
NumPy → Calculate Statistics
        ↓
OOP → Employee Objects
        ↓
Pandas → Analyze Departments/Experience
        ↓
Matplotlib → Generate Charts
        ↓
Meaningful Employee Salary Insights
```

## Final Project Objective

**"The objective of this mini-project is to develop a simple Python-based Employee Salary Analyzer that transforms raw employee data into meaningful salary statistics, comparisons, and visual insights using OOP, NumPy, Pandas, and Matplotlib."**
