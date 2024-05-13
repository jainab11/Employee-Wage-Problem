# wage_calculator.py

def calculate_wages(total_working_hours, total_working_days, wage_per_hour=20, full_day_hours=8):
    total_wage = 0
    total_hours = 0
    days_worked = 0

    while total_hours < total_working_hours and days_worked < total_working_days:
        daily_wage = wage_per_hour * full_day_hours
        total_wage += daily_wage
        total_hours += full_day_hours
        days_worked += 1

    return total_wage
