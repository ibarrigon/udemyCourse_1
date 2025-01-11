def divide(dividendo, divisor):
    try:
        return dividendo / divisor
    except:
        return 'You are dividing by zero'

print(divide(1, 0))
