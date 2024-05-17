def calculator_decorator(func):
    def wrapper(expression):
        try:

            allowed_chars = set("0123456789+-*/(). ")
            if not all(char in allowed_chars for char in expression):
                raise ValueError("Вираз містить неприпустимі символи")


            result = func(expression)

            
            if not isinstance(result, (int, float)):
                raise ValueError("Результат має бути числом")

            return result
        except ZeroDivisionError:
            return "Помилка: Ділення на нуль"
        except ValueError as ve:
            return f"Помилка: {ve}"
        except Exception as e:
            return f"Невідома помилка: {e}"

    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)


print(calculate("10 + 20"))
print(calculate("10 / 0"))
print(calculate("10 +"))
print(calculate("10 + (2 * 3)"))
print(calculate("10 + abc"))
