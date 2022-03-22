'''
Code for calculating BMI from JSON data
Author: Vishnu Teja Gadde
'''

import json

'''
Function to update each json
updateDict(bmi, i) -> updatedDictionary with three extra columns
	bmi: BMI value
    i: previous json data
'''
def updateDict(bmi, i):
    if bmi >= 18.4 and bmi < 18.5:
        i.update({"BMI": bmi, "BMICategory": "Underweight", "HealthRisk": "Malnutrition risk"})
        return(i)
    elif bmi >= 18.5 and bmi < 25:
        i.update({"BMI": bmi, "BMICategory": "Normal weight", "HealthRisk": "Low risk"})
        return(i)
    elif bmi >= 25 and bmi <30:
        i.update({"BMI": bmi, "BMICategory": "Overweight", "HealthRisk": "Enhanced risk"})
        return(i)
    elif bmi >= 30 and bmi < 35:
        i.update({"BMI": bmi, "BMICategory": "Moderately obese", "HealthRisk": "Medium risk"})
        return(i)
    elif bmi >= 35 and bmi < 40:
        i.update({"BMI": bmi, "BMICategory": "Severel obese", "HealthRisk": "High"})
        return(i)
    elif bmi >= 40:
        i.update({"BMI": bmi, "BMICategory": "Very severely obese", "HealthRisk": "Very high risk"})
        return(i)

# Static json input
rawData = [
  {
    "Gender": "Male",
    "HeightCm": 171,
    "WeightKg": 96
  },
  {
    "Gender": "Male",
    "HeightCm": 161,
    "WeightKg": 85
  },
  {
    "Gender": "Male",
    "HeightCm": 180,
    "WeightKg": 77
  },
  {
    "Gender": "Female",
    "HeightCm": 166,
    "WeightKg": 62
  },
  {
    "Gender": "Female",
    "HeightCm": 150,
    "WeightKg": 70
  },
  {
    "Gender": "Female",
    "HeightCm": 167,
    "WeightKg": 82
  }
]

# Empty varaible to update new columns
new_data = []

# Iterate throw rawData and update new_data
for i in rawData:
    height = i.get("HeightCm")/100
    weight = i.get("WeightKg")
    bmi = weight/pow(height, 2)
    updatedDict = updateDict(bmi, i)
    new_data.append(updatedDict)

# Print updated json
print(new_data)

'''
output received:
[{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'BMI': 32.83061454806607, 'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'}, {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85, 'BMI': 32.79194475521777, 'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'}, {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'BMI': 23.76543209876543, 'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'}, {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'BMI': 22.49963710262738, 'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'}, {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70, 'BMI': 31.11111111111111, 'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'}, {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82, 'BMI': 29.402273297715947, 'BMICategory': 'Overweight', 'HealthRisk': 'Enhanced risk'}]
'''