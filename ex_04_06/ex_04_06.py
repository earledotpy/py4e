def computepay(hr, rt):
    if hr <= 40:
        return hr * rt
    return rt * 40 + (rt *1.5) * (hr - 40)
hr = float(input("Enter Hours: "))
rt = float(input("Enter Rate: "))
py = computepay(hr, rt)
print('Pay', py)
