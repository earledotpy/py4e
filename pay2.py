hr = float(input("Enter Hours: "))
rt = float(input("Enter Rate: "))
if hr > 40:
    pay = rt * 40 + (rt * 1.5 * (hr - 40))
else: pay = hr * rt
print(pay)
