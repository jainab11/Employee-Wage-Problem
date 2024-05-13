import random

def attendance():
    # Generate a random integer between 0 and 1 (inclusive)
    random_value = random.randint(0, 1)
    
    # Check if the random value is 1 (Present) or 0 (Absent)
    if random_value == 1:
        print("Present")
    else:
        print("Absent")
