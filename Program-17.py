import tkinter as tk
import ast
import operator

root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("340x460")
root.resizable(False, False)

expression = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=expression,
    font=("Arial", 22),
    justify="right",
    bd=10
)
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=15, ipady=10, sticky="nsew")

def evaluate(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.UnaryOp):
        value = evaluate(node.operand)
        if isinstance(node.op, ast.UAdd):
            return value
        if isinstance(node.op, ast.USub):
            return -value

    if isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)

        operations = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
        }

        operation = operations.get(type(node.op))
        if operation:
            return operation(left, right)

    raise ValueError("Invalid expression")

def click(value):
    if value == "C":
        expression.set("")

    elif value == "⌫":
        expression.set(expression.get()[:-1])

    elif value == "=":
        try:
            result = evaluate(ast.parse(
                expression.get(), mode="eval"
            ).body)
            expression.set(str(result))

        except ZeroDivisionError:
            expression.set("Cannot divide by zero")

        except (ValueError, SyntaxError, TypeError):
            expression.set("Invalid expression")

    else:
        if expression.get() in (
            "Invalid expression",
            "Cannot divide by zero"
        ):
            expression.set("")
        expression.set(expression.get() + value)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("⌫", 5, 0), ("=", 5, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(
        root,
        text=text,
        font=("Arial", 16),
        command=lambda value=text: click(value)
    )

    if text == "=":
        button.grid(row=row, column=col, columnspan=3,
                    padx=4, pady=4, sticky="nsew")
    else:
        button.grid(row=row, column=col,
                    padx=4, pady=4, sticky="nsew")

for row in range(1, 6):
    root.grid_rowconfigure(row, weight=1)

for col in range(4):
    root.grid_columnconfigure(col, weight=1)

root.mainloop()
