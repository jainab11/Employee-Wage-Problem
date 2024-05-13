# employee.py
from employee import EmployeeWageCal
import random
class EmployeeWageCal:
    @staticmethod
    def calculate_daily_wage(wage_per_hour, full_day_hours):
        return wage_per_hour * full_day_hours

    @staticmethod
    def calculate_monthly_wage(wage_per_hour, full_day_hours, total_working_days):
        return EmployeeWageCal.calculate_daily_wage(wage_per_hour, full_day_hours) * total_working_days
    
    @staticmethod
    def calculate_part_time_wage(wage_per_hour, part_time_hours, total_working_days):
        return wage_per_hour * part_time_hours * total_working_days

    @staticmethod
    def attendance():
        return random.choice(["Present", "Absent"])
# main.py



def main():
    print("Welcome to Employee Wage Problem")
    print("START")

    # Company 1
    wage_per_hour_c1 = 20
    full_day_hours_c1 = 8
    total_working_days_c1 = 20

    print("Company 1 - Daily Wage:", EmployeeWageCal.calculate_daily_wage(wage_per_hour_c1, full_day_hours_c1))
    print("Company 1 - Monthly Wage:", EmployeeWageCal.calculate_monthly_wage(wage_per_hour_c1, full_day_hours_c1, total_working_days_c1))
    print("Company 1 - Attendance:", EmployeeWageCal.attendance())
    print("Company 1 - Part-time Wage:", EmployeeWageCal.calculate_part_time_wage(wage_per_hour_c1, 4, total_working_days_c1))

    # Company 2
    wage_per_hour_c2 = 25
    full_day_hours_c2 = 7
    total_working_days_c2 = 22

    print("\nCompany 2 - Daily Wage:", EmployeeWageCal.calculate_daily_wage(wage_per_hour_c2, full_day_hours_c2))
    print("Company 2 - Monthly Wage:", EmployeeWageCal.calculate_monthly_wage(wage_per_hour_c2, full_day_hours_c2, total_working_days_c2))
    print("Company 2 - Attendance:", EmployeeWageCal.attendance())
    print("Company 2 - Part-time Wage:", EmployeeWageCal.calculate_part_time_wage(wage_per_hour_c2, 6, total_working_days_c2))

if __name__ == "__main__":
    main()
