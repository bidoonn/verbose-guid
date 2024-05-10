result = []

def divider(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both a and b must be integers")
    if a < b:
        raise ValueError("a must be greater than or equal to b")
    if b > 100:
        raise IndexError("b must be less than or equal to 100")
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (TypeError, ValueError, IndexError) as e:
        print(f"Error: {e}")

print(result)
