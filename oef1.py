
# ZeroDivisionError
def deel(a, b):
    try:
        resultaat = a / b
        print(f"Resultaat: {resultaat}")
    except ZeroDivisionError:
        print("je kan nie delen door nul")

deel(10, 0)