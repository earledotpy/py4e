numlist = list ()
while (True):
    imp = input('Enter a numer: ')
    if imp == 'done': break
    value = float(imp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average', average)
