# Better catch exact error

def divide(dividendo, divisor):
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return 'You are dividing by zero'

print(divide(1, 0))
print('End of error')
