import random

# Define the ranges for each attribute
attribute_ranges = {
    'Red Blood Cell Count (RBC) (male)': (4.5, 6.0),
    'Red Blood Cell Count (RBC) (female)': (4.0, 5.5),
    'White Blood Cell Count (WBC)': (4500, 11000),
    'Hemoglobin (Hgb) (male)': (13.5, 17.5),
    'Hemoglobin (Hgb) (female)': (12.0, 15.5),
    'Hematocrit (Hct) (male)': (40, 50),
    'Hematocrit (Hct) (female)': (36, 46),
    'Platelet Count': (150000, 400000),
    'Glucose (fasting)': (70, 100),
    'Sodium': (135, 145),
    'Potassium': (3.5, 5.0),
    'Total Protein': (6.0, 8.0),
    'Total Cholesterol': (0, 200),
    'Alanine Aminotransferase (ALT)': (7, 56),
    'Aspartate Aminotransferase (AST)': (10, 40),
    'Alkaline Phosphatase (ALP)': (44, 147),
    'Total Bilirubin': (0.3, 1.2),
    'Creatinine (male)': (0.6, 1.3),
    'Creatinine (female)': (0.5, 1.1),
    'Blood Urea Nitrogen (BUN)': (7, 20),
    'Thyroid-Stimulating Hormone (TSH)': (0.4, 4.0),
    'Free Thyroxine (T4)': (0.8, 1.8),
    'Prothrombin Time (PT)': (11, 13.5),
    'International Normalized Ratio (INR)': (0.8, 1.2),
    'C-Reactive Protein (CRP)': (0, 1.0),
    'Vitamin D': (30, 100),
    'Vitamin B12': (200, 900),
    'Iron': (60, 170),
    'Testosterone (male)': (300, 1000),
    'Estradiol (premenopausal female)': (10, 40),
    'Progesterone (follicular phase)': (0.1, 0.8)
}

# Initialize an empty list to store generated values
generated_values = []

# Generate random values for each attribute and append to the list
for attribute, value_range in attribute_ranges.items():
    generated_value = random.uniform(value_range[0], value_range[1])
    generated_values.append((attribute, generated_value))

# Print the generated values
for attribute, value in generated_values:
    print(f"{attribute}: {value}")
