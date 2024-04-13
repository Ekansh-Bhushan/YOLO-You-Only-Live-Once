def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi


weight = 70  # in kilograms
height = 1.75  # in meters

bmi = calculate_bmi(weight, height)
print("BMI:", bmi)