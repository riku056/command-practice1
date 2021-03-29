import calc_bmi

print("BMI計算アプリ")
w = int(input("体重"))
h = float(input("身長"))
print(f"BMI:{calc_bmi.get_area(w,h)}")

