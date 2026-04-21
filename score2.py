def computegrade(score):
    if score < 0.0 or score > 1.0--:
        return("Bad Score")
    elif score >= 0.9:           
        return("A")
    elif score >= 0.8:
        return("B")
    elif score >= 0.7:
        return("C")
    elif score >= 0.6:
        return("D")
    else:
        return("F")
        
try:
    inp = input("Enter score: ")
    score = float(inp)
    grade = computegrade(score)
    print(grade)
    
except ValueError:
    print("Bad score")
