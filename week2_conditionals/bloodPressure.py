systolic = 180
diastolic = 65

stage_2_high = systolic > 160 or diastolic > 100

low = systolic < 90 and diastolic < 60

if systolic < 90 and diastolic < 60:
    category = "Low"
elif systolic < 120 and diastolic < 80:
    category = "Normal"
elif systolic < 140 and diastolic < 90:
    category = "Prehypertension"
elif systolic < 160 and diastolic < 100:
    category = "Stage 1 Hypertension"
elif systolic < 180 and diastolic < 80:
    category = "Normal"
else:
    category = "Abnormal Entry"

print (category)