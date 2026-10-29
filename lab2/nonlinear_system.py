import math


def parameter(number):
    group = (number - 1) // 3
    place = (number - 1) % 3
    values = [
        (2, 3, 4),
        (1, 2, 3),
        (2, 3, 4),
        (1, 2, 3),
        (2, 3, 4),
        (2, 3, 4),
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
        (4, 5, 6),
    ]
    if group < 0 or group >= len(values):
        raise ValueError("нет системы с номером " + str(number))
    return values[group][place]


def get_system(number):
    a = parameter(number)
    group = (number - 1) // 3
    ln10 = math.log(10)

    if group == 0:
        text = "(x1^2 + a^2)*x2 - a^3 = 0\n(x1 - a/2)^2 + (x2 - a/2)^2 - a^2 = 0"

        def f(x):
            return [
                (x[0] * x[0] + a * a) * x[1] - a ** 3,
                (x[0] - a / 2) ** 2 + (x[1] - a / 2) ** 2 - a * a,
            ]

        def jacobian(x):
            return [
                [2 * x[0] * x[1], x[0] * x[0] + a * a],
                [2 * (x[0] - a / 2), 2 * (x[1] - a / 2)],
            ]
    elif group == 1:
        text = "x1 - cos(x2) = 1\nx2 - lg(x1 + 1) = a"

        def f(x):
            return [
                x[0] - math.cos(x[1]) - 1,
                x[1] - math.log10(x[0] + 1) - a,
            ]

        def jacobian(x):
            return [
                [1, math.sin(x[1])],
                [-1 / ((x[0] + 1) * ln10), 1],
            ]
    elif group == 2:
        text = "x1^2 + x2^2 - a^2 = 0\nx1 - e^x2 + a = 0"

        def f(x):
            return [
                x[0] * x[0] + x[1] * x[1] - a * a,
                x[0] - math.exp(x[1]) + a,
            ]

        def jacobian(x):
            return [
                [2 * x[0], 2 * x[1]],
                [1, -math.exp(x[1])],
            ]
    elif group == 3:
        text = "x1 - cos(x2) = a\nx2 - sin(x1) = a"

        def f(x):
            return [
                x[0] - math.cos(x[1]) - a,
                x[1] - math.sin(x[0]) - a,
            ]

        def jacobian(x):
            return [
                [1, math.sin(x[1])],
                [-math.cos(x[0]), 1],
            ]
    elif group == 4:
        text = "x1^2/a^2 + x2^2/(a/2)^2 - 1 = 0\na*x2 - e^x1 - x1 = 0"

        def f(x):
            return [
                x[0] * x[0] / (a * a) + x[1] * x[1] / ((a / 2) ** 2) - 1,
                a * x[1] - math.exp(x[0]) - x[0],
            ]

        def jacobian(x):
            return [
                [2 * x[0] / (a * a), 2 * x[1] / ((a / 2) ** 2)],
                [-math.exp(x[0]) - 1, a],
            ]
    elif group == 5:
        text = "a*x1 - cos(x2) = 0\na*x2 - e^x1 = 0"

        def f(x):
            return [
                a * x[0] - math.cos(x[1]),
                a * x[1] - math.exp(x[0]),
            ]

        def jacobian(x):
            return [
                [a, math.sin(x[1])],
                [-math.exp(x[0]), a],
            ]
    elif group == 6:
        text = "x1^2 - 2*lg(x2) - 1 = 0\nx1^2 - a*x1*x2 + a = 0"

        def f(x):
            return [
                x[0] * x[0] - 2 * math.log10(x[1]) - 1,
                x[0] * x[0] - a * x[0] * x[1] + a,
            ]

        def jacobian(x):
            return [
                [2 * x[0], -2 / (x[1] * ln10)],
                [2 * x[0] - a * x[1], -a * x[0]],
            ]
    elif group == 7:
        text = "a*x1^2 - x1 + x2^2 - 1 = 0\nx2 - tg(x1) = 0"

        def f(x):
            return [
                a * x[0] * x[0] - x[0] + x[1] * x[1] - 1,
                x[1] - math.tan(x[0]),
            ]

        def jacobian(x):
            return [
                [2 * a * x[0] - 1, 2 * x[1]],
                [-1 / (math.cos(x[0]) ** 2), 1],
            ]
    elif group == 8:
        text = "a*x1^2 - x2 + x2^2 - a = 0\nx1 - sqrt(x2 + a) + 1 = 0"

        def f(x):
            return [
                a * x[0] * x[0] - x[1] + x[1] * x[1] - a,
                x[0] - math.sqrt(x[1] + a) + 1,
            ]

        def jacobian(x):
            return [
                [2 * a * x[0], -1 + 2 * x[1]],
                [1, -0.5 / math.sqrt(x[1] + a)],
            ]
    else:
        text = "e^(x1*x2) + x1 - a = 0\nx1^2 - a*x2 - 1 = 0"

        def f(x):
            return [
                math.exp(x[0] * x[1]) + x[0] - a,
                x[0] * x[0] - a * x[1] - 1,
            ]

        def jacobian(x):
            exponent = math.exp(x[0] * x[1])
            return [
                [x[1] * exponent + 1, x[0] * exponent],
                [2 * x[0], -a],
            ]

    return text, a, f, jacobian


def solve_2x2(matrix, right):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a * d - b * c
    if det == 0.0:
        raise ValueError("матрица Якоби вырождена")
    dx1 = (right[0] * d - b * right[1]) / det
    dx2 = (a * right[1] - c * right[0]) / det
    return dx1, dx2


def infinity_norm(dx1, dx2):
    if abs(dx1) > abs(dx2):
        return abs(dx1)
    return abs(dx2)


def simple_iteration(f, jacobian, x0, eps, max_iter=100):
    matrix = jacobian(x0)
    x1 = x0[0]
    x2 = x0[1]
    rows = []
    for iteration in range(1, max_iter + 1):
        values = f([x1, x2])
        dx1, dx2 = solve_2x2(matrix, [-values[0], -values[1]])
        error = infinity_norm(dx1, dx2)
        x1 = x1 + dx1
        x2 = x2 + dx2
        rows.append((iteration, error, x1, x2))
        if error < eps:
            return rows
    raise RuntimeError("простая итерация для системы не сошлась")


def newton(f, jacobian, x0, eps, max_iter=50):
    x1 = x0[0]
    x2 = x0[1]
    rows = []
    for iteration in range(1, max_iter + 1):
        values = f([x1, x2])
        matrix = jacobian([x1, x2])
        dx1, dx2 = solve_2x2(matrix, [-values[0], -values[1]])
        error = infinity_norm(dx1, dx2)
        x1 = x1 + dx1
        x2 = x2 + dx2
        rows.append((iteration, error, x1, x2))
        if error < eps:
            return rows
    raise RuntimeError("метод Ньютона для системы не сошёлся")


def solve_system(number, x0, eps):
    text, a, f, jacobian = get_system(number)
    simple_rows = simple_iteration(f, jacobian, x0, eps)
    newton_rows = newton(f, jacobian, x0, eps)
    simple_x = [simple_rows[-1][2], simple_rows[-1][3]]
    newton_x = [newton_rows[-1][2], newton_rows[-1][3]]
    if len(simple_rows) < len(newton_rows):
        faster = "простая итерация"
    elif len(newton_rows) < len(simple_rows):
        faster = "Ньютон"
    else:
        faster = "одинаково"
    return {
        "text": text,
        "a": a,
        "x0": x0,
        "eps": eps,
        "simple_rows": simple_rows,
        "newton_rows": newton_rows,
        "simple_x": simple_x,
        "newton_x": newton_x,
        "simple_f": f(simple_x),
        "newton_f": f(newton_x),
        "faster": faster,
    }
