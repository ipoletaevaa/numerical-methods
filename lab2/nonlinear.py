import math


def get_equation(number):
    ln2 = math.log(2)
    ln10 = math.log(10)

    if number == 1:
        text = "2^x - x^2 - 0.5 = 0"
        f = lambda x: 2 ** x - x * x - 0.5
        df = lambda x: ln2 * (2 ** x) - 2 * x
    elif number == 2:
        text = "ln(x + 2) - x^2 = 0"
        f = lambda x: math.log(x + 2) - x * x
        df = lambda x: 1 / (x + 2) - 2 * x
    elif number == 3:
        text = "sqrt(1 - x^2) - e^x + 0.1 = 0"
        f = lambda x: math.sqrt(1 - x * x) - math.exp(x) + 0.1
        df = lambda x: -x / math.sqrt(1 - x * x) - math.exp(x)
    elif number == 4:
        text = "x^3 + x^2 - x - 0.5 = 0"
        f = lambda x: x ** 3 + x * x - x - 0.5
        df = lambda x: 3 * x * x + 2 * x - 1
    elif number == 5:
        text = "cos(x) + 0.25x - 0.5 = 0"
        f = lambda x: math.cos(x) + 0.25 * x - 0.5
        df = lambda x: -math.sin(x) + 0.25
    elif number == 6:
        text = "e^x - 2x - 2 = 0"
        f = lambda x: math.exp(x) - 2 * x - 2
        df = lambda x: math.exp(x) - 2
    elif number == 7:
        text = "2^x + x^2 - 2 = 0"
        f = lambda x: 2 ** x + x * x - 2
        df = lambda x: ln2 * (2 ** x) + 2 * x
    elif number == 8:
        text = "ln(x + 1) - 2x^2 + 1 = 0"
        f = lambda x: math.log(x + 1) - 2 * x * x + 1
        df = lambda x: 1 / (x + 1) - 4 * x
    elif number == 9:
        text = "x^3 + x^2 - 2x - 1 = 0"
        f = lambda x: x ** 3 + x * x - 2 * x - 1
        df = lambda x: 3 * x * x + 2 * x - 2
    elif number == 10:
        text = "sin(x) - 2x^2 + 0.5 = 0"
        f = lambda x: math.sin(x) - 2 * x * x + 0.5
        df = lambda x: math.cos(x) - 4 * x
    elif number == 11:
        text = "e^x - x^3 + 3x^2 - 2x - 3 = 0"
        f = lambda x: math.exp(x) - x ** 3 + 3 * x * x - 2 * x - 3
        df = lambda x: math.exp(x) - 3 * x * x + 6 * x - 2
    elif number == 12:
        text = "3^x - 5x^2 + 1 = 0"
        f = lambda x: 3 ** x - 5 * x * x + 1
        df = lambda x: math.log(3) * (3 ** x) - 10 * x
    elif number == 13:
        text = "ln(x + 1) - 2x + 0.5 = 0"
        f = lambda x: math.log(x + 1) - 2 * x + 0.5
        df = lambda x: 1 / (x + 1) - 2
    elif number == 14:
        text = "x^3 - 2x^2 - 10x + 15 = 0"
        f = lambda x: x ** 3 - 2 * x * x - 10 * x + 15
        df = lambda x: 3 * x * x - 4 * x - 10
    elif number == 15:
        text = "sin(x) - x^2 + 1 = 0"
        f = lambda x: math.sin(x) - x * x + 1
        df = lambda x: math.cos(x) - 2 * x
    elif number == 16:
        text = "x*e^x + x^2 - 1 = 0"
        f = lambda x: x * math.exp(x) + x * x - 1
        df = lambda x: math.exp(x) * (x + 1) + 2 * x
    elif number == 17:
        text = "4^x - 5x - 2 = 0"
        f = lambda x: 4 ** x - 5 * x - 2
        df = lambda x: math.log(4) * (4 ** x) - 5
    elif number == 18:
        text = "ln(x + 1) - x^3 + 1 = 0"
        f = lambda x: math.log(x + 1) - x ** 3 + 1
        df = lambda x: 1 / (x + 1) - 3 * x * x
    elif number == 19:
        text = "x^4 - 2x - 1 = 0"
        f = lambda x: x ** 4 - 2 * x - 1
        df = lambda x: 4 * x ** 3 - 2
    elif number == 20:
        text = "tg(x) - 5x^2 + 1 = 0, x из [-1, 1]"
        f = lambda x: math.tan(x) - 5 * x * x + 1
        df = lambda x: 1 / (math.cos(x) ** 2) - 10 * x
    elif number == 21:
        text = "3*sqrt(x + 1) - e^x - 0.5 = 0"
        f = lambda x: 3 * math.sqrt(x + 1) - math.exp(x) - 0.5
        df = lambda x: 1.5 / math.sqrt(x + 1) - math.exp(x)
    elif number == 22:
        text = "10^x - 5x - 2 = 0"
        f = lambda x: 10 ** x - 5 * x - 2
        df = lambda x: ln10 * (10 ** x) - 5
    elif number == 23:
        text = "ln(x + 2) - x^4 + 0.5 = 0"
        f = lambda x: math.log(x + 2) - x ** 4 + 0.5
        df = lambda x: 1 / (x + 2) - 4 * x ** 3
    elif number == 24:
        text = "x^6 - 5x - 2 = 0"
        f = lambda x: x ** 6 - 5 * x - 2
        df = lambda x: 6 * x ** 5 - 5
    elif number == 25:
        text = "sqrt(x + 2) - 2*cos(x) = 0"
        f = lambda x: math.sqrt(x + 2) - 2 * math.cos(x)
        df = lambda x: 0.5 / math.sqrt(x + 2) + 2 * math.sin(x)
    elif number == 26:
        text = "lg(x + 1) - x + 0.5 = 0"
        f = lambda x: math.log10(x + 1) - x + 0.5
        df = lambda x: 1 / ((x + 1) * ln10) - 1
    elif number == 27:
        text = "x^6 - 5x^3 - 2 = 0"
        f = lambda x: x ** 6 - 5 * x ** 3 - 2
        df = lambda x: 6 * x ** 5 - 15 * x * x
    elif number == 28:
        text = "lg(2x + 1) - x^3 + 1 = 0"
        f = lambda x: math.log10(2 * x + 1) - x ** 3 + 1
        df = lambda x: 2 / ((2 * x + 1) * ln10) - 3 * x * x
    elif number == 29:
        text = "x^5 - 7x^2 + 3 = 0"
        f = lambda x: x ** 5 - 7 * x * x + 3
        df = lambda x: 5 * x ** 4 - 14 * x
    elif number == 30:
        text = "x*lg(x + 2) + x^2 - 1 = 0"
        f = lambda x: x * math.log10(x + 2) + x * x - 1
        df = lambda x: math.log10(x + 2) + x / ((x + 2) * ln10) + 2 * x
    else:
        raise ValueError("нет уравнения с номером " + str(number))
    return text, f, df


def simple_iteration(f, df, x0, eps, max_iter=100):
    q = df(x0)
    if q == 0.0:
        raise ValueError("производная в начальной точке равна нулю")
    x = x0
    rows = []
    for iteration in range(1, max_iter + 1):
        new_x = x - f(x) / q
        error = abs(new_x - x)
        rows.append((iteration, error, new_x))
        x = new_x
        if error < eps:
            return rows
    raise RuntimeError("простая итерация не сошлась")


def newton(f, df, x0, eps, max_iter=50):
    x = x0
    rows = []
    for iteration in range(1, max_iter + 1):
        derivative = df(x)
        if derivative == 0.0:
            raise ValueError("производная равна нулю, шаг Ньютона невозможен")
        new_x = x - f(x) / derivative
        error = abs(new_x - x)
        rows.append((iteration, error, new_x))
        x = new_x
        if error < eps:
            return rows
    raise RuntimeError("метод Ньютона не сошёлся")


def solve_equation(number, x0, eps):
    text, f, df = get_equation(number)
    simple_rows = simple_iteration(f, df, x0, eps)
    newton_rows = newton(f, df, x0, eps)
    simple_x = simple_rows[-1][2]
    newton_x = newton_rows[-1][2]
    if len(simple_rows) < len(newton_rows):
        faster = "простая итерация"
    elif len(newton_rows) < len(simple_rows):
        faster = "Ньютон"
    else:
        faster = "одинаково"
    return {
        "text": text,
        "x0": x0,
        "eps": eps,
        "slope": df(x0),
        "simple_rows": simple_rows,
        "newton_rows": newton_rows,
        "simple_x": simple_x,
        "newton_x": newton_x,
        "simple_f": f(simple_x),
        "newton_f": f(newton_x),
        "faster": faster,
    }
