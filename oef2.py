
def tel_op(a, b):
    try:
        return a + b
    except TypeError:
        print("je moet getallen gebruiken")

tel_op(5, "drie")