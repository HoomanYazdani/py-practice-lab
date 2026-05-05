from arabic_reshaper import reshape
from bidi.algorithm import get_display

# اطلاعات اولیه
weight_kg = 75
height_cm = 185

# تعریف تبدیل سانتی متر به متر
height_m = height_cm / 100

# محاسبه BMI
BMI = weight_kg / (height_m ** 2)

# نمایش نتیجه محاسبه شاخص توده بدنی
text = f"شاخص توده بدنی شما برابر است با: {BMI:.2f} بر حسب kg/m^2"
print(get_display(reshape(text)))

# بررسی شرایط
if BMI < 18.5:
    print(get_display(reshape("شخص دارای کمبود وزن است")))
elif BMI < 24.9:
    print(get_display(reshape("شخص دارای وزن ایده آل است")))
else:
    print(get_display(reshape("شخص دارای اضافه وزن می باشد")))