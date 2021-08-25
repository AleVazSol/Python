target = int(input('Pick a number: '))
epsilon = 0.001
bottom = 0.0
top = max(1.0, target)
answer = (bottom + top) / 2

while abs(answer**2 - target) >= epsilon:
    print(f'bajo={bottom}, alto={top}, respuesta={answer}')
    if answer**2 < target:
        bottom = answer
    else:
        top = answer

    answer = (top + bottom) / 2

print(f'the square root of {target} is {answer}')
