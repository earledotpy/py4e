total = 0
count = 0
while True:
    try:
        line = input('Enter a number: ')
        if line[0] == '#':
            continue
        if line == 'done':
            break
        current_number = int(line)
        total = total + current_number
        count = count + 1
        
    except ValueError:
        print('Invalid input!')
    print(line)
print('Done')
    
if count > 0:
    calculate_average = round(total / count,2) 
    print('Average: ', calculate_average)
    print(count)
    print(total)
else: print('No number entered')
