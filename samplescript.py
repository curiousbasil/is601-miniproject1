def bmi_calc(weight_kg, height_m):
    """Calculate BMI from weight in kg and height in meters"""
    bmi = int(weight_kg / height_m**2)
    return bmi

# Subject data = [weight_kg, height_m]
subject1 = [80, 1.62]
subject2 = [69, 1.53]
subject3 = [80, 1.66]

bmi_subject1 = bmi_calc(subject1[0], subject1[1])
print("bmi {} = {}".format('subject1', bmi_subject1))

bmi_subject2 = bmi_calc(subject2[0], subject2[1])
print("bmi {} = {}".format('subject2', bmi_subject2))

bmi_subject3 = bmi_calc(subject3[0], subject3[1])
print("bmi {} = {}".format('subject3', bmi_subject3))

