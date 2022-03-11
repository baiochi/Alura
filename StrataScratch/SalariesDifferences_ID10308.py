# Salaries Differences ID 10308

# Import your libraries
import pandas as pd

# Start writing code
db_employee.head()

# Check dept ids
db_dept.head()

# engineering = 1 , marketing = 4

# select only employees from engineering and marketing
db_employee.loc[(db_employee['department_id'] == 1) | (db_employee['department_id'] == 4)].sort_values('salary', ascending=True)

# create df for each dept, order by highest salary
eng_employee = db_employee.loc[db_employee['department_id'] == 1].sort_values('salary', ascending=False).reset_index()
mkt_employee = db_employee.loc[db_employee['department_id'] == 4].sort_values('salary', ascending=False).reset_index()

#eng_employee['total_salary'] = eng_employee['salary'][0:5] - mkt_employee['salary'][0:5]

salary_diff = abs(mkt_employee['salary'] - eng_employee['salary']).dropna()

salary_diff.name = 'salary_difference'
salary_diff