import sys

from nonlinear import solve_equation
from nonlinear_system import solve_system


def read_tokens(path):
    with open(path, encoding="utf-8") as source:
        return source.read().split()


def format_number(value):
    if abs(value) < 1e-9:
        value = 0.0
    return f"{value:.6g}"


def print_scalar_table(rows):
    print("  итерация    погрешность    приближение")
    for iteration, error, x in rows:
        print(f"  {iteration:8d}    {format_number(error):>12}    {format_number(x)}")


def print_system_table(rows):
    print("  итерация    погрешность    x1    x2")
    for iteration, error, x1, x2 in rows:
        print(
            f"  {iteration:8d}    {format_number(error):>12}"
            f"    {format_number(x1)}    {format_number(x2)}"
        )


def print_scalar(number, x0, eps):
    result = solve_equation(number, x0, eps)
    print(f"Уравнение {number}: {result['text']}")
    print(f"ε = {format_number(result['eps'])}")
    print(f"Начальное приближение x0 = {format_number(result['x0'])}")
    print("Его берут по графику и записывают во входной файл.")
    print(f"f'(x0) = {format_number(result['slope'])}")
    print()
    print("Простая итерация: x = x - f(x) / f'(x0)")
    print_scalar_table(result["simple_rows"])
    print(f"Корень: {format_number(result['simple_x'])}")
    print(f"Проверка f(x) = {format_number(result['simple_f'])}")
    print(f"Итераций: {len(result['simple_rows'])}")
    print()
    print("Метод Ньютона: x = x - f(x) / f'(x)")
    print_scalar_table(result["newton_rows"])
    print(f"Корень: {format_number(result['newton_x'])}")
    print(f"Проверка f(x) = {format_number(result['newton_f'])}")
    print(f"Итераций: {len(result['newton_rows'])}")
    print()
    print(f"Быстрее сошёлся: {result['faster']}")
    print("У Ньютона погрешность обычно падает быстрее: производная обновляется каждый шаг.")
    print()


def print_system(number, x0, eps):
    result = solve_system(number, x0, eps)
    print(f"Система {number}, a = {format_number(result['a'])}")
    print(result["text"])
    print(f"ε = {format_number(result['eps'])}")
    print(
        "Начальное приближение: "
        f"x1 = {format_number(x0[0])}, x2 = {format_number(x0[1])}"
    )
    print("Его берут по графику и записывают во входной файл.")
    print("Погрешность — бесконечная норма поправки, то есть максимум из |dx1| и |dx2|.")
    print()
    print("Простая итерация: матрица Якоби фиксируется в начальной точке")
    print_system_table(result["simple_rows"])
    print(
        "Решение: "
        f"x1 = {format_number(result['simple_x'][0])}, "
        f"x2 = {format_number(result['simple_x'][1])}"
    )
    print(
        "Проверка F: "
        f"{format_number(result['simple_f'][0])}  {format_number(result['simple_f'][1])}"
    )
    print(f"Итераций: {len(result['simple_rows'])}")
    print()
    print("Метод Ньютона: матрица Якоби считается заново на каждом шаге")
    print_system_table(result["newton_rows"])
    print(
        "Решение: "
        f"x1 = {format_number(result['newton_x'][0])}, "
        f"x2 = {format_number(result['newton_x'][1])}"
    )
    print(
        "Проверка F: "
        f"{format_number(result['newton_f'][0])}  {format_number(result['newton_f'][1])}"
    )
    print(f"Итераций: {len(result['newton_rows'])}")
    print()
    print(f"Быстрее сошёлся: {result['faster']}")
    print()


def main():
    if len(sys.argv) != 2:
        print("Запуск: python3 lab.py <файл>")
        print("Пример: python3 lab.py examples/scalar/01.txt")
        return 1

    tokens = read_tokens(sys.argv[1])
    kind = tokens[0]
    number = int(tokens[1])
    if kind == "scalar":
        print_scalar(number, float(tokens[2]), float(tokens[3]))
    elif kind == "system":
        x0 = [float(tokens[2]), float(tokens[3])]
        print_system(number, x0, float(tokens[4]))
    else:
        raise ValueError("первая строка файла должна быть scalar или system")
    return 0


if __name__ == "__main__":
    sys.exit(main())
