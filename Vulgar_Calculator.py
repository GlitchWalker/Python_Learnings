import re

print("Our mother fuckiin calculator")
print("Type 'fuck_off' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the piece of shit equation:")
    else:
        equation = input(str(previous))

    if equation == 'fuck_off':
        print("Gonna pop a cap in yo ass")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()

