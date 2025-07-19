class BMICalculator:
    def __init__(self, name, weight, height):
        self.name = name            # in string
        self.weight = weight        # in kilograms
        self.height = height        # in meters

    def BMIcal(self):
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)      # round off to 2 decimal places

    def yourCategory(self):
        bmi = self.BMIcal()
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        return category

    def info(self):
        bmi = self.BMIcal()
        category = self.yourCategory()
        print("Name: ",self.name)
        print("Weight in kg: ",self.weight)
        print("Height: ",self.height)
        print("BMI: ",bmi)
        print("Category: ",category)


person = BMICalculator("Saksham", 55, 1.75)
person.info()