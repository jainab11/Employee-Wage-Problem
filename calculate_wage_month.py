# monthly_wage_calculator.py

def calculate_monthly_wage(wage_per_hour, full_day_hours, total_working_days):
    daily_wage = wage_per_hour * full_day_hours
    return daily_wage * total_working_days
