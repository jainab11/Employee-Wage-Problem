# employee.py

import random

class EmployeeWageCal:
    wage_per_hour = 20
    full_day_hours = 8

    @classmethod
    def calculate_daily_wage(cls):
        return cls.wage_per_hour * cls.full_day_hours

    @classmethod
    def calculate_monthly_wage(cls, total_working_days):
        return cls.calculate_daily_wage() * total_working_days
    
    @classmethod
    def calculate_part_time_wage(cls, part_time_hours, total_working_days):
        return cls.wage_per_hour * part_time_hours * total_working_days

    @staticmethod
    def attendance():
        return random.choice(["Present", "Absent"])
