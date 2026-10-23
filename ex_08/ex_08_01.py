#Exercise 1: Write a function called `chop` that takes a list and modifies it, removing the first and last elements, and returns `None`. Then write a function called `middle` that takes a list and returns a new list that contains all but the first and last elements.

def chop(flst):
    del flst[:1]
    del flst[-1:]

def middle(flst):
    return flst[1:-1]

letters = ['a', 'b', 'c', 'd', 'e', 'f']

result = middle(letters)
print(letters)
print(result)

result = chop(letters)
print(letters)
print(result)

