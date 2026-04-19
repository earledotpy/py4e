try:
    inp = input("Enter Hours: ")
    hr = float(inp)
    inp = input("Enter Rate: ")
    rt = float(inp)
    if hr > 40:
        pay = (40 * rt) + (40 - hr) * (rt * 1.5)
    else:
        pay = rt * hr
    print(pay)
except:
    print("Error, please enter numeric input")
