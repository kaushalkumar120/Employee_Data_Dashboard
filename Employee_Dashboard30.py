import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load / Generate Data
def load_data():
    departments = ['HR', 'IT', 'Sales', 'Finance', 'Marketing']

    data = {
        'Department': np.random.choice(departments, 50),
        'Salary': np.random.randint(30000, 100000, 50)
    }

    df = pd.DataFrame(data)
    return df

# Analysis + Output
def analyze_data(df):
    print("\n📊 DATA SUMMARY")
    print(f"Total Employees: {len(df)}")

    avg_salary = df.groupby('Department')['Salary'].mean()
    dept_count = df['Department'].value_counts()

    print("\n👉 Average Salary by Department:")
    print(avg_salary)

    print("\n👉 Employees per Department:")
    print(dept_count)

    return avg_salary, dept_count

# Charts
def create_dashboard(avg_salary, dept_count):
    plt.figure(figsize=(10, 5))

    # Bar Chart
    plt.subplot(1, 2, 1)
    plt.bar(avg_salary.index, avg_salary.values)
    plt.title("Avg Salary by Department")

    # Pie Chart
    plt.subplot(1, 2, 2)
    plt.pie(dept_count.values, labels=dept_count.index, autopct='%1.1f%%')
    plt.title("Employee Distribution")

    plt.tight_layout()
    plt.show()

# Main
def main():
    print("🚀 EMPLOYEE DASHBOARD")

    df = load_data()
    avg_salary, dept_count = analyze_data(df)
    create_dashboard(avg_salary, dept_count)

    print("\n✅ Done!")

if __name__ == "__main__":
    main()