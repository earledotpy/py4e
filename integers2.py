largest = None
smallest = None            

while True:
    num_str = input('Enter a number:')
    
    if num_str == 'done':
        break
    try:
        num = int(num_str)
    except ValueError:
        print('Invalid input')
        continue
        
    if largest is None:
            largest = num
    elif num > largest:
            largest = num 
    if smallest is None:
            smallest = num
    elif num < smallest:
            smallest = num
   
if largest is not None:
    print('Maximum is', largest)
if smallest is not None:
    print('Minimun is', smallest)
else: print('No number entered')
