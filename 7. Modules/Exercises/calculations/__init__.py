def basic_calculations(num1, num2, operator):
    mapper = {
        '/': float(num1) / int(num2),
        '*': float(num1) * int(num2),
        '-': float(num1) - int(num2),
        '+': float(num1) + int(num2),
        '^': float(num1) ** int(num2)
    }

    return f'{mapper[operator]:.2f}'
